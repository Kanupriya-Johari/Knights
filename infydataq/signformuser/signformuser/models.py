from django.db import models
class FileUpload(models.Model):
    
    #title = models.CharField(max_length = 80)
    file = models.FileField(upload_to='media')
    
    
    