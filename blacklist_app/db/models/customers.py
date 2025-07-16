from tortoise import models, fields


class CustomersORM(models.Model):
    """
    blacklist_customer:
    * id - уникальный идентификатор записи
    * first_name - имя
    * last_name - фамилия
    * middle_name - отчество
    * birth_date - дата рождения
    * reason_id - причина внесения в черный список
    * created_at - дата добавления записи

    """

    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=30)
    middle_name = fields.CharField(max_length=30)
    birth_date = fields.DatetimeField()
    reasons = fields.ForeignKeyField(
        model_name="models.ReasonsORM",
        related_name="customers",
        source_field="reason_id",
    )
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        table = "blacklist_customer"
        unique_together = ("first_name", "last_name", "middle_name", "birth_date")
