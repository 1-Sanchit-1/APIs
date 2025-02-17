# Generated by Django 5.0.6 on 2024-05-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropdata',
            name='result',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cropdata',
            name='humidity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cropdata',
            name='nitrogen',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cropdata',
            name='ph',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cropdata',
            name='phosphorus',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cropdata',
            name='potassium',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cropdata',
            name='rainfall',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cropdata',
            name='temperature',
            field=models.FloatField(default=0),
        ),
    ]
