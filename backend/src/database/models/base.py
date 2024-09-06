import os
from sqlalchemy import text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from threading import local


class DatabaseConnection:
    _instance = None
    _thread_local = local()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        DATABASE_URL = os.getenv('DATABASE_URL')
        if not DATABASE_URL:
            raise ValueError("DATABASE_URL is not defined!")

        self.engine = create_engine(
            f"{DATABASE_URL}",
            # pool_size=20,
            # max_overflow=40,
            # pool_recycle=3600,
            pool_pre_ping=True
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def get_db(self):
        db = self._thread_local.db
        if db is None:
            db = self._thread_local.db = self.SessionLocal()
        try:
            yield db
        finally:
            self._thread_local.db = None


db_connect = DatabaseConnection()
