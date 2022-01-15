from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    """Store an user in the database."""
    pass

