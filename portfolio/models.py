from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from PIL import Image

class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    short_description = models.CharField(max_length=400)
    description = RichTextField()
    clients = models.CharField(max_length=400)
    start_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio')


    class Meta:
        ordering = ['-start_date', ]

    def __unicode__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name



# our helper, add above the new model
def get_image_path(instance, filename):
    return '/'.join(['project_images', instance.project.slug, filename])

class Upload(models.Model):
    project = models.ForeignKey(Project, related_name="uploads")
    image = models.ImageField(upload_to=get_image_path)

    # add this bit in after our model
    def save(self, *args, **kwargs):
        # this is required when you override save functions
        super(Upload, self).save(*args, **kwargs)
        # our new code
        if self.image:
            image = Image.open(self.image)
            i_width, i_height = image.size
            max_size = (1240,700)

            if i_width > 1240:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)
            elif i_height > 700:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)
