from vm import VM, VMTest, VMTestPackageInstalled
from vm import stderr_predicate_factory, stdout_predicate_factory
from ssh import sudo_cmd

MALLET_PORT = 2226
MALLET_LOGIN = "mallet"
MALLET_PASSWORD = "mallet"
MALLET_ONLINE_TESTS = [
        VMTest(
            "Hello world",
            "echo -n 'Hello World!'",
        ),
        VMTest(
            "Sudo",
            sudo_cmd("echo -n 'Hello World!'"),
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
            "Page 33: nmap -sU -p 52,53 alice",
            sudo_cmd("nmap -sU -p 52,53 alice"),
            predicate=stdout_predicate_factory("52/udp", "53/udp"),
            timeout=2,
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

MALLET_PACKAGES = ["tcpdump", "nmap", "telnet -h", "nc", "openvas-client",
        "msfconsole -h", "xtv", "xwatchwin", "xlsclients", "xkill", "vinagre",
]
MALLET_INSTALLATION_TESTS = [
        VMTest(
            "echod_exploit.py",
            "ls ~/Exploits/Echo\ Daemon",
            predicate=lambda o, e: "echod_exploit.py" in o and len(e) == 0,
        ),
]
for p in MALLET_PACKAGES:
    MALLET_INSTALLATION_TESTS += [VMTestPackageInstalled(p)]

class Mallet(VM):
    def __init__(self):
        VM.__init__(self, "mallet", MALLET_PORT, MALLET_LOGIN, MALLET_PASSWORD)
        self.manual_tests = MALLET_MANUAL_TESTS
        self.online_tests = MALLET_ONLINE_TESTS
        self.installation_tests = MALLET_INSTALLATION_TESTS
