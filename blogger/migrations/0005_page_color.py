# Generated by Django 2.1.7 on 2019-05-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0004_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='color',
            field=models.CharField(max_length=20),
        ),
    ]
