from django.db import models

NULLABLE = {"blank": True, "null": True}


class NetworkNode(models.Model):
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )
    # Название
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(max_length=100, unique=True)
    country = models.FloatField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень иерархии')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Долг поставщику')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Узел сети'
        verbose_name_plural = 'Узлы сети'


class Product(models.Model):
    node = models.ForeignKey(NetworkNode, related_name='products', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, verbose_name='Название продукта')
    product_model = models.CharField(max_length=100, verbose_name='Модель продукта')
    product_release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
