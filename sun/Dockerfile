FROM python:3.9-slim

작업 디렉토리 설정

WORKDIR /app

라이브러리 설치 파일 복사 및 설치

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

애플리케이션 전체 코드 복사

COPY . .

외부로 노출할 포트 명시

EXPOSE 8080

컨테이너 실행 시 작동할 명령어

CMD ["python", "main.py"]
