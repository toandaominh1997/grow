from useraccount.models import User
import jwt

class UserAdapter(object):
    def __init__(self):
        pass
    def add_user(self, email, password):
        token = jwt.encode({email: password}, "secret", algorithm = "HS256")
        print("token: ", token)
        User.objects.update_or_create(email=email, password=password, jwt = token)
        return True
    def validate_user(self, email, password):
        res = User.objects.filter(email = email, password = password)
        if res.exists():
            return {"jwt": res[0].jwt}
        else:
            return False
    def get_user(self, email, password):
        res = User.objects.filter(email = email, password = password)
        if res.exists():
            user = {
                "email": email,
                "password": password
            }
            return {"user": user, "jwt": res[0].jwt}
        else:
            return False


