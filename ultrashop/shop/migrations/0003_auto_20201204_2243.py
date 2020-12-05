# Generated by Django 3.1.2 on 2020-12-04 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201201_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productinfo', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Данные о товаре'),
        ),
    ]
