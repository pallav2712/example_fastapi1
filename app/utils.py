from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# deprecated Matlab:
# agar future mein algorithm change ho (bcrypt → kuch aur)
# toh old hashes ko automatically upgrade kar sakta hai
def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)