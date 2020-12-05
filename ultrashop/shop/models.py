from django.db import models
from registration.models import User
from django.utils.text import slugify


STATE_CHOICES = (
    ('basket', 'Статус корзины'),
    ('new', 'Новый'),
    ('confirmed', 'Подтвержден'),
    ('assembled', 'Собран'),
    ('sent', 'Отправлен'),
    ('delivered', 'Доставлен'),
    ('canceled', 'Отменен'),
)


class Shop(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True,)
    file = models.FileField(blank=True, upload_to=None, max_length=100)
    shop_manager = models.ForeignKey(User, null=False, blank=False,
                                     verbose_name="Администратор магазина",
                                     on_delete=models.CASCADE)
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"
        ordering = ('-name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Shop, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("Shop_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True,)
    shops = models.ManyToManyField(Shop, verbose_name="Магазины",
                                   related_name='categories', blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('-name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 related_name='products', blank=True,
                                 on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True,)
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ('-name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    # def get_absolute_url(self):
    #     return reverse("Product_detail", kwargs={"pk": self.pk})


class Productinfo(models.Model):
    name = models.CharField(max_length=50,  verbose_name='Данные о товаре',
                            blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт',
                                blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    price_rrc = models.PositiveIntegerField(verbose_name='Рекомендуемая розничная стоимость')

    class Meta:
        verbose_name = "Productinfo"
        verbose_name_plural = "Productinfos"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Productinfo_detail", kwargs={"pk": self.pk})


class Parameter(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = "Parameter"
        verbose_name_plural = "Parameters"
        ordering = ('-name',)

    def __str__(self):
        return self.name

#     # def get_absolute_url(self):
#     #     return reverse("Parameter_detail", kwargs={"pk": self.pk})


class ProductParameter(models.Model):
    product_info = models.ForeignKey(Productinfo, verbose_name="Данные о параметре продукта",
                                     on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, verbose_name="Параметр",
                                  on_delete=models.CASCADE)
    value = models.CharField(verbose_name='Значение', max_length=100)

    class Meta:
        verbose_name = "ProductParameter"
        verbose_name_plural = "ProductParameters"

    def __str__(self):
        return self.parameter


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="orders", blank=True,
                             verbose_name='Пользователь')
    dt = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    state = models.CharField(verbose_name='Статус', choices=STATE_CHOICES,
                             max_length=15)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ('-dt',)

    def __str__(self):
        return "{} статус {}".format(self.user, self.state)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='Заказ')
    product = models.ForeignKey(Productinfo, on_delete=models.CASCADE,
                                verbose_name='Продукт')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,
                             verbose_name='Магазин')
    quantity = models.PositiveIntegerField(verbose_name='Колличество')

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"

    def __str__(self):
        return "{}".format(self.order)



class Contact(models.Model):
    city = models.CharField(max_length=30, verbose_name='Город')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             related_name='contacts', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.user
