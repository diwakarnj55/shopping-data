from django.db import models

class Purchase(models.Model):
    item=models.TextField(max_length=200)
    price=models.IntegerField()
    image=models.TextField(max_length=200)
    desc=models.TextField(max_length=200)
    def __str__(self):
        return self.item
