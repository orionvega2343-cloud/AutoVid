from django.db import models


class CarModel(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Марка")
    name = models.CharField(max_length=100, verbose_name="Название модели")
    generation = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Поколение или годы выпуска"
    )

    class Meta:
        ordering = ['brand', 'name']
        verbose_name = "Модель автомобиля"
        verbose_name_plural = "Модели автомобилей"

    def __str__(self):
        return f"{self.brand} {self.name} ({self.generation})"


class Brand(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название бренда"
    )
    country = models.CharField(max_length=50, blank=True, verbose_name="Страна")

    class Meta:
        ordering = ['name']
        verbose_name = "Бренд запчастей"
        verbose_name_plural = "Бренды запчастей"

    def __str__(self):
        return self.name


class Part(models.Model):
    sku = models.CharField(max_length=50, unique=True, verbose_name="Артикул/OEM")
    name = models.CharField(
        max_length=255,
        verbose_name="Название детали"
    )
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='parts', verbose_name="Бренд")
    applicable_cars = models.ManyToManyField(CarModel, related_name='parts', verbose_name="Применимые модели автомобилей")
    category = models.CharField(
        max_length=30,
        choices=[
            ('suspension', 'Подвеска'),
            ('brakes', 'Тормозная система'),
            ('engine', 'Двигатель'),
            ('filters', 'Фильтры'),
            ('belts', 'Ремни и шкивы'),
            ('rubber', 'Резинотехника'),
            ('other', 'Прочее')
        ],
        verbose_name="Категория"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )
    price_old = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Старая цена"
    )
    in_stock = models.IntegerField(default=0, verbose_name="Наличие на складе")
    weight_kg = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        null=True,
        blank=True,
        verbose_name="Вес (кг)"
    )
    hs_code = models.CharField(max_length=20, blank=True, verbose_name="HS код")
    image = models.ImageField(upload_to='parts/', null=True, blank=True, verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Активность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['sku']
        verbose_name = "Запчасть"
        verbose_name_plural = "Запчасти"

    def __str__(self):
        return f"[{self.sku}] {self.brand.name} - {self.name}"


class Order(models.Model):
    part = models.ForeignKey(
        Part,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name="Запчасть"
    )
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    client_phone = models.CharField(max_length=20, verbose_name="Телефон клиента")
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'Новый'),
            ('processing', 'В обработке'),
            ('done', 'Выполнен')
        ],
        default='new',
        verbose_name="Статус заказа"
    )
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления заказа")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.id} — {self.client_name} ({self.part.name})"