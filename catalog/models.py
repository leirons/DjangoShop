from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from .exceptions.goods_exception import CantGetImage


class Category(models.Model):
    name: models.CharField = models.CharField(_("Name"), max_length=25)
    product: models.ForeignKey = models.ForeignKey("Product", on_delete=models.CASCADE)
    slug: models.SlugField = models.SlugField(_(u"Slug"), unique=True)

    meta_title: models.CharField = models.CharField(_("Meta title"), max_length=50)
    meta_keywords: models.TextField = models.TextField(_("Meta keywords"), blank=True)
    meta_description: models.TextField = models.TextField(_("Meta description"), blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        """
        Returns the absolute_url.
        """
        return reverse("category", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):
    name: models.CharField = models.CharField(max_length=25)
    item: models.ForeignKey = models.ForeignKey("Item", on_delete=models.CASCADE)
    image: models.ImageField = models.ImageField(upload_to="product__image")

    meta_title: models.CharField = models.CharField(max_length=50)
    meta_keywords: models.TextField = models.TextField(blank=True)
    meta_description: models.TextField = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_image(self):
        """
        Return Image if true else exception CantGetImage
        """
        if self.image:
            return self.image
        return CantGetImage.CantGetImage


class Item(models.Model):
    __choices = {'1': 'S',
                 '2': "M",
                 '3': "L"
                 }
    name: models.CharField = models.CharField(max_length=25)
    price: models.IntegerField = models.IntegerField(default=0)
    color:models.CharField = models.CharField(max_length=25)
    quantity: models.IntegerField = models.IntegerField(default=0)
    available_size: models.CharField = models.CharField(choices=__choices)
    description: models.TextField = models.TextField(max_length=500)
    characterization: models.TextField = models.TextField(max_length=20)
    photos: models.ImageField = models.ImageField(upload_to="items")
    popularity:models.IntegerField = models.IntegerField(default=0)

    def get_all_items(self):
        items = self.objects.all()
        return items


