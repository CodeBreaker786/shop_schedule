
from rest_framework import serializers
from shops.models import Shop
from shops.utils import is_shop_open





class ShopSerializer(serializers.ModelSerializer):
      is_shop_open=serializers.SerializerMethodField()
      
      
      class Meta:     
            model= Shop
            fields = "__all__"
       
      def get_is_shop_open(self,object):
          return is_shop_open()
         
                  
              
                  
                  
                  
                  
   
        
        