# Generated by Django 2.1.3 on 2018-11-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoteFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('party', models.CharField(blank=True, max_length=200)),
                ('votedon', models.DateTimeField(auto_now_add=True, null=True)),
                ('pages', models.IntegerField()),
            ],
        ),
    ]
