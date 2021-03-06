# Generated by Django 2.2.3 on 2019-09-04 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_publisher_addr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('book', models.ManyToManyField(to='library.Book')),
            ],
        ),
    ]
