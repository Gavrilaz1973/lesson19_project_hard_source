from service.user import UserService
import datetime
import calendar
import jwt

secret = 's3cR$eT'
algo = 'HS256'

class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def checking_user(self, data):
        data_all = self.user_service.get_all()
        email = data['email']
        for user in data_all:
            if user.email == email:
                if self.user_service.compare_passwords(user.password, data['password']) is True:
                    return self.generate_tokens(user)
                else:
                    return "", 404
        return '', 401

    def generate_tokens(self, user):
        if user is None:
            raise Exception()

        data = {"name": user.name, "email": user.email}
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)
        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_new_tokens(self, data):
        access_token = data.get("access_token")
        refresh_token = data.get('refresh_token')
        email = jwt.decode(jwt=access_token, key=secret, algorithms=algo).get('email')
        email_r = jwt.decode(jwt=refresh_token, key=secret, algorithms=algo).get('email')
        user = self.user_service.get_by_email(email)
        if email == email_r:
            return self.generate_tokens(user)
        return "", 401







