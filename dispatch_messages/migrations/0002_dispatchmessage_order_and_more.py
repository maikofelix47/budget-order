# Generated by Django 4.1.7 on 2023-04-13 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0001_initial'),
        ('orders', '0009_alter_orderdetails_rider'),
        ('dispatch_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatchmessage',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dispatchmessage',
            name='recepient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riders.rider'),
        ),
    ]