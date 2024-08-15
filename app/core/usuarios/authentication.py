from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

#esta clase permite determinar el tiempo de expiracion del token del usuario

class ExpiringTokenAuthentication(TokenAuthentication):
    
    #esta funcion determina el tiempo restante del token dependiendo de los segundos que se configura en settings
    def expires_in(self, token):
        time_elapsed= timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time
    
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)
    
    def token_expire_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user=user)
            return token
        return token
    
    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
        except self.get_model().DoesNotExist:
            raise AuthenticationFailed('Invalid token')
        
        token = self.token_expire_handler(token)
        
        if not token.user.is_active:
            raise AuthenticationFailed('User is inactive or deleted')
        
        return (token.user, token)