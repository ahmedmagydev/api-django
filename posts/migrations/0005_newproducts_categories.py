# Generated by Django 4.1.7 on 2023-03-04 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('posts', '0004_rename_productss_newproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='newproducts',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_posts', to='categories.category'),
        ),
    ]
