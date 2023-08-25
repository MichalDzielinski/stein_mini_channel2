from django.db import models
from django.template.defaultfilters import slugify

class Room(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug =  slugify(self.name)
    #         super(Room, self).save(*args, **kwargs)




