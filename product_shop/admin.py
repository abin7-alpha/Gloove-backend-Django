from sre_constants import CATEGORY_DIGIT
from django.contrib import admin
from product_shop.models import Product, ProductGrading, ProductStock, Gender, SubCategory, Category

admin.site.register(Product)
admin.site.register(ProductStock)
admin.site.register(ProductGrading)
admin.site.register(Gender)
admin.site.register(SubCategory)
admin.site.register(Category)
