# Generated by Django 3.2.3 on 2021-06-14 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0005_delete_result'),
        ('konto', '0003_alter_result_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacja.test'),
        ),
    ]