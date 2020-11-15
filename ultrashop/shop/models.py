from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Shop(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    file = models.FileField(upload_to=None, max_length=100)

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Shop_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50)
    shops = models.ManyToManyField(Shop, verbose_name="Магазины")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Product_detail", kwargs={"pk": self.pk})


class Productinfo(models.Model):
    name = models.CharField(max_length=50)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    price_rrc = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Productinfo"
        verbose_name_plural = "Productinfos"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Productinfo_detail", kwargs={"pk": self.pk})


class Parameter(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Parameter"
        verbose_name_plural = "Parameters"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Parameter_detail", kwargs={"pk": self.pk})


class ProductParameter(models.Model):
    product_info = models.ForeignKey(Productinfo, verbose_name="", on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, verbose_name="", on_delete=models.CASCADE)
    value = models.BooleanField()

    class Meta:
        verbose_name = "ProductParameter"
        verbose_name_plural = "ProductParameters"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("ProductParameter_detail", kwargs={"pk": self.pk})


class Order(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="users")
    dt = models.DateField(auto_now=False, auto_now_add=False)
    status =models.BooleanField()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Order_detail", kwargs={"pk": self.pk})


class OrderItem(models.Model):
    order =  models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("OrderItem_detail", kwargs={"pk": self.pk})


# class Contact(models.Model):
#     # type = 
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     value = models.BooleanField()
