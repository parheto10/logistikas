# Generated by Django 3.2.13 on 2022-06-30 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigle', models.CharField(max_length=255)),
                ('titre', models.CharField(max_length=500)),
                ('debut', models.DateField()),
                ('fin', models.DateField()),
                ('etat', models.CharField(choices=[('en_cours', 'EN COURS'), ('suspendu', 'SUSPENDU'), ('traite', 'TRAITE')], max_length=50)),
                ('add_le', models.DateTimeField(auto_now_add=True)),
                ('update_le', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'projet',
                'verbose_name_plural': 'PROJETS',
                'ordering': ['sigle'],
            },
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('poste', models.CharField(max_length=255)),
                ('prenoms', models.CharField(blank=True, max_length=255, null=True)),
                ('contact1', models.CharField(max_length=255)),
                ('contact2', models.CharField(blank=True, max_length=255, null=True)),
                ('email_pro', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'responsable projet',
                'verbose_name_plural': 'RESPONSABLES PROJETS',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Technicien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenoms', models.CharField(blank=True, max_length=255, null=True)),
                ('localite', models.CharField(max_length=255)),
                ('contact1', models.CharField(max_length=255)),
                ('contact2', models.CharField(blank=True, max_length=255, null=True)),
                ('poste', models.CharField(choices=[('AIDE', 'AIDE'), ('PEPINIERISTE', 'PEPINIERISTE'), ('SUPERVISEUR', 'SUPERVISEUR'), ('TECHNICIEN', 'TECHNICIEN AGRICOLE'), ('AUTRE', 'AUTRE')], max_length=255, verbose_name='POSTE OCCUPE')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametres.projet')),
            ],
            options={
                'verbose_name': 'technicien',
                'verbose_name_plural': 'TECHNICIENS',
                'ordering': ['nom'],
            },
        ),
        migrations.AddField(
            model_name='projet',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametres.responsable'),
        ),
    ]