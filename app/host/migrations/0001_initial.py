# Generated by Django 3.2.9 on 2022-01-07 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('vizier_id', models.CharField(max_length=20)),
                ('id_column', models.CharField(max_length=20)),
                ('ra_column', models.CharField(max_length=20)),
                ('dec_column', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('sedpy_id', models.CharField(max_length=20)),
                ('hips_id', models.CharField(max_length=20)),
                ('vosa_id', models.CharField(max_length=20)),
                ('image_download_method', models.CharField(max_length=20)),
                ('pixel_size_arcsec', models.FloatField()),
                ('wavelength_eff_angstrom', models.FloatField()),
                ('wavelength_min_angstrom', models.FloatField()),
                ('wavelength_max_angstrom', models.FloatField()),
                ('vega_zero_point_jansky', models.FloatField()),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.survey')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogPhotometry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('mag_column', models.CharField(max_length=20)),
                ('mag_error_column', models.CharField(max_length=20)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.catalog')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.filter')),
            ],
        ),
        migrations.AddField(
            model_name='catalog',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.survey'),
        ),
    ]