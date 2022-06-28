def a():
    n = 3
    print(id(n))
    
    def b():
        # nonlocal n
        print(id(n))
        # n = 3 이렇게 하면 오류남
    b()
    
a()