'''
isinstance()和type（）的区别
type() 不会认为子类是一种父类类型
isinstance() 会认为子类是一种父类类型
'''

class A:
    pass

class B(A):
    pass

isinstance(A(),A)