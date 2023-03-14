from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    # def get_one(self, bid):
    #     return self.session.query(User).get(bid)
    #
    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, data):
        email = data.get("email")
        user = self.get_by_email(email)
        user.name = data.get("name")
        user.surname = data.get("surname")
        user.favorite_genre = data.get("favorite_genre")

        self.session.add(user)
        self.session.commit()


