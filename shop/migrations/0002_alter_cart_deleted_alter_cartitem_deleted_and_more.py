# Generated by Django 5.1.3 on 2025-01-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
