# Generated by Django 3.2.24 on 2024-03-10 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_subject',
            field=models.CharField(choices=[('Shipping & Delivery', 'Shipping & Delivery'), ('Plants', 'Plants'), ('Other', 'Other')], max_length=30),
        ),
    ]