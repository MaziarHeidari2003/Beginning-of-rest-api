# Generated by Django 5.0 on 2024-05-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='advocate',
            name='bio',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
