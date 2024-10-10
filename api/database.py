from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQL_ALCHEMY_DATABASE_URL = 'sqlite:///workout_app.db'
# Update with your PostgreSQL database credentials
SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:ajncarz123@localhost:5432/fastapi'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False , autoflush=False , bind = engine)

Base = declarative_base()

