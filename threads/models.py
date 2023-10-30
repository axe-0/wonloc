from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Guild(models.Model):
    guild = models.CharField(max_length =150, default ='')

    def __str__(self):
        return self.guild

class Type (models.Model):
    title = models.CharField(max_length =150, default ='')

    def __str__(self):
        return self.title

class Category (models.Model):
    category =models.CharField(max_length =150, default ='')

    def __str__(self):
        return self.category


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    guild  = models.ForeignKey(Guild, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Type,on_delete= models.CASCADE)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)

    # Like counter for posts
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)


    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    

    def __str__(self):
        return f"Comment by {self.user.first_name} on {self.post.title}"
    
    def total_likes(self):
        return self.likes.count()



