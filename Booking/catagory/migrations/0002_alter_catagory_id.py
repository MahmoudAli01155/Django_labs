# Generated by Django 4.1.6 on 2023-02-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
    ]
