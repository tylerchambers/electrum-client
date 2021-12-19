import json
import socket
from .requests import Request


class Client:
    def __init__(self, addr: str, port: int) -> None:
        self.conn = socket.create_connection((addr, port))
        self.file = self.conn.makefile("r")
        self.request_id = 0

    def call(self, request: Request) -> dict:
        request.set_id(self.request_id)
        self.request_id += 1

        message = request.to_json() + "\n"
        self.conn.sendall(message.encode("ascii"))
        return json.loads(self.file.readline())

    def close(self) -> None:
        self.file.close()
        self.conn.close()
