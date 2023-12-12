# Generated by Django 4.0.3 on 2023-10-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='img/%y')),
                ('date_post', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_post',),
            },
        ),
    ]