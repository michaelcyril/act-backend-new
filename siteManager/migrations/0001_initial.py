# Generated by Django 3.2.18 on 2023-02-18 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'new',
            },
        ),
        migrations.CreateModel(
            name='NewFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.BinaryField()),
                ('new_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteManager.new')),
            ],
            options={
                'db_table': 'new_file',
            },
        ),
        migrations.CreateModel(
            name='EventFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.BinaryField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteManager.event')),
            ],
            options={
                'db_table': 'event_file',
            },
        ),
    ]
