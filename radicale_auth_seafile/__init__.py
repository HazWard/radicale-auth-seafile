import requests
from urllib.parse import urljoin
from radicale.auth import BaseAuth

class Auth(BaseAuth):
    def is_authenticated(self, user, password):
        server_address = self.configuration.get("auth", "server")
        data = {
            'username': user,
            'password': password,
        }
        address = urljoin(str(server_address), '/api2/auth-token/')
        print("Auth Address: " + address)
        res = requests.post(address, data=data)
        return int(res.status_code) == 200

    def is_authenticated2(self, login, user, password):
        return self.is_authenticated(user, password)
