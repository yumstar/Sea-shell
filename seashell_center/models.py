from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class CenterUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('An email is required to create a user.')
        if not password:
            raise ValueError('A password is required to create a user.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('An email is required to create a user.')
        if not password:
            raise ValueError('A password is required to create a user.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user


class CenterUser(AbstractBaseUser, PermissionsMixin):
    center_user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=60, unique=True)
    name = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CenterUserManager()
    def __str__(self):
        return self.get_username()

class Tag(models.Model):
    user = models.ForeignKey('seashell_center.CenterUser', related_name="tags", on_delete=models.CASCADE)
    text = models.CharField(blank=False, max_length=60)
    color = models.CharField(max_length= 50)

class Message(models.Model):
    user = models.ForeignKey('seashell_center.CenterUser', related_name='messages', on_delete=models.CASCADE)
    # body
    body = models.TextField(blank=True)
    # time
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.created.__str__() + ": " + self.body.__str__()

    class Meta:
        ordering = ['created']

class DayExperience(models.Model):
    GREAT = 5
    GOOD = 4
    OKAY = 3
    SUBPAR = 2
    AWFUL = 1
    EXPERIENCE_CHOICES = [(GREAT, "Great"), (GOOD, "Good"), (OKAY, "Okay"), (SUBPAR, "Subpar"), (AWFUL, "Awful")]
    user = models.ForeignKey('seashell_center.CenterUser',related_name='day_experiences', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    experience = models.IntegerField(choices=EXPERIENCE_CHOICES)

    class Meta:
        ordering = ['date']