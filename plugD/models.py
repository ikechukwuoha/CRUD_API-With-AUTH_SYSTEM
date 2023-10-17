from django.db import models
from users.models import User
import uuid




class Project(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=500)
    file_number = models.CharField(max_length=600)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='update_user')
    updated_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user')
    created_on = models.DateTimeField(auto_now_add=True)
    recieved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_user')



    def __str__(self):
        return self.project_name



