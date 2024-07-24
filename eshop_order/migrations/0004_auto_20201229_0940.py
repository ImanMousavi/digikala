# Generated by Django 3.1 on 2020-12-29 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop_variant', '0002_variants_status'),
        ('eshop_product', '0003_auto_20201229_0922'),
        ('eshop_order', '0003_auto_20201228_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop_product.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop_variant.variants', verbose_name='مدل محصول'),
        ),
    ]
