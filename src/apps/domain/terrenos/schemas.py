from core.schema import BaseSchema, ModelSchema


class TerrenoCreate(BaseSchema):
    # validate latitude e longitude
    name: str
    latitude: float
    longitude: float
    endereço: str | None


class UserResponse(ModelSchema):
    id: int
    name: str
    latitude: float
    longitude: float
    endereço: str | None
    # email: str
