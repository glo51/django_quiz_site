# Generated by Django 3.2.3 on 2021-06-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0006_alter_test_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='pub_date',
            field=models.DateField(auto_now=True, verbose_name='published'),
        ),
    ]
