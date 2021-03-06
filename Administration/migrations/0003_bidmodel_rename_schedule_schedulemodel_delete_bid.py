# Generated by Django 4.0.3 on 2022-03-25 11:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Administration', '0002_alter_bid_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='BidModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default='2022-03-25')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Schedule',
            new_name='ScheduleModel',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
    ]
