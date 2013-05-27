import os
import markdown
from waltz import web, render

_path = os.getcwd()

class Post:
    def GET(self, post):
        path = '%s/blog/posts/%s' % (_path, post)
        if os.path.isfile(path):
            with open(path) as p:
                return render().post(markdown.markdown(p.read()))
        raise web.notfound()
