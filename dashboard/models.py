from django.db import models

# Create your models here.

    
class Guild_status(models.Model):
    
    status= models.CharField(max_length=150, default="select")

    def __str__(self):
        return self.status
 




class Thumbnail(models.Model):
    thumbnail_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, )
    guild_text = models.CharField(max_length=150, default="MAKERS GUILD")
    #Guild category choice dropdown
    category_text = models.CharField(max_length=150, default='')

    #GUILD status choice 
    status = models.ForeignKey(Guild_status, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='thumbnails/')


