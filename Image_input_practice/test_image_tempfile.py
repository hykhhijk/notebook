"""
test_image_tempfile.py

이미지를 임시 파일로 저장한 뒤 base64로 인코딩하여 OpenAI API에 전달하는 테스트 코드.
로컬 파일이나 비공개 URL처럼 직접 URL을 넘길 수 없는 경우에 사용한다.
"""

import base64
import os
import tempfile
import urllib.request
from openai import OpenAI

SAMPLE_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png"


def download_image(url: str) -> bytes:
    """URL에서 이미지를 다운로드하여 바이트로 반환한다.

    Args:
        url: 다운로드할 이미지의 URL.

    Returns:
        이미지 바이너리 데이터.
    """
    with urllib.request.urlopen(url) as response:
        return response.read()


def encode_image_to_base64(image_bytes: bytes) -> str:
    """이미지 바이트를 base64 문자열로 인코딩한다.

    Args:
        image_bytes: 인코딩할 이미지 바이너리 데이터.

    Returns:
        base64로 인코딩된 문자열.
    """
    return base64.b64encode(image_bytes).decode("utf-8")


def analyze_image_from_tempfile(image_url: str, prompt: str = "이 이미지를 설명해주세요.") -> str:
    """이미지를 임시 파일로 저장 후 base64로 인코딩하여 OpenAI API로 분석한다.

    URL에서 이미지를 다운로드 → NamedTemporaryFile에 저장 → base64 인코딩 →
    data URL 형태로 API 호출. with 블록 종료 시 임시 파일은 자동으로 삭제된다.

    Args:
        image_url: 분석할 이미지의 URL.
        prompt: 이미지에 대해 모델에게 전달할 질문 또는 지시문.

    Returns:
        모델의 응답 텍스트.
    """
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    image_bytes = download_image(image_url)

    with tempfile.NamedTemporaryFile(suffix=".png", delete=True) as tmp:
        tmp.write(image_bytes)
        tmp.flush()

        encoded = encode_image_to_base64(image_bytes)
        data_url = f"data:image/png;base64,{encoded}"

        print(f"임시 파일 경로: {tmp.name}")

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": data_url}},
                    ],
                }
            ],
        )

    return response.choices[0].message.content


def main():
    """샘플 이미지 URL로 테스트를 실행한다."""
    print(f"이미지 URL: {SAMPLE_IMAGE_URL}\n")
    result = analyze_image_from_tempfile(SAMPLE_IMAGE_URL)
    print("모델 응답:")
    print(result)


if __name__ == "__main__":
    main()
