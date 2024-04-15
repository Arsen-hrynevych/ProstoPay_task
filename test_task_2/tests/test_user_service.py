import pytest
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from user_service import UserService
from schemas.user_schema import UserDTO
from utils import get_env_variable

# Mocking database connection
DATABASE_URL = get_env_variable('DATABASE_URL')
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@pytest.mark.asyncio
async def test_user_service():
    async with async_session_maker() as session:
        user_service = UserService(session)

        user_data = {"name": "John Doe", "email": "john@example.com", "age": 30}
        user_dto = UserDTO(**user_data)

        added_user = await user_service.add(user_dto)
        assert added_user.name == user_data["name"]
        assert added_user.email == user_data["email"]
        assert added_user.age == user_data["age"]

        retrieved_user = await user_service.get_user(added_user.id)
        assert retrieved_user.name == user_data["name"]
        assert retrieved_user.email == user_data["email"]
        assert retrieved_user.age == user_data["age"]

        non_existent_user = await user_service.get_user(-1)
        assert non_existent_user is None
