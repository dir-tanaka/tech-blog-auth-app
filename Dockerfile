FROM python:3.9

# Pipfile と Pipfile.lock をコピー
COPY Pipfile /
COPY Pipfile.lock /

# Pipenv を使って依存関係をインストール
RUN pip install pipenv && pipenv install --system --deploy

# アプリケーションコードをコピー
COPY ./app /app/

ENTRYPOINT ["uvicorn", "app.asgi:app", "--host", "0.0.0.0", "--port", "8888"]
