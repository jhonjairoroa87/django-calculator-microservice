__author__ = 'jhonjairoroa87'

from rest_framework.views import APIView
from rest_framework.response import Response


class Multiply(APIView):
    @staticmethod
    def get(request):
        try:
            first_number = int(request.GET.get('a'))
            second_number = int(request.GET.get('b'))
            return Response({'result': first_number * second_number})
        except Exception as e:
            return Response({'result': 'there was an error ' + str(e)})


class Divide(APIView):
    @staticmethod
    def get(request):
        try:
            first_number = int(request.GET.get('a'))
            second_number = int(request.GET.get('b'))
            return Response({'result': first_number / second_number})
        except Exception as e:
            return Response({'result': 'there was an error ' + str(e)})

