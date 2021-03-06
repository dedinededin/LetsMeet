# Generated by Django 2.1.4 on 2018-12-15 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_profile_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='main.Profile')),
                ('to_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='main.Profile')),
            ],
        ),
    ]
