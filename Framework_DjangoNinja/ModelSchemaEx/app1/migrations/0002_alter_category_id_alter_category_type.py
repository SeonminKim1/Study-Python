# Generated by Django 4.1.6 on 2023-02-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(default='개발', max_length=20),
        ),
    ]