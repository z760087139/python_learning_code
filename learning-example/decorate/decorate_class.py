import decorate_main
class test_class(object):
    @decorate_main.write_log()
    def func(self,a,b,c):
        print '%s,%s,%s' % (a,b,c)

    def test3(self,a,b,c):
            print 'test3:%s,%s,%s' % (a,b,c) 

    def test(self,a,b,c):
        print 'test:%s,%s,%s' % (a,b,c) 
        @decorate_main.write_log(a,b,c)
        def test2(a,b,c):       
            self.test3(a,b,c)
        test2(a,b,c)
a = test_class()
a.test('a','b','c')