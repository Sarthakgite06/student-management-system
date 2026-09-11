from pydantic import BaseModel ,Field
from typing import Annotated

class StudentStruct(BaseModel):
    roll:Annotated[int,Field(title="Enter roll")]
    name:Annotated[str,Field(title="Enter name")]
    age: Annotated[int,Field(title="Enter age")]
    
