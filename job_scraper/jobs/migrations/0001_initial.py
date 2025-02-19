# Generated by Django 5.1.4 on 2025-02-16 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('job_url', models.URLField()),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
