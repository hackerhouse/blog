import markdown
import web
import os

_path = os.getcwd()

class Post:
    def GET(self, post):
        path = '%s/blog/posts/%s' % (_path, post)
        if os.path.isfile(path):
            with open(path) as p:
                return markdown.markdown(p.read())
        raise web.notfound()
