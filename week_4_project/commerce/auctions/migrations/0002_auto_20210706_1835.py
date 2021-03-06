# Generated by Django 3.2 on 2021-07-06 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('Electronics', 'Electronics'), ('Food', 'Food'), ('Home', 'Home'), ('Other', 'Other'), ('Pets', 'Pets'), ('Tickets', 'Tickets'), ('Toys', 'Toys')], max_length=15),
        ),
        migrations.AlterField(
            model_name='listing',
            name='min_bid',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='u_listing', to=settings.AUTH_USER_MODEL),
        ),
    ]
