from vm import VM, VMTest, VMTestPackageInstalled
from vm import stderr_predicate_factory, stdout_predicate_factory
from vm import create_installation_tests

ALICE_PORT = 2224
ALICE_LOGIN = "alice"
ALICE_PASSWORD = "alice"
ALICE_ONLINE_TESTS = [
        VMTest(
            "Hello world test",
            "echo -n 'Hello World!'",
        ),
]

ALICE_MANUAL_TESTS = [
        "Page 37: xhost, xclock",
        "recon page 38",
        "recon page 41",
        "telnetd page 41",
        "ssh exercise page 50",
]

ALICE_PACKAGES = ["xclock", "xhost", "iptables", "ssh", "ssh-keygen -h",
        "ssh-agent -h",]
ALICE_FILES = []
ALICE_INSTALLATION_TESTS = create_installation_tests(ALICE_PACKAGES,
        ALICE_FILES)

class Alice(VM):
    def __init__(self):
        VM.__init__(self, "alice", ALICE_PORT, ALICE_LOGIN, ALICE_PASSWORD)
        self.manual_tests = ALICE_MANUAL_TESTS
        self.online_tests = ALICE_ONLINE_TESTS
        self.installation_tests = ALICE_INSTALLATION_TESTS
