from django.db import models

# Create your models here.

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')  # Specify where the image will be uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Automatically add upload timestamp

    def __str__(self):
        return f"Image {self.id} uploaded on {self.uploaded_at}"