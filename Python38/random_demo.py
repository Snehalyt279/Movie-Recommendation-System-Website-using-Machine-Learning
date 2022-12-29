import random
def sort(l):
    count=0
    print("sorting",1)
    for i in range(1,len(1)):
        x,j=l[i],i-1
        while j>=0 and l[j]>x:
            count+=1
            if l[j] > l[i]:
                l[i]=l[j+1]
            j-=1
        l[j+1]=x
        count+=1
        print("Sorted list",l)
        return l,count

if __name__=='__main__':
    print("Sorting via linear")
    n=40
    sorted_list,count=sort(random.sample(range(n),n))
    print("Runtime = %d for %d"%(count,n))
