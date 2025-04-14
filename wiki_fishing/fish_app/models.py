import os

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

class Fish(models.Model):
    """Модель для хранения информации о видах рыбы"""
    FISH_TYPE_CHOICES = [
        ('predator', 'Хищник'),
        ('peaceful', 'Мирная'),
        ('omnivore', 'Всеядная'),
    ]

    WATER_TYPE_CHOICES = [
        ('fresh', 'Пресная'),
        ('salt', 'Солёная'),
        ('brackish', 'Солоноватая'),
    ]

    SEASON_ACTIVITY_CHOICES = [
        ('winter', 'Зима'),
        ('spring', 'Весна'),
        ('summer', 'Лето'),
        ('autumn', 'Осень'),
        ('all_season', 'Круглый год'),
    ]

    BEST_CATCH_TIME_CHOICES = [
        ('morning', 'Утро'),
        ('afternoon', 'День'),
        ('evening', 'Вечер'),
        ('night', 'Ночь'),
        ('all_day', 'Круглые сутки'),
    ]

    # Основная информация
    name = models.CharField(max_length=50, verbose_name="Название рыбы")
    scientific_name = models.CharField(max_length=100, verbose_name="Научное название", blank=True)
    type = models.CharField(
        max_length=10,
        choices=FISH_TYPE_CHOICES,
        verbose_name="Тип питания"
    )
    description = models.TextField(verbose_name="Описание", blank=True)

    image = models.ImageField(
        upload_to='fish/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )

    # Ареал и среда обитания
    habitat = models.CharField(
        max_length=20,
        choices=WATER_TYPE_CHOICES,
        verbose_name="Тип воды",
        default='fresh',
        blank=True
    )
    area = models.CharField(max_length=100, verbose_name="Ареал обитания", blank=True)

    # Активность и поведение
    season_activity = models.CharField(
        max_length=10,
        choices=SEASON_ACTIVITY_CHOICES,
        verbose_name="Сезон активности",
        blank=True
    )
    best_catch_time = models.CharField(
        max_length=100,
        verbose_name="Лучшее время для ловли",
        choices=BEST_CATCH_TIME_CHOICES,
        help_text="Например: утро, день, вечер, ночь",
        blank=True
    )
    optimal_temperature = models.IntegerField(
        verbose_name="Оптимальная температура воды (°C)",
        null=True,
        blank=True
    )
    temperature_range = models.CharField(
        max_length=50,
        verbose_name="Диапазон температур активности (°C)",
        help_text="Например: 15-22",
        blank=True
    )
    is_red_book = models.BooleanField(verbose_name="В Красной книге", default=False)

    # Физические характеристики
    avg_weight = models.FloatField(verbose_name="Средний вес (кг)", null=True, blank=True)
    max_weight = models.FloatField(verbose_name="Максимальный вес (кг)", null=True, blank=True)
    avg_length = models.FloatField(verbose_name="Средняя длина (см)", null=True, blank=True)

    class Meta:
        verbose_name = "Рыба"
        verbose_name_plural = "Рыбы"
        ordering = ['name']  # Сортировка по названию по умолчанию

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    def save(self, *args, **kwargs):
        if self.image and not self.image.name.startswith('fish/'):
            self.image.name = f'fish/{os.path.basename(self.image.name)}'
        super().save(*args, **kwargs)

    def get_fishing_period(self):
        """Возвращает информацию о лучшем периоде ловли"""
        period = []
        if self.season_activity != 'all_season':
            period.append(f"Сезон: {self.get_season_activity_display()}")
        if self.best_catch_time:
            period.append(f"Время: {self.get_best_catch_time_display()}")
        if self.temperature_range:
            period.append(f"Температура: {self.temperature_range}°C")
        return ", ".join(period) if period else "Нет данных"

    def get_size_info(self):
        """Возвращает информацию о размерах рыбы"""
        info = []
        if self.avg_weight:
            info.append(f"Ø вес: {self.avg_weight} кг")
        if self.max_weight:
            info.append(f"Макс. вес: {self.max_weight} кг")
        if self.avg_length:
            info.append(f"Ø длина: {self.avg_length} см")
        return ", ".join(info) if info else "Нет данных"

    def get_habitat_info(self):
        """Возвращает информацию о среде обитания"""
        info = [self.get_habitat_display()]
        if self.area:
            info.append(self.area)
        return " - ".join(info)


class Bait(models.Model):
    """Модель для хранения информации о наживках и прикормках"""
    BAIT_TYPE_CHOICES = [
        ('bait', 'Наживка'),
        ('feed', 'Прикормка'),
        ('lure', 'Искусственная приманка'),
    ]

    PRICE_CATEGORY_CHOICES = [
        ('low', 'Низкая'),
        ('medium', 'Средняя'),
        ('high', 'Высокая'),
    ]

    TARGET_FISH_CHOICES = [
        ('universal', 'Универсальная'),
        ('predator', 'Для хищников'),
        ('peaceful', 'Для мирных рыб'),
    ]

    # Основная информация
    name = models.CharField(max_length=50, verbose_name="Название")
    type = models.CharField(
        max_length=10,
        choices=BAIT_TYPE_CHOICES,
        verbose_name="Тип приманки",
    )
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to='baits/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )

    target_fish = models.CharField(
        max_length=10,
        choices=TARGET_FISH_CHOICES,
        verbose_name="Целевая рыба",
        default='universal',
    )

    # Категория цены вместо конкретной стоимости
    price_category = models.CharField(
        max_length=10,
        choices=PRICE_CATEGORY_CHOICES,
        verbose_name="Категория цены",
        default='medium',
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name="Рейтинг (1-5)",
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def save(self, *args, **kwargs):
        if self.image and not self.image.name.startswith('baits/'):
            self.image.name = f'baits/{os.path.basename(self.image.name)}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Приманка"
        verbose_name_plural = "Приманки"
        ordering = ['type', 'name']

    def __str__(self):
        return f"{self.get_type_display()}: {self.name}"

    def get_price_info(self):
        """Возвращает информацию о ценовой категории"""
        return self.get_price_category_display()


class FishBaitRelation(models.Model):
    """Минималистичная модель связи рыбы и приманки"""
    fish = models.ForeignKey(
        Fish,
        on_delete=models.CASCADE,
        related_name='baits'  # Это важно!
    )

    bait = models.ForeignKey(
        'Bait',
        on_delete=models.CASCADE,
        verbose_name="Приманка"
    )

    efficiency = models.PositiveSmallIntegerField(
        verbose_name="Эффективность (1-5)",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Оценка от 1 (минимальная) до 5 (максимальная)"
    )

    notes = models.TextField(
        verbose_name="Заметки",
        blank=True,
        help_text="Дополнительные советы"
    )

    class Meta:
        verbose_name = "Связь рыба-приманка"
        verbose_name_plural = "Связи рыба-приманка"
        unique_together = ('fish', 'bait')
        ordering = ['-efficiency']

    def __str__(self):
        return f"{self.fish.name} + {self.bait.name}: {self.efficiency}/5"