from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Plant.Status.PUBLISHED)


class Plant(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Контент")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=Status.PUBLISHED,
                                       choices=tuple([(bool(i[0]), i[1]) for i in Status.choices]))
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name='Тег')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Растения'
        verbose_name_plural = 'Растения'
        ordering = ('-content',)

        indexes = [
            models.Index(fields=['-time_created'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, verbose_name='Тег')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})
