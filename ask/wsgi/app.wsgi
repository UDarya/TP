from urlparse import parse_qs

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello worl!'

    # get parameters
    output += '\nGET:'
    get_values = parse_qs(environ['QUERY_STRING'])
    for value in get_values:
        output += '\n\t' + value + ' = ' + get_values[value][0]


    # post parameters
    output += '\nPOST:'
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    post_values = parse_qs(request_body)
    for value in post_values:
        output += '\n\t' + value + ' = ' + post_values[value][0]


    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
  

