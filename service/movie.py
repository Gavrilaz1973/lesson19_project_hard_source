from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        if filters.get("status") == "new":
            vol = int(filters.get("page"))
            return self.dao.get_by_status(vol)
        elif filters.get("page") is not None:
            vol = int(filters.get("page"))
            movies = self.dao.get_by_page(vol)
        else:
            movies = self.dao.get_all()
        return movies

