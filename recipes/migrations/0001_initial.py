# Generated by Django 5.1.7 on 2025-03-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('number', models.CharField(max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(help_text='Wpisz nazwę dania', max_length=50)),
                ('cuisine', models.CharField(choices=[('polska', 'Polska'), ('wloska', 'Włoska'), ('tajska', 'Tajska'), ('wegierska', 'Węgierska')], help_text='Wybierz rodzaj kuchni', max_length=50)),
                ('ingredients', models.TextField(help_text='Wpisz składniki wraz z ilością, oddzielając je przecinkami (np. Mąka - 200g,Woda - 100ml,Sól - 1 łyczeczka)')),
                ('preparation_time', models.IntegerField(default=0, help_text='Wpisz czas przygotowania w minutach')),
                ('cooking_time', models.IntegerField(default=0, help_text='Wpisz czas wykonania przepisu w minutach')),
                ('allergens', models.ManyToManyField(blank=True, related_name='recipes', to='recipes.allergen')),
            ],
        ),
    ]
