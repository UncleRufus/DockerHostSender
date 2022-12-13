#!/usr/bin/env python
# Imports
import http.server
import json
import locla_script

# TypeHints
from typing import Any

HOST: str = '0.0.0.0'
PORT: int = 9999

urlpatterns: dict[str, Any] = {
    'get_pwd': locla_script.execute_local_command
}


class HostHTTPServer(http.server.SimpleHTTPRequestHandler):
    """
    Локальный сервер слущающий порт 9999
    """
    def do_GET(self) -> None:
        path: list[str] = self.path.split('/')

        if path[1] in urlpatterns.keys():
            message: dict[str, Any] = json.dumps(urlpatterns[path[1]]()._asdict())
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(message, "utf8"))
            return

        else:
            message: str = 'Url not found 404'
            self.send_response(404, message)
            self.wfile.write(bytes(message, "utf8"))



if __name__=='__main__':
    server = http.server.HTTPServer((HOST, PORT), HostHTTPServer)
    try:
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        print('Сервер остановлен вручную')