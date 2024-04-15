from sqlalchemy import (
    Column,
    Integer,
    String,
)

from db.session import Base


class User(Base):
    """
    User model for handling user data in the database.

    Attributes:
    id: The unique identifier of the user.
    name: The name of the user.
    email: The email address of the user.
    age: The age of the user. This field is optional.
    password_hash: The hashed password of the user.
    posts: The posts created by the user.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    email = Column(String(64), unique=True, index=True)
    age = Column(Integer)
