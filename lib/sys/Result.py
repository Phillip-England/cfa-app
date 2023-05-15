# this is a really cool class and has system-wide impact on the way our api functions
# every function or method in our entire program will return a result
# the result will contain one of three things

# 1. It will contain a value
# 2. It will contain an error
# 3. It will contain nothing

# we extract one of the above values by calling .unwrap(some_exception)
# where "some_exception" is an exception we wish to execute if an error is present in our Result
# here is the key to the result, it is always handled AFTER FUNCTION EXECUTION
# this means a funtion can trigger an error, and you can deal with it later when you feel like it.
# this allows all errors in your application to be dynamic.


class Result:
    def __init__(self):
        self.contains_err = None
        self.value = None

    def err(self):
        self.contains_err = True
        return self

    def wrap(self, value: any):
        self.value = value
        return self

    def unwrap(self, some_exception):
        if self.contains_err != None:
            raise some_exception
        if self.value != None:
            return self.value
        return None
