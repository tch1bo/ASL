from vm import VM, VMTest, VMTestPackageInstalled
from vm import stderr_predicate_factory, stdout_predicate_factory
from vm import create_installation_tests

BOB_PORT = 2225
BOB_LOGIN = "bob"
BOB_PASSWORD = "bob"
BOB_ONLINE_TESTS = [
        VMTest(
            "Hello world test",
            "echo -n 'Hello World!'",
        ),
]

BOB_MANUAL_TESTS = [
]

BOB_PACKAGES = [ ]
BOB_FILES = ["/etc/init.d/ssh", "/usr/sbin/sshd", ]

BOB_INSTALLATION_TESTS = create_installation_tests(BOB_PACKAGES, BOB_FILES)
class Bob(VM):
    def __init__(self):
        VM.__init__(self, "bob", BOB_PORT, BOB_LOGIN, BOB_PASSWORD)
        self.manual_tests = BOB_MANUAL_TESTS
        self.online_tests = BOB_ONLINE_TESTS
        self.installation_tests = BOB_INSTALLATION_TESTS
