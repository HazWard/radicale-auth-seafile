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
        self.logger.info("Auth Address: " + address)
        res = requests.post(address, data=data)
        self.logger.info("Login attempt by %r with password %r",
                         user, password)
        return int(res.status_code) == 200
