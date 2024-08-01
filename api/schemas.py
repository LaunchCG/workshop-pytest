from pydantic import BaseModel

class Consultant(BaseModel):
    consultant_name: str
    consultant_title: str | None = None
    consultant_location: str | None = None
    consultant_discipline: str


class Discipline(BaseModel):
    discipline_name: str
    studio_name: str


class Studio(BaseModel):
    studio_name: str