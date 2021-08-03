
# Enter four non-negative integers in a list. 
list_num = [10, 9, 21, 1]

# shuffle the list in 4 positions with no repeadted same position
def permutation(list_num):
    list_shuffle = []
    list_all = []
    count1 = 0
    count2 = 0
    for i in range(len(list_num)): # 1st slot: available for 4 possible numbers
        pos1 = list_num[i]
        list_shuffle.append(pos1)
        while count1 < 3:
            for j in range(len(list_num)): # 2nd slot: available for 3 possible remained numbers
                if j != i:
                    pos2 = list_num[j]                
                    list_shuffle.append(pos2)
                    while count2 < 2:
                        for k in range(len(list_num)): # 3d slot: available for 2 possible remained numbers
                            if k != i and k != j:
                                pos3 = list_num[k]
                                list_shuffle.append(pos3)
                                for l in range(len(list_num)): # 4th slot: available for 1 possible remained number
                                    if l != i and l != j and l != k:
                                        pos4 = list_num[l]
                                        list_shuffle.append(pos4)
                                        list_all.append(list_shuffle)                                                                                            
                                        list_shuffle = list_shuffle[:2]
                                        count2 += 1                               
                    count2 = 0
                    list_shuffle = list_shuffle[:1]
                    count1 += 1
        count1 = 0
        list_shuffle = []
    return list_all

permutation_list = permutation(list_num)

# arrange number in each list e.g. [1,2,3,4] => [1234]
list_str3 = []
def arrange_num(list_str3): 
    while len(list_str3) < len(permutation_list):
        str3 = "" 
        for m in range(len(permutation_list)):
            list_m = permutation_list[m]
            for values in list_m:
                str3 += str(values)
                str3_int = int(str3)
            list_str3.append(str3_int)
            str3 = ""
    return list_str3

arrange_list = arrange_num(list_str3)

# get rid of the duplicated number
unique_list = set(arrange_list)
# all number of member in list
#for index, value in enumerate(unique_list):
    #print(index+1, value)
largest_num = max(unique_list)
print(largest_num)