from color import color_red, color_green
from ssh import SSHClient

def default_test_predicate(out, err):
    return (len(err) == 0)

class VMTest:
    """ Represents a test case to run on the VM.

    Attributes:
        name(string): the name, which will be displayed in tests output
        cmd(string) : a command to run on the VM
        predicate(func(stdout, stderr)->bool): a function, which returns
            true if test succeeded and false otherwise
    """
    def __init__(self, name, cmd, predicate=None):
        self.name = name
        self.cmd = cmd
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


class VM:
    def __init__(self, name, port, username, password, tests):
        self.client = SSHClient(port, username, password)
        self.tests = tests
        self.name = name

    def run_tests(self):
        print "Running tests for VM: {0}".format(self.name)
        for t in self.tests:
            res = self.client.exec_command(t.cmd)
            print t.format_result(res)
        print "-"*80

