import test2
a = test2.test_class()
a.func(1,2,3)

def A(funE_decorated_by_C):
    def redecorated_E(str):
        return funE_decorated_by_C(str)+' > redecorated by A'
    return redecorated_E

def C(funE):
    def decorated_E(str):
        return funE(str)+' > decorated by C'
    return decorated_E

@A
@C
def E(str):
    return str

print E('A string is ')