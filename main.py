#!/usr/bin/python
#-*- coding: utf-8 -*-

import waltz

urls = ('/analytics/?', 'routes.analytics.Analytics',
        '/?', 'routes.index.Index')

app = waltz.setup.dancefloor(urls, globals())

if __name__ == "__main__":
    app.run()
