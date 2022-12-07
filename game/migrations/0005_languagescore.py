# Generated by Django 4.1.3 on 2022-12-07 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0004_league_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveBigIntegerField(default=0)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.league')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
