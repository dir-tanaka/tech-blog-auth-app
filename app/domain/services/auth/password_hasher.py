import hashlib
import os

class PasswordHasher:
  def __init__(self, salt: str, password_hash: str):
    # 受け取った引数をインスタンス変数として保存
    self.salt = salt
    self.password_hash = password_hash

  async def hash_password(password: str):
    # salt をバイト列で生成し、16進数文字列に変換
    salt = os.urandom(16).hex()
    password_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    # PasswordHasherクラスに文字列として渡す
    return PasswordHasher(salt=salt, password_hash=password_hash)
  
  async def test_hash_password(salt: str, password: str):
    password_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    return password_hash
