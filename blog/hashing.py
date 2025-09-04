from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hash():
    @staticmethod #means not for a certain object it is an utility method 
    def encrypt(password:str) -> str:
        hashed_pass=pwd_context.hash(password)
        return hashed_pass
    
    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_context.verify(plain_password, hashed_password)