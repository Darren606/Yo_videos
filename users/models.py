from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.base_model import BaseModel


class UserModel(AbstractUser, BaseModel):
    user_icon = models.FileField('profile_photo', max_length=200, null=True, blank=True)
    city = models.CharField('City', max_length=30, null=True, blank=True)
    age = models.IntegerField('Age', null=True, blank=True)
    email = models.CharField('Email', unique=True, max_length=50)

    class Meta:
        db_table = 't_users'
        verbose_name = 'users_table'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username


class UserfocusModel():
    cur_user = models.ForeignKey('UserModel', verbose_name='current_users', related_name='cur_user_list',
                                 on_delete=models.CASCADE)
    focus_user = models.ForeignKey('UserModel', verbose_name='focused_user', related_name='focus_user_list',
                                   on_delete=models.CASCADE)

    class Meta:
        db_table = 't_user_focus'
        verbose_name = 'userfocus_table'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.cur_user.username + self.focus_user.username
