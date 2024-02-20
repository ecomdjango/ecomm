from django.contrib import admin
from .models import Category, Product, Commande, Livraison
# Register your models here.
admin.site.site_header ="E-commerce"
admin.site.site_title ="AYM-shop"
admin.site.index_title ="Manager"


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    
    
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price',)
    
class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville', 'pays','total', 'date_commande')
    

class AdminLivraison(admin.ModelAdmin):
    list_display = ('status', 'commande', 'date_added') 

admin.site.register(Livraison, AdminLivraison)

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Commande, AdminCommande)
