# Generated by Django 5.0.7 on 2024-08-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_mouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pendrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_purchase', models.DateField()),
                ('brand', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('pendrive_status', models.CharField(max_length=50)),
                ('storage', models.CharField(max_length=50)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('warranty_details', models.CharField(max_length=255)),
                ('warranty_date', models.DateField()),
                ('purchased_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
