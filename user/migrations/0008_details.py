# Generated by Django 2.2 on 2020-08-12 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('state', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('postcode', models.CharField(max_length=6)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Cart')),
            ],
        ),
    ]