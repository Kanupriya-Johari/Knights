from django.db import models
class FileUpload(models.Model):
    #title = models.CharField(max_length = 80)
    # filename = models.CharField(max_length=128)
    FileName = models.CharField(max_length=200)
    UploadFile = models.FileField(upload_to='media')
    def __str__(self):
        return self.FileName
    # def save(self, force_insert=False, force_update=False):
    #     super(FileUpload, self).save(force_insert, force_update)
    
# class Profile(models.Model):
#    name = models.CharField(max_length = 50)
#    size = models.CharField(max_length = 10)
   
# from uuid import uuid4
# import os
# def get_random_filename(instance, filename):
#     instance.filename = filename
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (str(uuid4()), ext)
#     return os.path.join('some/path/', filename)

# # inside the model
# class FooModel(models.Model):
#     filename = models.CharField(max_length=128)
#     file = models.FileField(upload_to=get_random_filename) 