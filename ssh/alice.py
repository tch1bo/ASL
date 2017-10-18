from ssh.client import SSHClient

ALICE_PORT = 2224
ALICE_LOGIN = "alice"
ALICE_PASSWORD = "alice"

class Alice(SSHClient):
    def __init__(self):
        SSHClient.__init__(self, ALICE_PORT, ALICE_LOGIN, ALICE_PASSWORD)
