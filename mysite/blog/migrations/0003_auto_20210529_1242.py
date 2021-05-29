# Generated by Django 3.2.3 on 2021-05-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210524_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='city',
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.ManyToManyField(related_name='companies', to='blog.City'),
        ),
    ]
