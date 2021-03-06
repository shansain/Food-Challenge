# Generated by Django 3.0.3 on 2020-02-25 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200225_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInChallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userChallenge', to='core.Challenge')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userChallenge', to='core.Client')),
            ],
        ),
    ]
