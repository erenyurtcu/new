from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(upload_to = "img/%y")
    date_post = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ('-date_post',)

    def __str__(self):
        return self.title
    

class SliderModel(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "img/%y")
    date_img = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-date_img',)

    def __str__(self):
        return self.title
    

class AtolyeModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(upload_to = "img/%y")
    date_ato = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-date_ato',)

    def __str__(self):
        return self.title