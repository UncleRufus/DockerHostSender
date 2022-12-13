# Imports
from django.urls import reverse
from django.db import models


class RequestModel(models.Model):
    """Модель запроса"""

    cmd = models.CharField('Данные', max_length=255)
    exit_code = models.CharField('Код', max_length=255)

    request_date = models.DateTimeField('Дата запроса', auto_now=True)

    def get_absolute_url(self):
        """Return absolute url for request model"""

        return reverse('local_request_detail_page', args=[int(self.id)])

    def __str__(self):
        """Overrides __str__ method"""

        return f'{str(self.request_date)} | {str(self.code)}'

    class Meta:
        verbose_name: str = 'Запрос'
        verbose_name_plural: str = 'Запросы'
