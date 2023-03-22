from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Curse(models.Model):
    title = models.CharField(max_length=25, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")
    create_date = models.DateTimeField(auto_now=True, verbose_name="Создано")
    updated_date = models.DateTimeField(auto_now_add=True, verbose_name="Обновлено")
    is_published = models.BooleanField(default=True, verbose_name="Публиковать")
    group = models.ForeignKey("GroupC", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self,):
        # return f"/news/{self.URL}/"
        return reverse('curse', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["-create_date"]


class GroupC(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название", db_index=True)
    description = models.TextField(verbose_name="Описание")
    create_date = models.DateTimeField(auto_now=True, verbose_name="Создано")

    def __str__(self):
        return self.name

    def get_absolute_url(self,):
        # return f"/news/{self.URL}/"
        return reverse('curses',)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["-create_date"]


class Homework(models.Model):
    title = models.CharField(max_length=25, verbose_name="Название")
    file = models.FileField(upload_to="homework/%Y/%m/%d", verbose_name="Домашка")
    create_date = models.DateTimeField(auto_now=True, verbose_name="Создано")
    author = models.CharField(max_length=25, verbose_name="Автор")
    curse = models.ForeignKey("Curse", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Домашка"
        verbose_name_plural = "Домашки"
        ordering = ["-create_date"]




