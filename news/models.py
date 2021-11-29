from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='news title')
    content = models.TextField(blank=True, verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated date')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='active')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='category')
    tags = models.ManyToManyField('Tag', blank=True, related_name='news', verbose_name='tags')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ['-created_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='category name')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
