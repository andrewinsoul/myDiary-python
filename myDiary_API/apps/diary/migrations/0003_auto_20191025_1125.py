# Generated by Django 2.2.6 on 2019-10-25 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20190625_1552'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='diary',
            unique_together={('name', 'description')},
        ),
    ]
