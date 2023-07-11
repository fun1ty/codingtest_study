def digit_sum(x):
    global tmp, dap
    hap=0
    for i in range(len(x)):
        hap+= int(x[i])
    if tmp==0:
        tmp=hap
        dap=x
    if tmp < hap:
        tmp=hap
        dap=x

n=int(input())
arr=list(map(str,input().split()))
tmp=0
dap=0
for i in range(n):
    digit_sum(arr[i])
print(dap)
