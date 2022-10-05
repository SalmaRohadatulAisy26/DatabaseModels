# Generated by Django 4.1 on 2022-10-05 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('untirta', '0002_mahasiswa_tendik_alter_dosen_alamatrumah'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('keterangan', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='dosen',
            name='Fakultas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='untirta.fakultas'),
        ),
    ]