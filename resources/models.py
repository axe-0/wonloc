from django.db import models

# Create your models here.

class ResourceCategory(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category

class LibraryItem(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='library/files/')
    category= models.ForeignKey(ResourceCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='library/thumbs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
