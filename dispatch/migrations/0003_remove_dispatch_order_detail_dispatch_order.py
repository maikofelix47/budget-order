# Generated by Django 4.1.7 on 2023-04-13 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_orderdetails_rider'),
        ('dispatch', '0002_remove_dispatch_rider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispatch',
            name='order_detail',
        ),
        migrations.AddField(
            model_name='dispatch',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
            preserve_default=False,
        ),
    ]
