# Generated by Django 3.2.5 on 2021-07-28 21:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_orderitem_date_add'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]