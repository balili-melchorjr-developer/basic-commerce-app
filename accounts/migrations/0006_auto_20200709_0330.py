# Generated by Django 3.0.8 on 2020-07-09 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200709_0248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catergory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
