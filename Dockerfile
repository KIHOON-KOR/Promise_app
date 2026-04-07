# 파이썬 3.13 버전의 가벼운(slim) 운영체제를 기본 바탕으로 가져옵니다.
FROM python:3.13-slim

# 파이썬 출력을 버퍼링하지 않고 콘솔에 즉시 출력하도록 설정하여 로그 확인을 쉽게 합니다.
ENV PYTHONUNBUFFERED=1

# 파이썬이 불필요한 바이트코드(.pyc) 파일을 생성하지 않도록 강제하여 컨테이너 용량을 아낍니다.
ENV PYTHONDONTWRITEBYTECODE=1

# 컨테이너 내부에서 작업이 이루어질 기본 디렉토리를 /app으로 지정합니다.
WORKDIR /app

# 운영체제 패키지 목록을 업데이트하고 데이터베이스 연결 등에 필요한 필수 시스템 패키지들을 설치합니다.
RUN apt-get update && apt-get install -y \
    # 인터넷에서 데이터를 다운로드하기 위한 도구입니다.
    curl \
    # 포스트그레SQL 데이터베이스와 파이썬을 연결할 때 필요한 핵심 라이브러리입니다.
    libpq-dev \
    # C 언어로 작성된 파이썬 패키지를 설치할 때 필요한 컴파일러입니다.
    gcc \
    # 설치가 끝난 후 불필요해진 임시 파일(캐시)을 삭제하여 도커 이미지 크기를 대폭 줄입니다.
    && rm -rf /var/lib/apt/lists/*

# 파이썬 기본 패키지 관리자를 사용하여 Poetry를 전역으로 깔끔하게 설치합니다.
RUN pip install poetry

# 도커 자체가 이미 격리된 공간이므로, Poetry가 내부에 또 가상환경을 만들지 않도록 설정을 끕니다.
RUN poetry config virtualenvs.create false

# 패키지 명세서와 자물쇠 파일을 소스 코드보다 먼저 복사하여 도커의 캐시 기능을 최대한 활용합니다.
COPY pyproject.toml poetry.lock /app/

# 명세서를 읽어 의존성 패키지들을 설치하되, 개발용 도구를 제외하고 사용자 묻기 및 색상 출력을 무시합니다.
RUN poetry install --without dev --no-root --no-interaction --no-ansi

# 나머지 모든 프로젝트 소스 코드를 도커 컨테이너 내부의 /app 디렉토리로 마저 복사합니다.
COPY . /app/