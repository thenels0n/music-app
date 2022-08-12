# Generated by Django 3.2.8 on 2022-06-03 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.FileField(null=True, upload_to='media/')),
                ('song', models.FileField(upload_to='media')),
            ],
        ),
    ]