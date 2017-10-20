from alice import Alice
from mallet import Mallet

if __name__ == "__main__":
    alice = Alice()
    mallet = Mallet()
    vms = [
            alice,
            mallet,
            ]
    for vm in vms:
        vm.run_tests()
