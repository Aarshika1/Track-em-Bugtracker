from django.db import models
from projects_app.models import Project
from django.contrib.auth.models import User


class Bug(models.Model):

    PRIORITY_CHOICES = [
        ('LO','Low'),
        ('MD','Medium'),
        ('HI','High')
    ]
    STATE_CHOICES = [
        ('RE','Resolved'),
        ('UN', 'Unresolved')
    ]

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, default='0')
    name = models.CharField(max_length=50)
    desc = models.TextField()
    comments = models.TextField()
    priority = models.CharField(max_length=2, choices = PRIORITY_CHOICES)
    state = models.CharField(max_length=2, choices = STATE_CHOICES)
    assigned_user = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'