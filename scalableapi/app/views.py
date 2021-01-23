import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class JsonInputView(APIView):
   """
   Takes in any json object and reverses the order of elements
   Python 3+ all dictonaries are now OrderedDict 

   """
    
   def post(self, request, *args, **kwargs):
         response_data = {}
         data = json.loads(request.body)

         for key in reversed(data):
            response_data[key] = data[key]

         return Response(response_data)
         




