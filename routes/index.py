from waltz import render, track

class Index:
    @track
    def GET(self):
        return render().index()
