from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    # body2 = models.TextField()
    # body3 = models.TextField()
    # quote = models.TextField()
    # body4 = models.TextField()
    # body5 = models.TextField()
    # feature_image = 
    # post_image
    # post_image2
    created_at = models.DateTimeField(auto_now_add=True)
     # updated_at = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])


class Comment(models.Model):
    blog = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name='comments',
        )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('blog')