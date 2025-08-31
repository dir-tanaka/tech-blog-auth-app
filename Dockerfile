FROM python:3.9

WORKDIR /app

# Pipfile と Pipfile.lock をコピー
COPY Pipfile /app/
COPY Pipfile.lock /app/

# Pipenv を使って依存関係をインストール
RUN pip install pipenv && pipenv install --system --deploy

# アプリケーションコードをコピー
COPY ./app /app/

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
