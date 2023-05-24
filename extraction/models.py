from django.db import models

class UploadedApp(models.Model):
    zip_file = models.FileField(upload_to='uploaded_apps/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.zip_file.name.split('.')[0]
        

        # return self.zip_file.name.split("apps/")[1].split("_")[0]
        

    @property
    def slug(self):
        return self.zip_file.name.split('.')[0]
