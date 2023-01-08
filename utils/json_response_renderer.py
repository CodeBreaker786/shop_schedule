import re
from rest_framework.renderers import JSONRenderer,StaticHTMLRenderer
from rest_framework.response import Response
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
class MyJsonRenderer(JSONRenderer):
    charset='utf-8'
   
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if 'status' in data:
            return  super().render(data, accepted_media_type, renderer_context)    
        return super().render({'status':True,'message':'','data':data,}, accepted_media_type, renderer_context)
       
    