# Generated by Django 4.2 on 2023-04-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iMagazine', '0003_alter_productcard_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcard',
            name='image',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]
