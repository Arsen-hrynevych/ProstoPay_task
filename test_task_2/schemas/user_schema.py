from pydantic import (
    BaseModel,
    EmailStr,
    Field,
)
from typing import Optional


class UserDTO(BaseModel):
    """
    User Data Transfer Object (DTO) for handling user data.

    Attributes:
    name: The name of the user.
    email: The email address of the user.
    age: The age of the user. This field is optional.
    """
    name: str = Field(..., description="The name of the user.")
    email: EmailStr = Field(..., description="The email address of the user.")
    age: Optional[int] = Field(None, gt=0, description="The age of the user. Must be a positive integer.")

    class Config:
        from_attributes = True