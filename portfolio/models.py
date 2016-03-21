from __future__ import unicode_literals
from django.contrib.auth.models import User
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
    category = models.ManyToManyField('Category')
    tag = models.ManyToManyField('Tag')
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


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    def get_projects(self):
        return Project.objects.filter(category=self)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name

#basic blog Model
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,related_name='blog_posts')
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    image = models.ImageField(upload_to='blog')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
