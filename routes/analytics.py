from waltz import db

class Analytics:
    def GET(self):
        return db().get('analytics')
