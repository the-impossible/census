#My Django import
from django.db import models

# My app imports


# Create your models here.        
class LGA(models.Model):
    lga = models.CharField(max_length=30)
    population = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.lga}'
    
    class Meta:
        db_table = 'Lga'
        verbose_name_plural = 'Lgas'