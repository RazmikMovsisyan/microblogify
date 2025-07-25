from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=201)
    slug = models.SlugField(
        unique=True, blank=True, max_length=201
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='image_large-1172x570_rfmaxb'
    )

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        unique_slug = base_slug
        counter = 1

        if self.pk:
            old_post = Post.objects.get(pk=self.pk)
            if old_post.title != self.title:
                while Post.objects.filter(
                    slug=unique_slug
                ).exclude(pk=self.pk).exists():
                    unique_slug = f"{base_slug}-{counter}"
                    counter += 1
                self.slug = unique_slug
        elif not self.slug:
            while Post.objects.filter(
                slug=unique_slug
            ).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
