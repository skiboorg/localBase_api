from django.db import models


class Column(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    order_num = models.IntegerField(default=0)



    class Meta:
        ordering = ('order_num',)

class Task(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, blank=True, null=True, related_name='tasks')
    order_num = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('order_num',)


class Tab(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    order_num = models.IntegerField(default=0)

    class Meta:
        ordering = ('order_num',)

class Param(models.Model):
    order_num = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('order_num',)


class Record(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE, blank=True, null=True, related_name='records')
    order_num = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('order_num',)


class RecordParam(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, blank=True, null=True, related_name='params')
    param = models.ForeignKey(Param, on_delete=models.CASCADE, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)