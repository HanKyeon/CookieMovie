# Generated by Django 3.2.13 on 2022-11-23 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(default='제목 없는 컬렉션', max_length=200),
        ),
    ]