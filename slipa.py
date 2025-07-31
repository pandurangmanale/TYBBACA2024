def Remove (duplicate):
    final_list=[]
    for num in duplicate:
        if num not in final_list:
            final_list. append(num)
    return final_list
duplicate=[2,4,6,4,7,2,9,5,1,9,0]
print(Remove(duplicate)) 