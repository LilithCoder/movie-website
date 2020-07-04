from django.db import models

# Create your models here.
class Movie(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    writers = models.CharField(max_length=50)
    stars = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.IntegerField()
    tags = models.CharField(max_length=50)
    comments = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['num_stars']
    
    def __str__(self):
        return self.title
    