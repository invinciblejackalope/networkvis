# Generated by Django 2.1.7 on 2019-11-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0012_auto_20191121_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='desc_color',
            field=models.CharField(default='#444444', max_length=20),
        ),
    ]
