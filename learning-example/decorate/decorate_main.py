import os
def write_log(*_tuple,**_dict):
    def get_func(func):
        def to_do(*args,**kwargs):
            try:
                func(*args,**kwargs)
            except Exception,e:
                log = 'logtest.txt'
                with open(log,'a') as file:
                    file.write(str(e))
                    file.write(str(args))
                    file.write(str(kwargs))
                    file.close()
                raise
        return to_do
    return get_func