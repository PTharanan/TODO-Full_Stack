from django.db import models

class Data(models.Model):
    task_tit = models.CharField(max_length=20)
    tasks = models.CharField(max_length=200)

    def __str__(self):
        return self.task_tit
