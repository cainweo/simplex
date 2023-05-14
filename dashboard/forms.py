from django import forms
from .models import Product



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['name','category','quantity']     ['name','description','category','quantity','price_per_day','price_per_week','price_per_month'] 
"""
class OutilForm(forms.ModelForm):
    class Meta:
        model = Outil
        fields = ['nom', 'description', 'categorie', 'quantite_disponible', 'prix_par_jour', 'prix_par_semaine', 'prix_par_mois']
"""