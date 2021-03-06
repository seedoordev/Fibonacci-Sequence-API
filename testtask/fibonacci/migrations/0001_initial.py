# Generated by Django 3.2.3 on 2021-07-12 18:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FibonacciSequence',
            fields=[
                ('parameter', models.IntegerField(primary_key=True, serialize=False)),
                ('start_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('OK', 'Done'), ('IP', 'In progress')], default='IP', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ResultNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=10000, null=True)),
                ('sequence_parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sequence', to='fibonacci.fibonaccisequence')),
            ],
        ),
    ]
