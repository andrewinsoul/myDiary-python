# Generated by Django 2.2.2 on 2019-06-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='entry_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='diary',
            name='description',
            field=models.CharField(default='default description text', max_length=500),
            preserve_default=False,
        ),
    ]