from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):    
   use_in_migrations = True    

   def create_user(self, email, organization, password):        
       if not email:            
           raise ValueError('must have user email')
       if not password:            
           raise ValueError('must have user password')

       user = self.model(            
           email=self.normalize_email(email),
           organization=organization              
       )        
       user.set_password(password)        
       user.save(using=self._db)        
       return user

   def create_superuser(self, email, organization, password):        
       user = self.create_user(            
           email = self.normalize_email(email),
           organization=organization,                       
           password=password        
       )
       user.is_admin = True
       user.is_superuser = True
       user.save(using=self._db)
       return user 


class User(AbstractBaseUser, PermissionsMixin):    
   
   objects = UserManager()
   
   email = models.EmailField(        
       max_length=255,        
       unique=True,    
   )
   organization = models.CharField(max_length=30)
   is_active = models.BooleanField(default=True)
   is_admin = models.BooleanField(default=False)

   USERNAME_FIELD = 'email'    
   REQUIRED_FIELDS = ['organization']

   def __str__(self):
       return self.email

   @property
   def is_staff(self):
       return self.is_admin