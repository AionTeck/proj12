from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Date of creation')
    update_at = models.DateTimeField(auto_now=True,
                                     verbose_name='Date of update')
    is_published = models.BooleanField(default=False)
