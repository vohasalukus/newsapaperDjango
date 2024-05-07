from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=255
    )
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['id']

    def __str__(self):
        return f'{self.title} - {self.created_at}'
