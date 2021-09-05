def printOP(s):
    Dict = dict({})
    for c in s:
        if c in Dict.keys():
            Dict[c]+=1
        else:
            Dict[c]=1
    
    Dict = dict(sorted(Dict.items(), key=lambda item: item[1], reverse=True))
    count=0
    thisV=0
    for k,v in Dict.items():
        if(count==3): break
        elif(v==thisV): continue
        list1=[k1 for k1,v1 in Dict.items() if v1 == v]
        if(len(list1)==1):
            print(k+" "+str(v))
            count+=1
        else:
            list2 = sorted(list1)
            for i in list2:
                if(count==3): break
                else:
                    count+=1
                    print(i+" "+str(v))
        thisV=v

if __name__ == '__main__': #pragma: no cover
    s = input()
    printOP(s)
    
    