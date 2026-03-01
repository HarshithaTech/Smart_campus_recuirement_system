from pydantic import BaseModel, ConfigDict
from typing import Optional, List, Any
from datetime import datetime

class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class UserBase(BaseSchema):
    email: str
    full_name: str
    role: str

class StudentCreate(UserBase):
    password: str

class StudentRead(UserBase):
    id: int
    created_at: datetime

class JobRoleBase(BaseSchema):
    title: str
    description: str
    requirements: List[str]

class InterviewSessionBase(BaseSchema):
    student_id: int
    job_role_id: int
    status: str
