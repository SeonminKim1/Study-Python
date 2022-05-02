from django.db import models

# DB 생성용
class Feed(models.Model):
    user_id = models.TextField()
    nickname = models.TextField(null=True)
    profile_image = models.TextField()
    content = models.TextField()
    image = models.TextField()
    is_marked = models.BooleanField(null=True)
    like_count = models.TextField()

class Reply(models.Model):
    nickname = models.TextField()
    content = models.TextField()