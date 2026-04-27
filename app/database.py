from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# commit permanent changes to db and flush temprory changes to db, default values here F,T

Base = declarative_base() #old way deprecated now new way use class Base(DeclarativeBase):


#def get_db()-> Generator[Session, None, None]: #added by chatgpt

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                     password='051727', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was sucessfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)   
#         time.sleep(2)