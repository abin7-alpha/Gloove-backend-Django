from operator import mod
from django.db import models

class Gender(models.Model):
    sex = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.sex

class Category(models.Model):
    sex = models.ForeignKey(Gender, on_delete=models.CASCADE)
    category_title = models.CharField(max_length=50)

    def __str__(self):
        return self.category_title

class SubCategory(models.Model):
    sex = models.ForeignKey(Gender, on_delete=models.RESTRICT)
    cateogry = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_title = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_category_title


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, unique=True)
    short_description = models.CharField(max_length=500)
    image1 = models.ImageField(upload_to='product/%Y/%m/%d/', max_length=255)
    image2 = models.ImageField(upload_to='product/%Y/%m/%d/', max_length=255, blank=True)
    image3 = models.ImageField(upload_to='product/%Y/%m/%d/', max_length=255, blank=True)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

class ProductStock(models.Model):
    SMALL = 'S'
    LARGE = 'L'
    MEDIUM = 'M'
    XTRA_LARGE = 'XL'
    DOUBLE_XTRA = 'XXL'

    SIZE_CHART_CHOICES = [
        (SMALL, 'small'),
        (LARGE, 'large'),
        (MEDIUM, 'medium'),
        (XTRA_LARGE, 'xtra large'),
        (DOUBLE_XTRA, 'double xtra large')
    ]

    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    size_chart = models.CharField(max_length=5, choices=SIZE_CHART_CHOICES, default=SMALL, blank=True)
    cloth_size = models.IntegerField(blank=True)  
    foot_size = models.IntegerField(blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        if self.size_chart:
            return self.product + self.size_chart
        elif self.cloth_size:
            return self.product + self.cloth_size
        elif self.foot_size:
            return self.product + self.foot_size

class ProductGrading(models.Model):

    class Rating(models.IntegerChoices):
        ONE_STAR = 1, "1*"
        TWO_STAR = 2, "2*"
        THREE_STAR = 3, "3*"
        FOUR_STAR = 4, "4*"
        FIVE_STAR = 5, "5*"

    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    rating = models.PositiveSmallIntegerField(choices=Rating.choices, null=True, blank=True)
    reviews = models.TextField(blank=True)
    images = models.FileField(blank=True, upload_to='user_review_images/%Y/%m/%d/')
