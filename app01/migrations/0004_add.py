# Generated by Django 3.2.9 on 2022-03-14 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_contact_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]