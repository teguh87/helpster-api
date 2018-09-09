import os

from eve import Eve
from eve.auth import BasicAuth
import sassutils.wsgi

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == 'hr@helpster.asia' and password == 'betterhelpster'

app = Eve(auth=MyBasicAuth)
app.wsgi_app = sassutils.wsgi.SassMiddleware(app.wsgi_app, {})