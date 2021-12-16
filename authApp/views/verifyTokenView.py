from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenVerifySerializer

class VerifyTokenView(TokenVerifyView):
   #metodo propio de esta clase
   def post(self, request, *args, **kwargs):
     #una variable que los datos que me va a serializar son los que llegan de la solicitud.
     #cuando se usa get mis datos viajan por la url
     #cuando se usa post los datos viajan por la url pero en un paquete que no es visible
    serializer = TokenVerifySerializer(data=request.data)
    #una variable que me guarda un algoritmo para decodificar
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    #se usa el try para que me haga algo y si sucede un error me lo ccapte con el except pero no me dane 
    #la ejecucion del programa
    try:
      #se verifica que el token exista
      serializer.is_valid(raise_exception=True)
      #dentro de request.data hay una variable llamada token que es la que vamos a decodificar
      #el token decodificado contiene toda la informacion de user
      token_data = tokenBackend.decode(request.data['token'],verify=False)
      #si el token existe me retorna una clave UserId con el valor de user_id
      serializer.validated_data['UserId'] = token_data['user_id']
    
    except TokenError as e:
        raise InvalidToken(e.args[0])
    return Response(serializer.validated_data, status=status.HTTP_200_OK)