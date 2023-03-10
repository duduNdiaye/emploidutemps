# Generated by Django 4.1.5 on 2023-01-27 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0005_alter_edt_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creneau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('matiere', models.CharField(max_length=255)),
                ('type_creneau', models.CharField(choices=[('Cours', 'Cours'), ('TD', 'TD'), ('TP', 'TP')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('Informatique', 'Informatique'), ('Physique Chimie', 'Physique Chimie'), ('Science Eau Environnement', 'Science Eau Environnement'), ('Mathematique', 'Mathematique')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edt.departement')),
            ],
        ),
        migrations.CreateModel(
            name='GroupeTDTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('M1', 'M1'), ('M2', 'M2')], max_length=255)),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edt.filiere')),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='EDT',
        ),
        migrations.AddField(
            model_name='groupetdtp',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edt.promotion'),
        ),
        migrations.AddField(
            model_name='creneau',
            name='departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edt.departement'),
        ),
        migrations.AddField(
            model_name='creneau',
            name='enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edt.enseignant'),
        ),
        migrations.AddField(
            model_name='creneau',
            name='promo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edt.promotion'),
        ),
        migrations.AddField(
            model_name='creneau',
            name='salle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edt.salle'),
        ),
    ]
