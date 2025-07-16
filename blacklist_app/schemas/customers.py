from pydantic import BaseModel
import datetime


class InCustomer(BaseModel):
    """
    * first_name - имя
    * last_name - фамилия
    * middle_name - отчество
    * birth_date - дата рождения
    * reason_id - причина внесения в черный список
    * created_at - дата добавления записи
    """

    first_name: str
    last_name: str
    middle_name: str | None
    birth_date: datetime.date
    reason_id: int
    created_at: datetime.date


class Customer(InCustomer):
    """* id - уникальный идентификатор записи"""

    id: int
