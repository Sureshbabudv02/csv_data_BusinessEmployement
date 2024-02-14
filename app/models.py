from django.db import models

# Create your models here.
class BusinessEmployment(models.Model):
    series_reference=models.CharField(max_length=100)
    period=models.FloatField()
    data_value=models.CharField(max_length=100)
    suppressed=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    units=models.CharField(max_length=100)
    magnitude=models.IntegerField()
    subject=models.CharField(max_length=100)
    group=models.CharField(max_length=100)
    Series_title_1=models.CharField(max_length=100)
    Series_title_2=models.CharField(max_length=100)
    Series_title_3=models.CharField(max_length=100)

    def __str__(self):
        return self.data_value

