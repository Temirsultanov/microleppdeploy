from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100, help_text="Введите название курса", verbose_name="Название")
    desc = models.TextField(max_length=1000, help_text="Введите описание курса", verbose_name="Описание")
    img = models.TextField(max_length=100, default="default.png", help_text="Укажите путь к фотографии", verbose_name="Фотография")
    class Meta:
        permissions = (("can_mark_returned", "Set course as returned"),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', args=[str(self.id)])

class Card(models.Model):
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, help_text="Введите заголовок карточки",verbose_name="Заголовок")
    text = models.TextField(max_length=1000, help_text="Введите контент карточки", verbose_name="Контент карточки")
    queue = models.IntegerField(help_text="Введите место в очереди", verbose_name="Место в очереди")
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный ID")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["queue"]

    def get_absolute_url(self):
        return reverse('card-detail', args=[str(self.id)])

class UsersStats(models.Model):
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    # pupil = models.ForeignKey('User')
    pupil = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    USER_STATUS = (
        ('p', 'process'),
        ('f', 'finished')
    )
    status = models.CharField(max_length=1, choices=USER_STATUS, blank=True)
    time = models.DateField(null=True, blank=False)
    def __str__(self):
        return '%s (%s)' % (self.course, self.pupil)

