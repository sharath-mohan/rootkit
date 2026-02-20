from sqlalchemy import create_engine, text, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Session
from datetime import datetime, timezone
from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv()
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"


def create_user(username, email, password):
    with Session(engine) as session:
        user = User(username=username, email=email, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
    return user


def test_connection():
    try:
        # Attempt to connect and execute a simple query
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("PostgreSQL connection successful!")
    except Exception as e:
        print("Failed to connect to PostgreSQL.")
        print(f"Error: {e}")


if __name__ == "__main__":
    test_connection()
    Base.metadata.create_all(engine)
    fake = Faker()
    user = create_user(fake.user_name(), fake.email(), "password")
    print(f"User created: {user}")
