# Generated by Django 4.0.10 on 2023-07-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='category',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sizes',
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('electronics', 'electronics'), ('jewelery', 'jewelery'), ("men's clothing", "men's clothing"), ("women's clothing", "women's clothing")], default="women's clothing", max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='https://images.unsplash.com/photo-1461988320302-91bde64fc8e4?ixid=2yJhcHBfaWQiOjEyMDd9', upload_to=''),
        ),
    ]
