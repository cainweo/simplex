from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Create your models here.

CATEGORY = (
    ('Outils1', 'outils1'),
    ('Outils2', 'outils2'),
    ('Outils3', 'outils3'),
)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    category =  models.CharField(max_length=255, choices=CATEGORY)
    quantity = models.PositiveIntegerField(null=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}-{self.quantity}'
    
class Order(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null = True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username }'
    

class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Employe(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employe', 'Employé'),
    )
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"    

class Reservation(models.Model):
    STATUT_CHOICES = (
        ('en_attente', 'En attente'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('termine', 'Terminé'),
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.employe} - {self.date_debut} - {self.date_fin}"

class ReservationOutil(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    outil = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.reservation} - {self.outil} - {self.quantite}"