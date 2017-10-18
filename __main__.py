from ssh.alice import Alice

if __name__ == "__main__":
    alice = Alice()
    print "login done"
    print alice.exec_command("ls -l")
    print alice.exec_command("ls -l")
    print alice.exec_command("ls -l")
