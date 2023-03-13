from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_page(self, val):
        show_to = (val - 1) * 5
        page = self.session.query(Movie).offset(show_to).limit(5)
        return page

    def get_by_status(self, val):
        show_to = (val - 1) * 5
        return self.session.query(Movie).order_by(Movie.year.desc()).offset(show_to).limit(5)

