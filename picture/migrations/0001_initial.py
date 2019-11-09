# Generated by Django 2.2.7 on 2019-11-09 19:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=400)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('sold', 'sold'), ('for sale', 'for sale')], default='for sale', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commented', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picture.Artwork')),
            ],
        ),
    ]