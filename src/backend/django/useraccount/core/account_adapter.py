from useraccount.models import User
import jwt

class UserAdapter(object):
    def __init__(self):
        pass
    def add_user(self, email, password):
        User.objects.create_or_update(email=user_name, password=password)
        return True
    def validate_user(self, email, password):
        res = User.objects.filter(email = email, password = password)
        if res.exists():
            encoded_jwt = jwt.encode({email: password}, "secret", algorithm = "HS256")
            return encoded_jwt
        else:
            return False
