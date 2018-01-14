# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class items(models.Model):
    item_name = models.CharField(max_length=20)
    item_pic = models.URLField(default="#")
    item_price = models.PositiveIntegerField(default=0)
    item_cost = models.PositiveIntegerField(default=0)
    item_num = models.PositiveIntegerField(default=0)
    item_des = models.TextField(default='暂无说明')

    def __unicode__(self):
        return self.item_name