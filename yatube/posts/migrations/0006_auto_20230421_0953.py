# Generated by Django 2.2.16 on 2023-04-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_follow'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_follow'),
        ),
    ]
