# Generated by Django 3.0.8 on 2020-09-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call_app', '0006_auto_20200921_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='in_crm',
            field=models.CharField(default='пока нет данных атс', max_length=25, verbose_name=' Добавлено в CRM'),
        ),
    ]