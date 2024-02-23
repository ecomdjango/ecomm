from django.db import models


# Create your models here.
class Customer(models.Model):
    fname = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=10)
    adresse = models.CharField(blank=True, max_length=500)
    email = models.EmailField()
    username = models.CharField(blank=True, max_length=50)
    password = models.CharField(max_length=100)

    def register(self):
        self.save()

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    def __str__(self):
        return f"{self.fname} {self.phone} {self.adresse} {self.email} {self.username}"

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class Commande(models.Model):
    LIVRAISON_CHOICES = (
        ('en_stock', 'En Stock'),
        ('en_route', 'En Route'),
        ('livre', 'Livré'),
        ('annule', 'Annulé'),
    )
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)
    livraison = models.CharField(max_length=20, choices=LIVRAISON_CHOICES, default='en_stock')

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom
