# 경량 웹서버를 Docker image로 빌드하기

- Web, App: Flask, Gunicorn
- Container: Docker

----
## 도커 실행하기
```
# 도커 이미지 빌드하기
docker build -t [image name]:[image tag]

# 도커 컨테이너 실행하기 
docker run -d -p 8000:8000 --name [container name] [image name]:[image tag]
```
