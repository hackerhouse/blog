#!/usr/bin/python
#-*- coding: utf-8 -*-

import waltz

urls = ('/analytics/?', 'waltz.modules.Analytics',
        '/([0-9]+)', 'routes.blog.Post',
        '/404/?', 'routed.index.NotFound',
        '/?', 'routes.index.Index')

app = waltz.setup.dancefloor(urls, globals())

if __name__ == "__main__":
    app.run()
