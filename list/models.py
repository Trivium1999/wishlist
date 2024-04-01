from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Wish(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор'
        )
    title = models.CharField('Название', blank=False, max_length=150)
    image = models.ImageField('Фото', upload_to='image/', blank=True)
    description = models.TextField('Описание', blank=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    gift = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'
        ordering = ["-pub_date"]
    