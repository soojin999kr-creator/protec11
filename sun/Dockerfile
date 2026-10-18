STREAMING_CHUNK:Setting up base image...

가볍고 최적화된 파이썬 3.9 이미지 사용

FROM python:3.9-slim

컨테이너 내 작업 디렉토리 설정

WORKDIR /app

STREAMING_CHUNK:Installing dependencies...

라이브러리 설치 파일 복사 및 설치

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

애플리케이션 전체 코드 복사

COPY . .

외부로 노출할 포트 명시 (Cloud Run 문서화 용도)

EXPOSE 8080

컨테이너 실행 시 작동할 명령어

CMD ["python", "main.py"]
