# Generated by Django 3.2 on 2023-04-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=12)),
                ('Message', models.TextField(max_length=150)),
            ],
        ),
    ]