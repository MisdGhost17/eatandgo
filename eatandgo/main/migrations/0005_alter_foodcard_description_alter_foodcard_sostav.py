# Generated by Django 5.1 on 2024-09-01 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_foodcategory_options_foodcard_sostav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcard',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='foodcard',
            name='sostav',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]
