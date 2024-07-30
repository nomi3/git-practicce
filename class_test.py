def comment_decorator(comment):
    def decorator(func):
        def wrapper(self):
            print(comment)
            return func(self)

        return wrapper

    return decorator


class Parent:
    comment = "I'm the parent class"

    def __init__(self):
        print("Parent class created")
        self.name = "Parent"  # name attribute added

    @comment_decorator(comment)
    def hello(self):
        self.hello_impl()

    def hello_impl(self):
        print(f"Hello, {self.name}")


class Child(Parent):
    comment = "I'm the child class"

    def __init__(self):
        print("Child class created")
        super().__init__()
        self.name = "Child"

    @comment_decorator(comment)
    def hello(self):
        self.hello_impl()


# Create an instance of Parent and call the hello method
parent = Parent()
parent.hello()

child = Child()
child.hello()
