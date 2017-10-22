from vm import VM, VMTest, stderr_predicate_factory, stdout_predicate_factory

ALICE_PORT = 2224
ALICE_LOGIN = "alice"
ALICE_PASSWORD = "alice"
ALICE_TESTS = [
        VMTest(
            "Hello world test",
            "echo -n 'Hello World!'",
        ),
        VMTest(
            "Page 37: xhost installed test",
            "xhost",
            predicate=stderr_predicate_factory("xhost", "unable", "display")
        ),
        VMTest(
            "Page 37: xclock installed test",
            "xclock",
            predicate=stderr_predicate_factory("Error", "display")
        ),
        VMTest(
            "Page 43: iptables installed test",
            "iptables --help",
            predicate=stdout_predicate_factory("Usage", "iptables")
        ),
]

ALICE_MANUAL_TESTS = [
        "Page 37: xhost, xclock",
        "recon page 38",
        "recon page 41",
        "telnetd page 41",
]

class Alice(VM):
    def __init__(self):
        VM.__init__(self, "alice", ALICE_PORT, ALICE_LOGIN, ALICE_PASSWORD, 
                ALICE_TESTS)
        self.manual_tests = ALICE_MANUAL_TESTS
