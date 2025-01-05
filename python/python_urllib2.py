import urllib2

# if not (200 <= code < 300): response = self.parent.error( 'http', request, response, code, msg, hdrs)
#
# The HTTPRedirectHandler automatically deals with HTTP 301, 302, 303 and 307 redirect errors
# if (code in (301, 302, 303, 307) and m in ("GET", "HEAD") or code in (301, 302, 303) and m == "POST"):
# http_error_301 = http_error_303 = http_error_307 = http_error_302
#
# /usr/lib/python2.7/urllib2.py
# /usr/lib/python2.7/test/test_urllib2.py

# 200 OK
# 201 Created
# 301 Moved Permanently
# 302 Found
# 303 See Other
# 304 Not Modified
# 307 Temporary Redirect
# 400 Bad Request
# 401 Unauthorized
# 403 Forbidden
# 404 Not Found
# 405 Method Not Allowed
# 409 Conflict
# 413 Request Entity Too Large
# 415 Unsupported Media Type
# 500 Internal Server Error
# 501 Not Implemented
# 502 Bad Gateway
# 503 Service Unavailable
# 504 Gateway Timeout
# 505 HTTP Version Not Supported
#
# https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

def send_http_request(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    try:
        returncode = response.code
        returndata = response.read()
    finally:
        response.close()
    return (returncode, returndata)

def send_http_request2(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    try:
        returncode = response.code
        if returncode != 200:
            raise ValueError('http status code is %s (not 200)' % returncode)
        returndata = response.read()
    finally:
        response.close()
    return (returncode, returndata)

# url = 'http://httpstat.us/200'
# url = 'http://httpbin.org/status/200'

# url = 'http://httpbin.org/status/200'
# returncode, returndata = send_http_request(url)
# print(returncode) # 200
# # print(returndata)

# url = 'http://httpbin.org/status/201'
# returncode, returndata = send_http_request(url)
# print(returncode) # 201
# # print(returndata)

# url = 'http://httpbin.org/status/301'
# returncode, returndata = send_http_request(url)
# print(returncode) # 200
# # print(returndata)

# url = 'http://httpbin.org/status/302'
# returncode, returndata = send_http_request(url)
# print(returncode) # 200
# # print(returndata)

# url = 'http://httpbin.org/status/303'
# returncode, returndata = send_http_request(url)
# print(returncode) # 200
# # print(returndata)

# url = 'http://httpbin.org/status/307'
# returncode, returndata = send_http_request(url)
# print(returncode) # 200
# # print(returndata)

# url = 'http://httpbin.org/status/304'
# returncode, returndata = send_http_request(url)
# print(returncode) # urllib2.HTTPError: HTTP Error 304: NOT MODIFIED
# # print(returndata)

# url = 'http://httpbin.org/status/400'
# returncode, returndata = send_http_request(url)
# print(returncode) # urllib2.HTTPError: HTTP Error 400: BAD REQUEST
# # print(returndata)

# url = 'http://httpbin.org/status/401'
# returncode, returndata = send_http_request(url)
# print(returncode) # urllib2.HTTPError: HTTP Error 401: UNAUTHORIZED
# # print(returndata)

# url = 'http://httpbin.org/status/403'
# returncode, returndata = send_http_request(url)
# print(returncode) # urllib2.HTTPError: HTTP Error 403: FORBIDDEN
# # print(returndata)

# url = 'http://httpbin.org/status/404'
# returncode, returndata = send_http_request(url)
# print(returncode) # urllib2.HTTPError: HTTP Error 404: NOT FOUND
# # print(returndata)

# url = 'http://httpbin.org/status/500'
# returncode, returndata = send_http_request(url)
# print(returncode) # urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR
# # print(returndata)

# url = 'http://httpbin.org/status/502'
# returncode, returndata = send_http_request(url)
# print(returncode) # urllib2.HTTPError: HTTP Error 502: BAD GATEWAY
# # print(returndata)

# url = 'http://httpbin.org/status/503'
# returncode, returndata = send_http_request(url)
# print(returncode) # urllib2.HTTPError: HTTP Error 503: SERVICE UNAVAILABLE
# # print(returndata)

# url = 'http://httpbin.org/status/504'
# returncode, returndata = send_http_request(url)
# print(returncode) # urllib2.HTTPError: HTTP Error 504: GATEWAY TIMEOUT
# # print(returndata)
