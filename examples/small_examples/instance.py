

class A:
    pass

class B(A):
    pass

class C(A):
    pass

b = B()
c = C()

print(isinstance(b, A))
print(isinstance(b, B))
print(isinstance(b, C))