from tortoise import models, fields


class ReasonsORM(models.Model):
    """
    reasons:

    * id - уникальный идентификатор причины
    * name - человекочитаемое именование причины
    * slug - машинное именование причины
    * description - развернутое описание причины
    """

    id = fields.IntField
    name = fields.CharField(pk=True)
    slug = fields.CharField()
    description = fields.TextField()

    def __str__(self):
        return self.name

    class Meta:
        table = "reasons"
