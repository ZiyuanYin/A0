# CSE 477 A0 Ziyuan Yin 
import sys
def counter(T,P,a:int):
    if len(P)>len(T): #if P>T, return -1
        return -1
    if len(P)<=int(a): #if a is longer than the length of P, return -1
        return 1
    for i in range(len(T)-len(P)):
        count = 0
        cut = T[i:i+len(P)]
        for x in range(len(cut)):
            if cut[x] != P[x]:
                count+=1
        if count<=int(a):
            return i+1
    return -1

if __name__=="__main__":
    with open(sys.argv[1], 'r') as file:
        text = file.read().strip()
    print(counter(text,sys.argv[2],sys.argv[3]))

