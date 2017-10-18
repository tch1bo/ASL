from vm import VM, VMTest

ALICE_PORT = 2224
ALICE_LOGIN = "alice"
ALICE_PASSWORD = "alice"
ALICE_TESTS = [
        VMTest(
            "Hello world test",
            "echo -n 'Hello World!'",
        ),
        VMTest(
            "Failing test",
            ">&2 echo -n 'error'",
        )
]

class Alice(VM):
    def __init__(self):
        VM.__init__(self, "alice", ALICE_PORT, ALICE_LOGIN, ALICE_PASSWORD, 
                ALICE_TESTS)
