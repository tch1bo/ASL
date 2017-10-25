import paramiko
import socket

INIT_ERR_MSG = """\
An exception occured when connecting to "localhost:{0}" with username="{1}"
and password="{2}". Exception message:"{3}".\
"""

# wraps a command to execute with sudo
def sudo_cmd(cmd):
    return "sudo -S -p '' " + cmd

class ExecResult:
    """ Represents the result of a command execution on the VM

    Attributes:
        success(bool) : true if the command was executed, false otherwise
        error(string) : a string representation of an exception (if it occurred)
        stdout(string): the contents of stdout stream
        stderr(string): the contents of stderr stream
    """
    def __init__(self, success, error=None, stdout=None, stderr=None):
        self.success = success
        self.error = error
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return 'Success={0} error="{1}" stdout="{2}" stderr="{3}"'.format(
                self.success, self.error, self.stdout, self.stderr)

class SSHClient:
    client = None

    def __init__(self, port, username, password):
        self.port = port
        self.username = username
        self.password = password
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        try:
            self.client.connect("localhost", port=port, look_for_keys=False,
                    password=password, username=username)
        except Exception as e:
            print INIT_ERR_MSG.format(port, username, password, e)
            self.client = None

    def connection_is_set(self):
        return self.client is not None

    def exec_command(self, cmd, timeout):
        sudo = "sudo" in cmd
        if not self.connection_is_set():
            return ExecResult(False, error="Connection is not set")
        try:
            stdin, stdout, stderr = self.client.exec_command(cmd, 
                    timeout=timeout)
            if sudo:
                stdin.write(self.password + "\n")
                stdin.flush()
            return ExecResult(True, stdout=stdout.read(), stderr=stderr.read())
        except Exception as e:
            return ExecResult(False, error=str(e))



    def close(self):
        if self.connection_is_set():
            self.client.close()


