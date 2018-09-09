SERVER_NAME = None
SECRET_KEY = 'asaad2ewewe0ds.sds'
DEBUG = True

DOMAIN = {
    'chat': {
        # We choose to override global cache-control directives for this resource.
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        # 'title' tag used in item links. Defaults to the resource title minus
        # the final, plural 's' (works fine in most cases but not for 'name')
        'item_title': 'name',

        # by default the standard item entry point is defined as
        # '/companies/<ObjectId>'. We leave it untouched, and we also enable an
        # additional read-only entry point. This way consumers can also perform
        # GET requests at '/company/<company_name>'.
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'name'
        },
        # most global settings can be overridden at resource level
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'schema': {
            'name': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 200,
            },
            'desc': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 200,
            },
            'loc':{
                'type': 'dict',
                'schema': {
                    'type': { 'type':'string'},
                    'coordinates': {
                        'type': 'list'
                    }
                }
            }
        }
    }
}

X_DOMAINS = '*'
X_HEADERS = ['Content-Type', 'Accept', 'If-Match', 'Access-Control-Allow-Origin', 'Authorization']

#Mongo setup
MONGO_HOST = 'mongo'
MONGO_PORT = 27017
MONGO_DBNAME   = 'qomm'
IF_MATCH  = False

#Enable reads (GET), inserts (POST) and delete (DELETE) for resource collection
#If you omit this line,  the API will default to ['GET'] and provide
#Read Only access to the endpoint
RESOURCE_METHODS = ['GET', 'POST']

#Enable reads (GET), edit (PATCH) or (PUT) and delete for item resource
#(default to read only-items access)
ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']

#Enable standard client cache directive for all resource exposed by the
#API. And Always override these global setting letter
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRED = 20