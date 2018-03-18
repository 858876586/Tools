#coding=utf-8
import cgi
from http.server import BaseHTTPRequestHandler



class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            })

        self.send_response(200)
        self.end_headers()
        self.wfile.write(
            bytes('Client: %sn ' % str(self.client_address), 'ascii'))
        self.wfile.write(
            bytes('User-agent: %sn' % str(self.headers['user-agent']),
                  'ascii'))
        self.wfile.write(bytes('Path: %sn' % self.path, 'ascii'))
        self.wfile.write(b'Form data:n')
        for field in form.keys():
            field_item = form[field]
            filename = field_item.filename
            filevalue = field_item.value
            filesize = len(filevalue)  #文件大小(字节)
            with open(filename, 'wb') as f:
                f.write(filevalue)
        return


def StartServer():
    from http.server import HTTPServer
    sever = HTTPServer(("", 80), PostHandler)
    sever.serve_forever()


if __name__ == '__main__':
    StartServer()
