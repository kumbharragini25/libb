# Generated by Django 4.2.5 on 2023-09-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopperwithLabels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagesT')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('label', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]