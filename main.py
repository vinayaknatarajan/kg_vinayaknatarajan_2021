import sys

def fun(s,t):
    if(len(s) != len(t)):
        return False
    if(len(set(s))>=len(set(t))):
        return True
    else:
        return False

#a = fun(s1,s2)
#print(a)

if __name__ == "__main__":
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    print(fun(s1, s2))