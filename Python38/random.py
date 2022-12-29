import random
def sort(l):
  count=0
  print("sorting",l)
  #start sorted list from 0th index
  for i in range(1,len(l)):
    x,j=l[i],i-1
#place where the current item's to be moved, set at its current loc.
    while j>=0 and l[j]>x:
      count+=1 #for the comparison
#    for j in reversed(range(i)): #will go from (0,i-1) in reversed order
      if l[j] > l[i]: #this will increment the counter too
        l[i]=l[j+1] #keep shifting elements to the right
      j-=1
    l[j+1]=x
    count+=1 #for the swap
    print("Sorted list",l)
    return l,count


if __name__=='__main__':
    print("Sorting via linear")
    n=40 #move this show the count's near to n^2
    sorted_list,count=sort(random.sample(range(n),n))
    print("Runtime = %d for %d"%(count,n))
