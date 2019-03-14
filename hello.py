bind = '0.0.0.0:8080'


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    resp = environ['QUERY_STRING'].split("&")
    resp = [item.encode('utf-8') + "\n" for item in resp]
    return resp

