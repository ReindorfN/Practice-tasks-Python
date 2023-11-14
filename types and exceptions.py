name = "Ama"
if type(name) is str:
    print(name)
else:
    raise Exception("This is an Error")
#print(name)

def name(s) -> str:
    if type(s) is str:
        print(s)
    else:
        raise Exception("This is an Erorr")


print(name(14))
        
#print(type(14))