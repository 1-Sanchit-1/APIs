# Generated by Django 5.0.6 on 2024-05-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_cropdata_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
