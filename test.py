class Base(object):
    pass

class M1(object):
    def just_test(self):
        return False

class Main(M1,Base):
    pass

k = Main()
print(k)
assert k.just_test()