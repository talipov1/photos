from django.db import models
from datetime import date

class Categories(models.Model):
    '''категории'''
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    '''Актеры'''
    name = models.CharField("Имя", max_length=150)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"


class Genre(models.Model):
    '''жанры'''
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Photo(models.Model):
    '''фоточки'''
    name = models.CharField("Название", max_length=150)
    slogan = models.CharField("Слоган", max_length=150, default='')
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="фото/")
    year = models.DateTimeField("Дата", null=True)
    location = models.CharField("Местоположение", max_length=150)
    operator = models.ManyToManyField(Actor, verbose_name="Оператор", related_name="photo_operator", blank=True)
    actor = models.ManyToManyField(Actor, verbose_name="Актер", related_name="photo_actor", blank=True)
    genre = models.ManyToManyField(Genre,verbose_name="Жанры", blank=True)
    categories = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(unique=True, max_length=160)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Rating(models.Model):
    '''рейтинг'''
    ip = models.CharField("IP адрес", max_length=150)
    rating = models.PositiveSmallIntegerField("Рейтинг", default=0)
    actor = models.ForeignKey(Actor, verbose_name="Актер", on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, verbose_name="Фото", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинг"


class Review(models.Model):
    '''отзывы'''
    email = models.EmailField()
    name = models.CharField("Отзыв", max_length=30)
    text = models.TextField("Текст", max_length=150)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank = True, null = True)
    photo = models.ForeignKey(Photo, verbose_name="Фото", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

