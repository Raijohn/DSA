def merging(values,start,mid,end):
    pos1 = start
    pos2 = mid+1
    merg_result=[]
    while pos1 <= mid and pos2 <= end:
        if values[pos1] < values[pos2]:
            merg_result.append(values[pos1])
            pos1 = pos1 + 1
        else:
            merg_result.append(values[pos2])
            pos2 = pos2 + 1
    while pos1 <= mid:
        merg_result.append(values[pos1])
        pos1 = pos1 + 1
    while pos2 <= end:
        merg_result.append(values[pos2])
        pos2 = pos2 + 1
    values[start:end+1] = merg_result

def mergsort(values,start,end):
    if start<end:
        mid = (start+end)//2
        mergsort(values,start,mid)
        mergsort(values,mid+1,end)
        merging(values,start,mid,end)

values = [3,7,2,9,5,6,1,3,0,4,8]
mergsort(values,0,len(values)-1)
print(values)
