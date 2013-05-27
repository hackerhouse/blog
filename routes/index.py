import markdown
from waltz import render, track
import os

class Index:
    def GET(self):
        posts = []
        filenames = os.listdir(os.path.join(os.getcwd(),"blog","posts"))
        for filename in filenames:
            with open(os.path.join(os.getcwd(),"blog","posts",filename)) as f:
                posts.append((filename, markdown.markdown(f.read())))
        return render().index(posts)

class NotFound:
    def GET(self):
        return "404"
