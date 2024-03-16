from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Wish(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор'
        )
    title = models.CharField('Название', blank=False, max_length=150)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    image = models.ImageField('Фото', upload_to='image/', blank=True)
    description = models.TextField('Описание', blank=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    gift = models.BooleanField(default=False)

    def __str__(self):
        return self.description[:20]

    def get_absolute_url(self):
        return reverse('wish', kwargs={'wish_slug': self.slug})
    
    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'
        ordering = ["-pub_date"]
    