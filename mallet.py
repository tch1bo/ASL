from vm import VM, VMTest, stderr_predicate_factory, stdout_predicate_factory
from ssh import sudo_cmd

MALLET_PORT = 2226
MALLET_LOGIN = "mallet"
MALLET_PASSWORD = "mallet"
MALLET_TESTS = [
        VMTest(
            "Hello world",
            "echo -n 'Hello World!'",
        ),
        VMTest(
            "Sudo",
            sudo_cmd("echo -n 'Hello World!'"),
        ),
        VMTest(
            "Page 32: tcpdump installed",
            "tcpdump -h",
            predicate=lambda o, e: len(e) != 0
        ),
        VMTest(
            "Page 32: nmap installed",
            "nmap -h",
        ),
        VMTest(
            "Page 32: nmap alice",
            "nmap alice",
            predicate=stdout_predicate_factory("443/tcp")
        ),
        VMTest(
            "Page 32: nmap alice -v -p 22,24 alice",
            "nmap -v -p 22,24 alice",
            predicate=stdout_predicate_factory("22/tcp", "24/tcp")
        ),
        VMTest(
            "Page 32: sudo nmap -sX -v -p 22,24 alice",
            sudo_cmd("nmap -sX -v -p 22,24 alice"),
            predicate=stdout_predicate_factory("22/tcp", "24/tcp"),
            timeout=3,
        ),
        VMTest(
            "Page 33: telnet installed",
            "telnet -h",
            predicate=stderr_predicate_factory("Usage")
        ),
        VMTest(
            "Page 33: nc installed",
            "nc -h",
            predicate=stderr_predicate_factory("usage")
        ),
        VMTest(
            "Page 33: nmap -sU -p 52,53 alice",
            sudo_cmd("nmap -sU -p 52,53 alice"),
            predicate=stdout_predicate_factory("52/udp", "53/udp"),
            timeout=2,
        ),
        VMTest(
            "Page 34: openvas-client installed",
            "openvas-client -h",
            predicate=stdout_predicate_factory("Usage"),
        ),
        VMTest(
            "Page 35: msfconsole installed",
            "msfconsole -h",
            predicate=stdout_predicate_factory("Usage"),
        ),
        VMTest(
            "Page 36: echod_exploit.py installed",
            "ls ~/Exploits/Echo\ Daemon",
            predicate=lambda o, e: "echod_exploit.py" in o and len(e) == 0,
        ),
        VMTest(
            "Page 37: xtv installed",
            "xtv",
            predicate=stderr_predicate_factory("Error", "display")
        ),
        VMTest(
            "Page 37: xwatchwin installed",
            "xwatchwin",
            predicate=stderr_predicate_factory("xwatchwin", "Usage")
        ),
        VMTest(
            "Page 37: xlsclients installed",
            "xlsclients",
            predicate=stderr_predicate_factory("xlsclients", "unable")
        ),
        VMTest(
            "Page 37: xkill installed",
            "xkill",
            predicate=stderr_predicate_factory("xkill", "unable")
        ),
        VMTest(
            "Page 37: vinagre installed",
            "vinagre --help",
            predicate=stdout_predicate_factory("vinagre", "Usage")
        ),
        VMTest(
            "Page 43: nmap -sV -sU -p 2049 alice",
            sudo_cmd("nmap -sV -sU -p 2049 alice"),
            predicate=stdout_predicate_factory("2049/udp"),
        ),
]

MALLET_MANUAL_TESTS = [
        "sudo tcpdump host alice",
        "sudo nmap -O -sV -v alice",
        "telnet alice 25",
        "nc alice 25",
        "telnet alice 80",
        "sudo openvasd; openvas-client", # perform this one with GUI
        "telnet bob 12345",
        "metasploit exercise page 35",
        "echod_exploit.py page 36",
        "xtv, xwatchwin, xlsclients, xkill, vinagre page 37",
        "exercise page 43",
]

class Mallet(VM):
    def __init__(self):
        VM.__init__(self, "mallet", MALLET_PORT, MALLET_LOGIN, MALLET_PASSWORD, 
                MALLET_TESTS)
        self.manual_tests = MALLET_MANUAL_TESTS
