# Generated by Django 4.0.10 on 2023-07-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_category_colors_remove_category_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='https://images.unsplash.com/random/?girlshirt', upload_to=''),
        ),
    ]
