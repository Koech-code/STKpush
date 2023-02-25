from rest_framework.decorators import api_view
from rest_framework.response import Response
from .c2b import lipa_na_mpesa

# Create your views here.
@api_view(['POST'])
def lipa_na_mpesa_online(request):
    mpesa_payment = lipa_na_mpesa()
    return Response({"mpesa_payment": mpesa_payment})