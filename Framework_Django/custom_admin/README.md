### User Table by Admin
- Custom User Table by Admin

### Structure
```
├── users  // app
│   ├── admin.py
│   ├── models.py
│   └── ...
├── custom_admin // project
│   ├── urls.py       
│   ├── settings.py    
│   └── ...
└── ... 
``` 

### Key code
```
# admin.py
admin.site.register(UserModel)

# models.py
from django.contrib.auth.models import AbstractUser
class UserModel(AbstractUser):
  ...
```
