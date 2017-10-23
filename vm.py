from color import color_red, color_green
from ssh import SSHClient

""" The default predicate used for testing."""
def default_test_predicate(out, err):
    return (len(err) == 0)

""" Factory that build predicates that check that err stream contains all
strings in given list."""
def stderr_predicate_factory(*strings):
    def inner(out, err):
        return reduce(lambda a, b: a and (b in err), strings, True)
    return inner

""" Factory that builds predicates that check that out stream contains all
strings in given list."""
def stdout_predicate_factory(*strings):
    def inner(out, err):
        return reduce(lambda a, b: a and (b in out), strings, True)
    return inner

class VMTest:
    """ Represents a test case to run on the VM.

    Attributes:
        name(string): the name, which will be displayed in tests output
        cmd(string) : a command to run on the VM
        predicate(func(stdout, stderr)->bool): a function, which returns
            true if test succeeded and false otherwise
        timeout(int): the command's timeout in seconds (default: 1)
    """
    def __init__(self, name, cmd, timeout=1, predicate=None):
        self.name = name
        self.cmd = cmd
        self.timeout = timeout
        if predicate is None:
            self.predicate = default_test_predicate
        else:
            self.predicate = predicate

    def is_success(self, res):
        return (res.success and self.predicate(res.stdout, res.stderr))

    def format_result(self, res):
        if self.is_success(res):
            output = "[ {0} ] {1}".format(color_green('PASSED'), self.name)
        else:
            output = """[ {0} ] {1}
            \rCmd    = "{2}"
            \rError  = "{3}"
            \rStdout = "{4}"
            \rStderr = "{5}"
            """.format(color_red("FAILED"), self.name, self.cmd, res.error,
                    res.stdout, res.stderr)
        return output

class VMTestPackageInstalled(VMTest):
    """ Checks if a package is installed on the VM.

    Attributes:
        package(string): the name of the package
    """

    def __init__(self, package):
        name = package + "installed"
        cmd = package
        predicate = lambda o,e: "command not found" not in e
        VMTest.__init__(self, name, cmd, predicate=predicate)

class VM:
    def __init__(self, name, port, username, password, tests):
        self.client = SSHClient(port, username, password)
        self.tests = tests
        self.name = name

    def run_tests(self):
        print "Running tests for VM: {0}".format(self.name)
        for t in self.tests:
            res = self.client.exec_command(t.cmd, t.timeout)
            print t.format_result(res)
        print "-"*80

