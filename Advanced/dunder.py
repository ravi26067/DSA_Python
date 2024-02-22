'''
Dunder is represented by __xyz__
'''


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Operator overriding and magic methods

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X:{self.x}, Y:{self.y}"

    # def __len__(self):
    #     return 10

    def __call__(self, *args, **kwargs):
        print("Hello, I was called!")


v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2

print(v3)

# Calling the object
v3()
