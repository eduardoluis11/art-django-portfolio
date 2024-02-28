from django.db import models

""" Para registrar usuarios y dejarles que inicien sesión, voy a usar la biblioteca "Abstract User", ya que me deja 
hacer esto muy rápidamente.
"""
from django.contrib.auth.models import AbstractUser

# Create your models here.

""" Modelo para almacenar usuarios.

Esto me dejará tanto registrar usuarios, como dejarles iniciar sesión.

Quiero que los usuarios puedan iniciar sesión usando su email, no su nombre de usuario, pero, normalmente, no puedo 
hacer eso, ya que los emails en el modelo "User" NO tienen la restriccion "unique". Es decir, 2 usuarios distintos
pueden usar el mismo email. YO NO QUIERO ESO. 

Entonces, crearé un modelo de usuarios customizado en donde los emails tengan que ser únicos. Así, un email no se 
podrá repetir. Así, si un usuario inicia sesión con su email, la base de datos sabrá exactamente a cual usuario único
se refiere.

Tendré que agregar nuevos campos a CustomUser. Puedo agregar campos como “tipo de usuario”, en donde el tipo de usuario 
puede ser “administrador”, “capturista”, “vendedor” o “comprador”. El campo será opcional para evitar complicaciones. 

Luego, en el layout.html, lo que haré es revisar si request.user.tipo_de_usuario es “administrator”, 
“seller” o “buyer”, y dependiendo de eso, pondré si renderizar el enlace de “Registrar Productos”.
"""


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Email. Two different users can't use the same email.

    # Useer's Profile type (Administrator, Seller, etc) (OPCIONAL)
    profile_type = models.CharField(blank=True, null=True, max_length=13)
