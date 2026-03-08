"""
test_image_url.py

이미지 URL을 OpenAI API에 직접 전달하여 분석하는 테스트 코드.
"""

import os
from openai import OpenAI

SAMPLE_IMAGE_URL = "https://placehold.co/600x400.png?text=Hello+World"


def analyze_image_from_url(image_url: str, prompt: str = "이 이미지를 설명해주세요.") -> str:
    """이미지 URL을 OpenAI API에 직접 전달하여 분석한다.

    Args:
        image_url: 분석할 이미지의 공개 URL.
        prompt: 이미지에 대해 모델에게 전달할 질문 또는 지시문.

    Returns:
        모델의 응답 텍스트.
    """
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }
        ],
    )

    return response.choices[0].message.content


def main():
    """샘플 이미지 URL로 테스트를 실행한다."""
    print(f"이미지 URL: {SAMPLE_IMAGE_URL}\n")
    result = analyze_image_from_url(SAMPLE_IMAGE_URL)
    print("모델 응답:")
    print(result)


if __name__ == "__main__":
    main()
