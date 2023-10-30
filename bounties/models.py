from django.db import models

# Create your models here.
class Bounty_category(models.Model):
    category= models.CharField(max_length=150, default='')


    def __str__(self):
        return self.category


class Bounty(models.Model):
    bounty_title= models.CharField(max_length=150, default='')
    location= models.CharField(max_length=150, default='')
    category_choice= models.ForeignKey(Bounty_category, on_delete=models.CASCADE)
    despriction = models.TextField()
    overview = models.TextField()
    responsibilities =models.TextField()
    qualifications =models.TextField()
    inclosing = models.TextField()
    value = models.IntegerField()

    def __str__(self):
        return self.bounty_title
    
class Fund(models.Model):
    fund_title = models.CharField(max_length=150, default='')
    bounty = models.ForeignKey(Bounty, on_delete=models.CASCADE)
    intro = models.TextField()
    overview = models.TextField()
    why_support= models.TextField()
    how_to_help = models.TextField()
    qr_code = models.ImageField(upload_to='donate_qr/')

    def __str__(self):
        return self.fund_title

class ApplicationForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='uploads/resumes/')
    cover_letter = models.FileField(upload_to='uploads/cover_letters/')
    portfolio = models.FileField(upload_to='uploads/portfolios/', blank=True, null=True)


class Apply(models.Model):
    apply_title = models.CharField(max_length=150, default='')
    bounty = models.ForeignKey(Bounty, on_delete=models.CASCADE)
    intro = models.TextField()
    why_contribute = models.TextField()
    #application form
    
    class Meta:
        verbose_name_plural = "Applications"