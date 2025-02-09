# Generated by Django 4.2.7 on 2023-11-21 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=20)),
                ('a_gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=1)),
                ('a_email', models.EmailField(max_length=254)),
                ('a_profilepic', models.ImageField(upload_to='photos')),
                ('a_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(choices=[('1', 'Fiction'), ('2', 'Mythology'), ('3', 'Horror'), ('4', 'study'), ('5', 'UPSC')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=20)),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=20)),
                ('state_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.state')),
            ],
        ),
        migrations.CreateModel(
            name='bookinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=20)),
                ('b_info', models.CharField(max_length=40)),
                ('b_price', models.FloatField()),
                ('b_desc', models.TextField()),
                ('b_pages', models.IntegerField()),
                ('b_image', models.ImageField(upload_to='photos')),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
