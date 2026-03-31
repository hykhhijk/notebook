# 버전확인
minikube version

# 가상머신 시작
minikube start --driver=docker
# 특정 k8s 버전 실행
minikube start --kubernetes-version=v1.34.0

# 상태확인
minikube status


- Kubectl 명령어는 minikube돌려야 실행가능

---
# minikube 상태확인
minikube status

# minikube 실행
minikube start

# 특정 k8s 버전 실행
minikube start --kubernetes-version=v1.23.1


# minikube ip 확인 (접속테스트시 필요)
minikube ip

# minikube 종료
minikube stop

# minikube 제거
minikube delete