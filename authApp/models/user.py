from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    #una metodo propio de la clase que me recibe un username.
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        #si no se recibio un username me captura un error.
        if not username:
           raise ValueError('Users must have an username')
           #esta variable me almacenara un metodo que me guarda el username
        user = self.model(username=username)
        #a ese user tambien se le almacena su password
        user.set_password(password)
        #se guarda en nuestra base de datos
        user.save(using=self._db)
        return user
    #se crea otra metodo que sera un admin pero de django.
    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        #se crea la variable user que me almacena el metodo create_user 
        user = self.create_user(
           username=username,
           password=password,
        )
        #una varible con la funcion is_admin para decir que es verdadero
        user.is_admin = True
        #se guarda en el fondo de nuestra base de datos
        user.save(using=self._db)
        return user
#creo una clase de user donde iran todas las variables que se almacenaran en la base de datos

class User(AbstractBaseUser, PermissionsMixin):
   id = models.BigAutoField(primary_key=True)
   username = models.CharField('Username', max_length = 15, unique=True)
   password = models.CharField('Password', max_length = 256)
   name = models.CharField('Name', max_length = 30)
   email = models.EmailField('Email', max_length = 100)

#creo una metodo que sera propio de mi clase user porque tiene la variable self para indicar
#que esta relacionada a un objeto para
#la variable **kwargs me indica que me recibira distintos argumentos de tamano variable y me 
#y me los almacenara en un dicionario
   def save(self, **kwargs):
       #creo una variable que me almacenara un codigo que me permitira codificar mi password
       some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
       #la variable password que es propia de la clase user le asigno una funcion 
       #que me codificara esa password recibida en el front y me la codificara junto con mi
       #some_salt
       self.password = make_password(self.password, some_salt)
       #uso el constructor super de la clase AbstractBaseUser que hereda una funcion propia llamada save para guardar ese 
       # diccionario **kwargs en un punto en el fondo de mi base de datos.
       super().save(**kwargs)

   objects = UserManager()
   #esta variable me indica que la autentificacion me la va a realizar con el username 
   #ya que es un campo unico.
   USERNAME_FIELD = 'username'