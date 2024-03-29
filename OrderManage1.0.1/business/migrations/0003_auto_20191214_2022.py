# Generated by Django 2.2.7 on 2019-12-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_cuisine_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='custom_num',
            field=models.IntegerField(default=0, verbose_name='用餐人数'),
        ),
        migrations.AlterField(
            model_name='desk',
            name='desk_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='桌号'),
        ),
    ]
