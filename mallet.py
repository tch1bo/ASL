from vm import VM, VMTest
from ssh import sudo_cmd

MALLET_PORT = 2226
MALLET_LOGIN = "mallet"
MALLET_PASSWORD = "mallet"
MALLET_TESTS = [
        VMTest(
            "Hello world test",
            "echo -n 'Hello World!'",
        ),
        VMTest(
            "Sudo test",
            sudo_cmd("echo -n 'Hello World!'"),
        )
]

class Mallet(VM):
    def __init__(self):
        VM.__init__(self, "mallet", MALLET_PORT, MALLET_LOGIN, MALLET_PASSWORD, 
                MALLET_TESTS)
