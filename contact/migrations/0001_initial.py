# Generated by Django 3.2.24 on 2024-03-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=60)),
                ('contact_date', models.DateField(auto_now_add=True, null=True)),
                ('contact_subject', models.CharField(choices=[('Other', 'Other'), ('Shipping & Delivery', 'Shipping & Delivery'), ('Plants', 'Plants')], max_length=30)),
                ('contact_message', models.TextField(max_length=500)),
            ],
        ),
    ]
