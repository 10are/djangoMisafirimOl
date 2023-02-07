# Generated by Django 4.1.6 on 2023-02-07 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogModel',
        ),
        migrations.AddField(
            model_name='blog',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.city'),
        ),
    ]