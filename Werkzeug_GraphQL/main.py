import os
import json

from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import SharedDataMiddleware
from jinja2 import Environment, FileSystemLoader
from query import schema


class GraphQLApp(object):

    def __init__(self):
        self.url_map = Map([
            Rule('/graphql', endpoint='graphql'),
            Rule('/graphiql', endpoint='graphiql')
        ])
        self.wsgi_app = SharedDataMiddleware(self.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException, e:
            return e

    def on_graphql(self, request):
        query_dict = json.loads(request.data)
        result = schema.execute(query_dict['query'])
        return Response(json.dumps(result.data))

    def on_graphiql(self, request):
        t = self.jinja_env.get_template('graphiql.html')
        return Response(t.render(), mimetype='text/html')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = GraphQLApp()
    run_simple('localhost', 4000, app)
