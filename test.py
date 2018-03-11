class Test(object):
    def f1(self):
        self.x = "hello"
    def f2(self):
        print self.x+" world"
t = Test()
t.f2()
