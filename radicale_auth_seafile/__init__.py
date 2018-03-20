import requests
from radicale.auth import BaseAuth

class Auth(BaseAuth):
    def is_authenticated(self, user, password):
        server_address = self.configuration.get("auth", "server")
        data = {
            'username': user,
            'password': password,
        }
        address = str(server_address).strip('/') + '/api2/auth-token/'
        self.logger.info("Login attempt by {0} on '{1}'".format(user, address))
        try:
            res = requests.post(address, data=data)
            return int(res.status_code) == 200
        except Exception as error:
            self.logger.error("Error while authenticating: " + str(error))
            return False
