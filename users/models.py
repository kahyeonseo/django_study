from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):

    def create_customer(self, email, password, **extra_fields):
        extra_fields.setdefault('is_owner', False)
        if email is None:
            raise ValueError('Users must have an email address')
        if password is None:
            raise ValueError('Users must have a password')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(email, password, **extra_fields)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    GenderChoices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    email = models.EmailField(max_length=30, null=False, unique=True) # 이메일
    is_active = models.BooleanField(default=False) #
    phone = models.CharField(max_length=13, unique=True) # 전화 번호
    nickname = models.CharField(max_length=12) # 이름(닉네임)
    birthday = models.DateField(null=True, blank=True) # 생일
    gender = models.CharField(choices=GenderChoices) # 성별
    is_owner = models.BooleanField(default=False) # 주인 여부

    objects = UserManager()

    USERNAME_FIELD = 'email'
