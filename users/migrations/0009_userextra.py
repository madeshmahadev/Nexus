# Generated by Django 3.0.8 on 2020-07-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('department', models.CharField(blank=True, max_length=15, null=True)),
                ('registrationnumber', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
