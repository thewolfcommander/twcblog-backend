from django.db import models
from django.conf import settings

class Profile(models.Model):
    """
    It is kind of a UserProfile
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    profile_picture = models.URLField(max_length=300, null=True, blank=True)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True, null=True)

    def __str__(self):
        return self.user.get_username()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField(null=True, blank=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    published = models.BooleanField(default=False)
    
    publish_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ["-publish_date"]