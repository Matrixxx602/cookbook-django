from django.db import models

# TextChoices dla rodzaju kuchni:
class Cuisine(models.TextChoices):
    Polska = 'polska'
    Włoska = 'wloska'
    Tajska = 'tajska'
    Węgierska = 'wegierska'

# Utworzenie modelu dla alergenów.
class Allergen(models.Model):
    name = models.CharField(
        max_length=50, unique=True
    )
    number = models.CharField(
        max_length=2, unique=True
    )

    def __str__(self):
        return f"{self.number}. {self.name}"

# Utworzenie modelu głównego z przepisem.
class Recipe(models.Model):
    dish = models.CharField(
        max_length=50,
        help_text='Wpisz nazwę dania',
    )
    cuisine = models.CharField(
        max_length=50,
        choices=Cuisine.choices,
        help_text='Wybierz rodzaj kuchni',
    )
    ingredients = models.TextField(
        help_text='Wpisz składniki wraz z ilością, oddzielając je przecinkami (np. Mąka - 200g,Woda - 100ml,Sól - 1 łyczeczka)',
    )
    allergens = models.ManyToManyField(
        Allergen,
        blank=True,
        related_name='recipes',
    )
    preparation_time = models.IntegerField(
        default=0,
        help_text='Wpisz czas przygotowania w minutach',
    )
    cooking_time = models.IntegerField(
        default=0,
        help_text='Wpisz czas wykonania przepisu w minutach',
    )
    image = models.ImageField(
        upload_to='recipes/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.dish
    
    def get_ingredients_list(self):
        list = []
        for i in self.ingredients.split(','):
            list.append(i)
        return list