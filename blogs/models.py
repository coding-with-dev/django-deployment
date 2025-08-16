from django.db import models

class Blog(models.Model):
    title = models.TextField()
    description = models.TextField()
    image_url = models.ImageField(upload_to='blogs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title