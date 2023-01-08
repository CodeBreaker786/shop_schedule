import uuid
from django.db import models




 




class Shop(models.Model):
      
  id                       =                   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name                     =                   models.CharField(max_length=100)
  rate                     =                   models.DecimalField(default=0.0,max_digits=2,decimal_places=1)
  ratings                  =                   models.IntegerField(default=0)
  address                  =                   models.CharField(max_length=100)
  city                     =                   models.CharField(max_length=100)
  phone                    =                   models.CharField(max_length=100) 
  email                    =                   models.EmailField(unique=True)
  cancelation_policy       =                   models.CharField(max_length=300)
  website                  =                   models.URLField()
  description              =                   models.CharField(max_length=500)
  main_photo               =                   models.ImageField(upload_to='images/' )
  gender_specific          =                   models.CharField(max_length = 10,default = 'MEN',choices=(('MEN','men'),('WOMAN','women')))
  
  
    
  def __str__(self):
    return self.name



