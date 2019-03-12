bind = '0.0.0.0:8080'

def app (environ,start_response):
    status = '200 OK'
    headers= [('Content-type','text/plain')]
    start_response(status,headers)
    body="\r\n".join(environ['QUERY_STRING'].split('&'))
    return [body]