# Generated by Django 3.2.6 on 2021-08-28 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Paper', '0002_rename_papers_my_papers'),
        ('Account', '0001_initial'),
        ('Comment', '0002_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True, null=True, verbose_name='Date')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_comment', to='Paper.my_papers')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to='Account.user')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]