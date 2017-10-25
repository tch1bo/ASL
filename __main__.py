from alice import Alice
from bob import Bob
from mallet import Mallet

if __name__ == "__main__":
    alice = Alice()
    mallet = Mallet()
    bob = Bob()
    vms = [
            alice,
            mallet,
            bob,
            ]
    for vm in vms:
        vm.run_tests()
    # print "Don't forget to run the manual tests:"
    # for vm in vms:
    #     print vm.name
    #     if getattr(vm, "manual_tests"):
    #         for i, t in enumerate(vm.manual_tests):
    #             print "{0}. {1}".format(i, t)
    #     print '-' * 80
