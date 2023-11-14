#!/usr/bin/env python3


def greet_programmer():
    print ("Hello, programmer!")
    pass


def greet(name):
    print("Hello, " + name + "!")
    pass


def greet_with_default(name="programmer"):
    #print("Hello, " + name + "!", end="\n")
    print("Hello, {}!".format(name))
    pass


def add(num1, num2):
    return num1 + num2
    pass


def halve(number=100):
    return number / 2
    pass

def halve_int(number=100):
    return int(number / 2)
    pass

def halve_float(number=100):
    return float(number / 2)
    pass    

