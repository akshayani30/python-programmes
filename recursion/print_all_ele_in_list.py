list=["ak","suman"]
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx],end="")
    print_list(list,idx+1)
print_list(list)