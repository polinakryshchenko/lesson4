class Parent1:
    def __init__(self):
        self.attr1 = "Attribute from Parent1"

    def method1(self):
        return "Method from Parent1"


class Parent2:
    def __init__(self):
        self.attr2 = "Attribute from Parent2"

    def method2(self):
        return "Method from Parent2"


class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        self.attr3 = "Attribute in Child"

    def method3(self):
        return "Method in Child"

obj = Child()

print(obj.attr1)
print(obj.attr2)
print(obj.attr3)
print(obj.method1())
print(obj.method2())
print(obj.method3())