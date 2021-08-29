# Generated by Django 3.2.6 on 2021-08-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('subject', models.CharField(blank=True, max_length=30, null=True, verbose_name='Subject')),
                ('message', models.TextField(blank=True, max_length=300, null=True, verbose_name='Mesmessage')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
