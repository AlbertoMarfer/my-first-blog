from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class School(models.Model):
    LANGUAGES_CHOICES = (
    ('EN', 'English'),
    ('DE', 'German'),
    ('ES', 'Spanish'),
    ('IT', 'Italian'),
    ('FR', 'French'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=4)
    laungagues = models.CharField(max_length=2, choices=LANGUAGES_CHOICES)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
