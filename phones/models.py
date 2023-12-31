from django.db import models
class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=120)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)

    # def __str__(self):
    #     return [self.id, self.name, self.price, self.release_date.isoformat(), self.image]