import copy


# function for search nestedlist
def search_lst(lis, nes_list, miss, index_list):
    for i in range(len(lis)):

        if lis[i] == miss:
            found = copy.deepcopy(nes_list)
            found.append(i)
            index_list.append(found)

        # if we found another list call this function again
        if lis[i] != miss and type(lis[i]) == list:
            nes_list.append(i)
            search_lst(lis[i], nes_list, miss, index_list)
        if lis[i] != miss and type(lis[i]) == str:
            count = 0
            if miss in lis[i]:
                nes_list.append(i)
                for j in lis[i]:
                    if j == miss:
                        found = copy.deepcopy(nes_list)
                        found.append(count)
                        index_list.append(found)
                    count += 1
        if i == len(lis) - 1:
            nes_list.pop()
    return index_list


# find all places input_list[1] appear in input_list[0]
def findallindex(input_list):
    index_list = []
    miss = input_list[-1]
    lis = input_list[0]
    input_list.pop(-1)

    for i in range(len(lis)):
        # if we found the item add the index to the index list
        if lis[i] == miss:
            index_list.append([i])
        # if we found list, search inside
        if lis[i] != miss and type(lis[i]) == list:
            # nested list indexes
            nes_list = [i]
            search_lst(lis[i], nes_list, miss, index_list)
        if lis[i] != miss and type(lis[i]) == str:
            count = 0
            st = []
            if miss in lis[i]:
                st.append(i)
                for j in lis[i]:
                    if j == miss:
                        st.append(count)
                    count += 1
                index_list.append(st)



    return index_list


# running examples
if __name__ == '__main__':
    A = [[[[1, 2, 3, [0, 1, 2]], 2, [1, 3]], [1, 2, 3]], 2]
    print(findallindex(A))

    B = [[[[1, 2, 3, [0, 1, 2]], 2, [1, 3]], [1, 2, 3]], [1, 3]]
    print(findallindex(B))

    C = [[['ee',['ae']], 'eer','e'],'e']
    print(findallindex(C))
