# Generated by Django 4.0 on 2021-12-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kitchenLocation', models.CharField(max_length=100)),
                ('amountInStorage', models.IntegerField(blank=True)),
            ],
        ),
    ]
