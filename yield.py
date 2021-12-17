def running(*args):
    for i in args:
        print(i)

def joy(happy):
    if happy =="positive":
        print("smiling face")
    elif happy =="worried":
        print("unhappy face")
    yield "disys"
    print("live long life")

def smile(worries):
    print("kill the problems with smile")
    worries("good","empty pocket")

 def problems(health,wealth):
     print(health,wealth)

smile(problems)     
