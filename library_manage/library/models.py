from django.db import models


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    addr = models.CharField(max_length=128, default="北京")

    def __str__(self):
        return "<Publisher object：>".format(self.name)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.DO_NOTHING)

    def __str__(self):
        return "<Book object：{}>".format(self.title)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True, null=False)
    # 多对多关联book
    book = models.ManyToManyField(to=Book)

    def __str__(self):
        return "<Author object>: {}".format(self.name)


