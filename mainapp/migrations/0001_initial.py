# Generated by Django 4.2 on 2023-04-23 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='graphic_img')),
            ],
            options={
                'verbose_name_plural': 'Rasmlar',
            },
        ),
        migrations.CreateModel(
            name='CalculationResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('x1', models.FloatField(blank=True, default=0, null=True)),
                ('x2', models.FloatField(blank=True, default=0, null=True)),
                ('x3', models.FloatField(blank=True, default=0, null=True)),
                ('x4', models.FloatField(blank=True, default=0, null=True)),
                ('y1', models.FloatField(blank=True, default=0, null=True)),
                ('y2', models.FloatField(blank=True, default=0, null=True)),
                ('y3', models.FloatField(blank=True, default=0, null=True)),
                ('y4', models.FloatField(blank=True, default=0, null=True)),
                ('z1', models.FloatField(blank=True, default=0, null=True)),
                ('z2', models.FloatField(blank=True, default=0, null=True)),
                ('z3', models.FloatField(blank=True, default=0, null=True)),
                ('z4', models.FloatField(blank=True, default=0, null=True)),
                ('r1', models.FloatField(blank=True, default=0, null=True)),
                ('r2', models.FloatField(blank=True, default=0, null=True)),
                ('r3', models.FloatField(blank=True, default=0, null=True)),
                ('r4', models.FloatField(blank=True, default=0, null=True)),
                ('rkv1', models.FloatField(blank=True, default=0, null=True)),
                ('rkv2', models.FloatField(blank=True, default=0, null=True)),
                ('rkv3', models.FloatField(blank=True, default=0, null=True)),
                ('rkv4', models.FloatField(blank=True, default=0, null=True)),
                ('img', models.ImageField(null=True, upload_to='img')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Koordinatalar',
            },
        ),
    ]
