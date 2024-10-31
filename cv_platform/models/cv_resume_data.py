from django.db import models
from django.contrib.auth.models import User



class Resume(models.Model):
    title = models.CharField(max_length=100,default='Nome Padrão')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.user.username}'