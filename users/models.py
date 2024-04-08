   
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    
    

# class User(AbstractBaseUser):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     referral_code = models.CharField(max_length=10, blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     objects = UserManager()





# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     referral_code = models.CharField(max_length=20, blank=True, null=True)
#     registration_timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username



# from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     referral_code = models.CharField(max_length=10, blank=True, null=True)
#     points = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name
