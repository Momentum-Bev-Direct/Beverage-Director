from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


CATEGORIES = [
    {
        "cat": "Bourbon",
        "min": 0,
        "max": 99,
    },{
        "cat": "Whiskey - Other",
        "min": 100,
        "max": 199,
    },{
        "cat": "Scotch",
        "min": 200,
        "max": 299,
    },{
        "cat": "Gin",
        "min": 300,
        "max": 399,
    },{
        "cat": "Vodka",
        "min": 400,
        "max": 499,
    },{
        "cat": "Rum",
        "min": 600,
        "max": 649,
    },{
        "cat": "Brandy & Cognac",
        "min": 650,
        "max": 699,
    },{
        "cat": "Cordials & Liqueurs",
        "min": 700,
        "max": 799,
    },{
        "cat": "Tequila & Mezcal",
        "min": 800,
        "max": 899,
    },{
        "cat": "Other",
        "min": 19700,
        "max": 21099,
    },{
        "cat": "Mini",
        "min": 21100,
        "max": 22050,
    },{
        "cat": "Bourbon",
        "min": 22050,
        "max": 22299,
    },{
        "cat": "Rye",
        "min": 22300,
        "max": 22899,
    },{
        "cat": "Bourbon",
        "min": 22900,
        "max": 27999,
    },{
        "cat": "Whiskey - Other",
        "min": 29400,
        "max": 33499,
    },{
        "cat": "Scotch",
        "min": 33600,
        "max": 36999,
    },{
        "cat": "Canadian Whiskey",
        "min": 37700,
        "max": 39050,
    },{
        "cat": "Irish Whiskey",
        "min": 40000,
        "max": 40249,
    },{
        "cat": "Whiskey - Other",
        "min": 40250,
        "max": 40279,
    },{
        "cat": "Gin",
        "min": 40280,
        "max": 43199,
    },{
        "cat": "Vodka",
        "min": 43250,
        "max": 47006,
    },{
        "cat": "Rum",
        "min": 47017,
        "max": 49499,
    },{
        "cat": "Brandy & Cognac",
        "min": 49500,
        "max": 51040,
    },{
        "cat": "Other",
        "min": 51400,
        "max": 65613,
    },{
        "cat": "Cordials & Liqueurs",
        "min": 56700,
        "max": 61999,
    },{
        "cat": "Other",
        "min": 62044,
        "max": 62199,
    },{
        "cat": "Cordials & Liqueurs",
        "min": 62200,
        "max": 64049,
    },{
        "cat": "Tequila & Mezcal",
        "min": 64050,
        "max": 65999,
    },{
        "cat": "NC Products",
        "min": 66000,
        "max": 69999,
    },{
        "cat": "Vodka",
        "min": 70000,
        "max": 70200,
    },
]


class Spirit(models.Model):
    brandname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nc_code = models.CharField(max_length=10)
    supplier = models.CharField(max_length=100)
    proof = models.CharField(max_length=100)
    size = models.FloatField(default=0)
    mxb = models.FloatField(default=0)

    def __str__(self):
        return f'{self.brandname}'

    @property
    def price_per_oz(self):
        bottle_size_oz = float(self.size) * 33.814
        price_per_oz = round(float(self.mxb)/bottle_size_oz, 2)
        return price_per_oz

    @property
    def category(self):
        code = int(self.nc_code.replace('-', ''))
        for category in CATEGORIES:
            if code >= category["min"] and code <= category["max"]:
                return category["cat"]
        else:
            return "Category Not Found"

class MyStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spirit = models.ForeignKey(Spirit, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.spirit.brandname}'


class MiscIngredient(models.Model):
    name = models.CharField(max_length=100)
    cost_per_unit = models.FloatField(default=0)
    notes = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Rating(models.Model):
    stars = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    spirits = models.ForeignKey(Spirit, related_name='ratings', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {stars} stars'


class Cocktail(models.Model):
    user = models.ForeignKey(to=User, related_name='cocktails', on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    target_profit = models.IntegerField(default=20, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return f'{self.name}'

    @property
    def total_cost(self):
        total = 0
        for shot in self.shots.all():
            total += shot.cost
        for portion in self.portions.all():
            total += portion.cost
        return round(total,2)

    @property
    def recommended_price(self):
        """
        product of target_profit and total_cost
        """
        rec_price = round(self.total_cost/(self.target_profit/100),2)
        return rec_price


class Shot(models.Model):
    volume = models.FloatField(default=0)
    cocktail= models.ForeignKey(Cocktail, related_name='shots', on_delete=models.CASCADE)
    spirit = models.ForeignKey(Spirit, related_name='shots', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.volume} of {self.spirit.brandname} for {self.cocktail.name}'

    @property
    def cost(self):
        cost = self.volume * self.spirit.price_per_oz
        return cost


class Portion(models.Model):
    amount = models.FloatField(default=0)
    unit = models.CharField(max_length=10)
    price_per_unit = models.FloatField(default=0)
    cocktail= models.ForeignKey(Cocktail, related_name='portions', on_delete=models.CASCADE)
    misc_ingredient = models.ForeignKey(MiscIngredient, related_name='portions', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}{self.unit} of {self.misc_ingredient.name} for {self.cocktail.name}'

    @property
    def cost(self):
        cost = self.amount*self.price_per_unit
        return cost
