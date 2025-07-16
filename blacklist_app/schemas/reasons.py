from pydantic import BaseModel


class InReason(BaseModel):
    """
    * name - человекочитаемое именование причины
    * slug - машинное именование причины
    * description - развернутое описание причины
    """

    name: str
    slug: str
    description: str


class Reason(InReason):
    """
    * id - уникальный идентификатор причины
    """

    id: int
