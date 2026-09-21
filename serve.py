#!/usr/bin/env python3
"""Üzleti angol drill - helyi webszerver (localhost + helyi hálózat)."""
import http.server, socket, socketserver, os, webbrowser, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8931
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        t = super().guess_type(path)
        if t and (t.startswith('text/') or 'javascript' in t or 'json' in t):
            t += '; charset=utf-8'
        return t
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()
    def log_message(self, *a):
        pass

def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80)); ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('0.0.0.0', PORT), Handler) as httpd:
    url = 'http://localhost:%d/index.html' % PORT
    print('\n  Üzleti angol drill fut.')
    print('  Ezen a gépen:  ' + url)
    print('  Telefonról (azonos wifin):  http://%s:%d/index.html' % (lan_ip(), PORT))
    print('\n  Leállítás: Ctrl+C  (vagy csukd be ezt az ablakot)\n')
    try:
        webbrowser.open(url)
    except Exception:
        pass
    httpd.serve_forever()
