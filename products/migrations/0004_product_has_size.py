# Generated by Django 3.2.24 on 2024-02-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_content_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_size',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
