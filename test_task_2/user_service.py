from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user_model import User
from schemas.user_schema import UserDTO

from db.session import get_async_session


class UserService:
    """
    A service class for managing User operations in an asynchronous context.
    """
    def __init__(self, session: AsyncSession = None):
        self._session = session

    async def __aenter__(self):
        if self._session is None:
            self._session = get_async_session()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self._session is not None:
            await self._session.close()

    async def get_user(self, user_id: int) -> UserDTO | None:
        """
        Retrieve a User by their ID. Returns a UserDTO if found, otherwise None.
        """
        result = await self._session.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            return UserDTO.from_orm(user)
        return None

    async def add(self, user: UserDTO) -> UserDTO:
        """
        Add a new User to the database from a UserDTO. Returns the added UserDTO.
        """
        db_user = User(name=user.name, email=user.email, age=user.age)
        self._session.add(db_user)
        await self._session.commit()
        await self._session.refresh(db_user)
        return db_user
