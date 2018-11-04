from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Image(models.Model):
    image_name = models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    photo = models.ImageField(upload_to = 'articles/')

    def __str__(self):
        return self.image_name

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images