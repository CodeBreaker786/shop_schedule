from rest_framework import viewsets
from shops.models import Shop
from shops.utils import is_shop_open
from shops.serializers import ShopSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shops.utils import Tz

import datetime
class ShopView(viewsets.ModelViewSet):
    queryset=Shop.objects.all()
    serializer_class=ShopSerializer 
   
@api_view(['GET'])
def get_shop_status(request):   
    if request.data:
        date=datetime.datetime.fromisoformat(request.data['date']).replace(tzinfo=Tz)
        availabilty=is_shop_open(date=date)
        if availabilty == True:
            return Response('"Shop will be open at selected time"')
        return Response(availabilty)
    return Response( 'Please pass date to check shop availability')