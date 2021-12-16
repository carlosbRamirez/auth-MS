from rest_framework import serializers
from authApp.models.user import User

#serializar 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
       #serializar de usuario los siguientes campos 
       model = User
       fields = ['id', 'username', 'password', 'name', 'email',]
    #metodo propio de la clase para que me retorne solo los valores definidos y no todos junto con el password
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id'        : user.id,
            'username'  : user.username,
            'name'      : user.name,
            'email'     : user.email,
        }