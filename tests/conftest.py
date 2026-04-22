from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import schemas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings
from app.database import get_db
from app.database import Base



SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.
database_password}@{settings.database_hostname}:{settings.database_port}/{settings.
database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# commit permanent changes to db and flush temprory changes to db, default values here F,T

Base.metadata.create_all(bind=engine) 


#def get_db()-> Generator[Session, None, None]: #added by chatgpt

# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db

#client = TestClient(app)

@pytest.fixture()  #scope="module"
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# @pytest.fixture
# def client():
# # run our code before run our test
#     # Base.metadata.drop_all(bind=engine)
#     # Base.metadata.create_all(bind=engine)
#     yield TestClient(app)
# #run our code after our test finishes
#     #Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def client(session):
    def override_get_db():
    
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db        
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data = {"email": "pallav@gmail.com",
                 "password": "password123"}
    res = client.post("/users", json=user_data)

    assert res.status_code == 201
    
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user