from datetime import timedelta, timezone, datetime
import jwt

# openssl rand -hex 32
SECRET_KEY = "574fc04774f9371e49dbefa44eeb9594a55d3521b31052651b0ed522c9d9cf82"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(user_data: dict):
  to_encode = user_data.copy()
  expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

  return encoded_jwt
