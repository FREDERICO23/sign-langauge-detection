from django.db import models
import os

def upload_path(instance, filename):
    """Generates upload path for sign language images"""
    return os.path.join('uploads', filename)

class SignImage(models.Model):
    """Model for storing sign language images"""
    image = models.ImageField(upload_to=upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Sign Image {self.id}"
