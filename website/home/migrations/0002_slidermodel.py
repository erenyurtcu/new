# Generated by Django 4.0.3 on 2023-12-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img/%y')),
                ('date_img', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_img',),
            },
        ),
    ]