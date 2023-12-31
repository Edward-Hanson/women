# Generated by Django 3.1.14 on 2023-08-31 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=25, null=True)),
                ('occupation', models.CharField(max_length=25)),
                ('institution', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='media')),
                ('telephone', models.PositiveIntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('details', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
