# Seafile Authentication Plugin for Radicale
radicale_auth_seafile is a Radicale plugin that uses a Seafile server to perform the authentication.

## Installation
1. Install radicale_auth_seafile
```
git clone https://github.com/hazward/radicale-auth-seafile.git
cd radicale-auth-seafile
python setup.py install
```
2. Edit the configuration file to use the plugin
```
[auth]
type = radicale_auth_seafile
server = "http://<seafile address>"
```

3. Restart your Radicale server