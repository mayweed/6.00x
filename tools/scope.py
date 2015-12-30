#!/usr/bin/python
# From Python Tut, test scopes 9.2.1
#"You can also see that there was no previous binding for spam before the
#global assignment." I cant get that.. except: everything was local

global spam
spam = "test global"

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
