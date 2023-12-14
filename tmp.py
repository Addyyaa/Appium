class MyClass:
    @classmethod
    def class_method(cls):
        # 在类方法中定义属性
        cls.class_variable = "Modified in class method"

    def another_method(self):
        # 在其他方法中访问类方法中定义的属性
        MyClass.class_variable = "xxxx"
        print(f"Accessing class variable in another method: {MyClass.class_variable}")

# 直接通过类调用类方法
MyClass.class_method()

# 通过类调用其他方法，访问类方法中定义的属性
obj = MyClass()
obj.another_method()
