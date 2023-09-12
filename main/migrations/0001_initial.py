# Generated by Django 4.1.5 on 2023-08-10 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('nationality', models.CharField(choices=[('US', 'US'), ('UK', 'UK'), ('FR', 'FR')], max_length=2, verbose_name='Nationality')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10, verbose_name='Room Number')),
                ('room_capacity', models.IntegerField(verbose_name='Room Capacity')),
                ('is_available', models.BooleanField(default=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='main.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100, verbose_name='Guest Name')),
                ('guest_email', models.EmailField(max_length=254, verbose_name='Guest Email')),
                ('guest_nationality', models.CharField(choices=[('US', 'US'), ('UK', 'UK'), ('FR', 'FR')], max_length=2, verbose_name='Guest Nationality')),
                ('check_in_date', models.DateField(verbose_name='Check-in Date')),
                ('check_out_date', models.DateField(verbose_name='Check-out Date')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='main.room')),
            ],
        ),
    ]