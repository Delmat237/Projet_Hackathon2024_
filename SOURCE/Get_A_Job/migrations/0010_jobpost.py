# Generated by Django 5.0 on 2024-04-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Get_A_Job', '0009_joboffer_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('cv', models.FileField(upload_to='')),
            ],
        ),
    ]
