from pydantic import BaseModel, Field


class Lugar(BaseModel):

    id: int | None = None
    name: str = Field(min_lenght=3)
    description: str | None = None 
    precio: float = Field(gt=0)
    limite: int = Field(ge=0)

