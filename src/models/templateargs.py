#HACK: Removes error-message for "from pydantic import BaseModel" statement
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# Find tutorial here: https://fastapi.tiangolo.com/

from pydantic import BaseModel
from typing import Optional

class TemplateArgs(BaseModel):
    id: int
    name: str
    width: int
    height: int
    tags: Optional[list] = None
    createdDate: str
    createdBy: str
    updatedDate: Optional[str] = None
    updatedBy: Optional[str] = None
    isDeleted: Optional[bool] = None
    deletedDate: Optional[str] = None
    deletedBy: Optional[str] = None
    isReady: Optional[bool] = None


