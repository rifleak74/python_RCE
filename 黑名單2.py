def make_secure():
    kill = ['open',
              'eval'
              ]
    for func in kill:
        del __builtins__.__dict__[func]


make_secure()

while True:
    try:
        inp = input('> ')
        ret = None
        exec("ret=" + inp)
        if ret != None:
            print(ret)
    except Exception as e:
        print (e)

