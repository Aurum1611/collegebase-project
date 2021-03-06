# Generated by Django 3.2.13 on 2022-05-16 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('phone_num', models.CharField(max_length=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.city')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.city')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.college')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.state'),
        ),
    ]
