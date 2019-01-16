from django.db import models

class Task(models.Model):

    class Meta:
        db_table = "tasks"

    name = models.CharField(verbose_name='名前', max_length=100, null=False)

    def __str__(self):
        return f"{self.id} {self.name}"
