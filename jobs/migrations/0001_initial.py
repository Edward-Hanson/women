# Generated by Django 3.1.14 on 2023-08-31 19:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('certificate', models.FileField(upload_to='media', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('ghana_card', models.CharField(max_length=15)),
                ('confirm_job', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('telephone', models.PositiveIntegerField()),
                ('company', models.CharField(max_length=25)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
