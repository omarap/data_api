from django.db import models
from django.db.models import Sum
from django.core.serializers import serialize
from django.contrib.auth.models import User


# Create your models here.
#Project Affected Person Model
class ProjectAffectedPerson(models.Model):
    pap_image = models.ImageField(upload_to='pap_uploads', blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=128)
    nin = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=20, unique=True)
    phone_number = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='owners', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.nin}"

class ConstructionList(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
class ConstructionBuilding(models.Model):
    """
    CONSTRUCTION_TYPES = [
    ('Fire-resistive', 'Fire-resistive'),
    ('Non-combustible', 'Non-combustible'),
    ('Ordinary', 'Ordinary'),
    ('Heavy timber', 'Heavy timber'),
    ('Wood-framed', 'Wood-framed')
    ]
    """
    pap = models.ForeignKey(ProjectAffectedPerson, related_name='pap_construction',on_delete=models.CASCADE)
    name = models.ForeignKey(ConstructionList, related_name='list_of_construction', on_delete=models.CASCADE)
    construction_image = models.ImageField(upload_to='construction_uploads', blank=True)
    size = models.FloatField(default=0)
    number_of_construction = models.PositiveSmallIntegerField(default=0)
    rate = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def value_of_structures(self):
        return self.size * self.number_of_construction * self.rate
   
class TreeList(models.Model):
    name = models.CharField(max_length=100)
    rate = models.PositiveIntegerField(default=0, blank=True)
    district = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   

class Tree(models.Model):
    """
    TREE_TYPES= [
        ('apple_tree', 'apple_tree'),
        ('mango_tree', 'mango_tree'),
        ('avocado_tree', 'avocado_tree'),
        ('papaya_tree', 'papaya_tree'),
        ('orange_tree', 'orange_tree'),
        ('lemon_tree', 'lemon_tree'),
        ('black_willow_tree', 'black_willow_tree'),
        ('black_wallnut_tree', 'black_wallnut_tree'),
        ('beech_tree', 'beech_tree'),
        ('hazel_tree', 'hazel_tree'),
        ('common_ash_tree', 'common_ash_tree'),
        ('hawthorn_tree', 'hawthron_tree'),
        ('maple_tree', 'maple_tree'),
        ('oak_tree', 'oak_tree'),
        ('cedar_tree', 'cedar_tree'),
        ('cucumber_tree', 'cucumber_tree'),
        ('mivule_tree', 'mivule_tree'),
        ('jackfruit_tree', 'jackfruit_tree'),
        ('pine_tree', 'pine_tree'),
        ('moringa_tree', 'moringa_tree'),
        ('guava_tree', 'guava_tree'),
        ('banyan_tree', 'banyan_tree'),
        ('neem_tree', 'neem_tree'),
        ('peepal_tree', 'peepal_tree'),
        ('aloevera_tree', 'aloevera_tree'),
        ('eucalyptus_tree', 'eucalyptus_tree'),
        ('mahogany_tree', 'mahongany_tree'),
        ('tulip_tree', 'tulip_tree'),
        ('sal_tree', 'sal_tree'),
        ('cork_tree', 'cork_tree'),
        ('turmeric_tree', 'turmeric_tree'),
        ('teak_tree', 'teak_tree'),
        ('others', 'others(add in description)')
    ]

    """
    pap = models.ForeignKey(ProjectAffectedPerson, related_name='pap_trees',on_delete=models.CASCADE)
    name = models.ForeignKey(TreeList, related_name = 'list_of_trees',on_delete=models.CASCADE)
    description = models.CharField(max_length=50, blank=True)
    tree_image = models.ImageField(upload_to='tree_uploads', blank=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    rate = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    @property
    def value_of_trees(self):
        return self.quantity * self.rate
   
class CropList(models.Model):
    name = models.CharField(max_length=50)
    rate = models.PositiveIntegerField()
    district = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.rate} {self.district}"

# Class model for crop
class Crop(models.Model):
    QUALITY_CHOICES= [
        ('Mature_good', 'Mature_good'),
        ('Mature', 'Mature'),
        ('Immature_good', 'Immature_good'),
        ('Immature', 'Immature'),
    ]
    '''
    CROP_NAMES = [
    ('Bananas', (
            ('sweet bananas', 'sweet bananas'),
            ('matooke', 'matooke'),
            ('bananas(bogoya)', 'bananas(bogoya)'),
            ('bananas(gonja)', 'bananas(gonja)'),
        )
    ),
    ('Greens', (
            ('cabage', 'cabage'),
            ('nakati', 'nakati'),
            ('others', 'others(add in description)'),
        )
    ),
    ('Peas', (
            ('Peas', 'Peas'),
            ('Cow_peas', 'Cow_peans'),
        )
    ),
    ('coffee', 'coffee'), 
    ('beans', 'beans'),
    ('Maize', 'Maize'),
    ('Cassava', 'Cassava'),
    ('sweet_potatoes', 'sweet_potatoes'),
    ('sugar_cane', 'sugar_cane'),
    ('rice', 'rice'),
    ('yams', 'yams'),
    ('ground_nuts', 'ground_nuts'),
    ('others', 'others(add in description)'),
    ('Fruits', (
            ('pineapples', 'pineaples'),
            ('apples', 'apples'),
            ('black_berries', 'black_berries'),
            ('mangoes', 'mangoes'),
            ('lemon', 'lemon'),
            ('oranges', 'oranges'),
            ('others', 'others(add in description)'),
        )
    ),
]
    '''
    crop_name = models.ForeignKey(CropList, related_name='crop_list', on_delete=models.CASCADE )
    crop_image = models.ImageField(upload_to='crop_uploads', blank=True)
    description = models.CharField(max_length=50, blank=True)
    quantity = models.PositiveIntegerField()
    quality = models.CharField(max_length=20, choices = QUALITY_CHOICES)
    rate = models.PositiveIntegerField()
    pap = models.ForeignKey(ProjectAffectedPerson, related_name='pap_crops',on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{ self.name} { self.pap} { self.quantity}"
    
    @property
    def value_of_crops(self):
        return self.quantity * self.rate

   
class LandList(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

class TenureType(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Land(models.Model):
    """
    LAND_TYPES= (
        ('Urban/Built-up Land', 'Urban/Built-up Land'),
        ('Agricultural Land', 'Agricultural Land'),
        ('Rangeland', 'Rangeland'),
        ('Forest Land', 'Forest Land'),
        ('Water Areas', 'Water Areas'),
        ('Wetland', 'Wetland'),
        ('Barren Land.', 'Barren Land'),
        ('Tundra', 'Tundra'),
        ('Perennial snow or ice', 'Perennial snow or ice'),
        ('Others(add in description)', 'Others(add in description)')

    )
    """
    """
    TENURE_TYPES= (
        ('Mailo Land', 'Mailo Land'),
        ('Freehold Land', 'Freehold Land'),
        ('Lease Land', 'Lease Land'),
        ('Customary Land', 'Customary Land')
    )
    """
    land_type = models.ForeignKey(LandList, related_name='list_of_land', on_delete=models.CASCADE)
    land_image = models.ImageField(upload_to='land_uploads', blank=True)
    survey_no = models.CharField(max_length=200, blank=True, unique=True, null=True)
    pap = models.ForeignKey(ProjectAffectedPerson, related_name='pap_lands', on_delete=models.CASCADE)
    tenure = models.ForeignKey(TenureType, related_name='tenure_types', on_delete=models.CASCADE)
    size = models.FloatField(blank=True)
    location = models.CharField(max_length=255)
    land_use = models.TextField(blank=True,)
    land_services  = models.TextField(blank=True,)
    rate = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='user_lands', on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.land_type} {  self.pap} "

    @property
    def value_of_land(self):
        return self.size * self.rate
   




    
