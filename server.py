#! /usr/bin/env python3

# SPDX-FileCopyRightText: Copyright (c) 2023-present Jeffrey LeBlanc
# SPDX-License-Indentifier: MIT

from pathlib import Path
import json
import asyncio
import tornado


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class APIHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(self.application.posts))

    def post(self):
        msg_dict = tornado.escape.json_decode(self.request.body)
        msg_dict["id"] = len(self.application.posts)
        self.application.posts.append(msg_dict)
        self.write(json.dumps(msg_dict))


class MyApp(tornado.web.Application):

    def __init__(self):
        self._handlers = []
        self._settings = {}
        self.initialize()
        super().__init__(self._handlers,**self._settings)

    def initialize(self):
        # Mock Data
        self.posts = [{
            "id": 0,
            "title": "The First Post!",
            "content": "This is the first of many posts I'm sure"
        },{
            "id": 1,
            "title": "Second Post",
            "content": "Might get boring after a while..."
        }]

        # Get our paths
        self.HERE = Path(__file__).parent
        static_dir =   self.HERE/"static"
        template_dir = self.HERE/"templates"
        files_dir =    self.HERE/"files"

        # Handlers
        self._handlers += [
            (r"^/$", MainHandler),
            (r"^/api/v1/posts/?$",APIHandler),
            (r"^/files/(.*)",tornado.web.StaticFileHandler,{"path":files_dir})
        ]

        # Settings
        self._settings = dict(
            debug= True,
            static_path= static_dir,
            template_path= template_dir,
            autoreload= True
        )


async def main():
    PORT = 8888
    app = MyApp()
    app.listen(PORT)
    print(f"Running at localhost:{PORT}")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
