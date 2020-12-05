#HACK: Removes error-message for "from pydantic import BaseModel" statement
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# Find tutorial here: https://fastapi.tiangolo.com/

from pydantic import BaseModel

class TemplateArgs(BaseModel):
    id: int
    name: str
    width: int
    height: int
    tags: list
    createdDate: str
    status: bool

