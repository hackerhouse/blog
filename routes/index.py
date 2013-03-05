from waltz import render, track

class Index:
    @track
    def GET(self):
        return render().index()

class NotFound:
    def GET(self):
        return "404"
