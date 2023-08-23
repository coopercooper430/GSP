def calcSupportOneItem(min_support, *items):
    list_of_candidates = []
    for i in items:
        list_of_candidates.append((i for i in i if (i != '(' and i != ')')))

    set_of_candidates = []
    for i in list_of_candidates:
        set_of_candidates.extend(sorted(set(i)))

    list = []
    for i in set_of_candidates:
        list.extend(i)

    support_of_one_item = {}
    for i in list:
        list.count(i)
        if list.count(i) >= min_support:
            support_of_one_item[i] = list.count(i)

    return support_of_one_item


def generateTwoItemsCandidateSequences(*Sequences):
    ListOfCandidates = []
    for i in Sequences:
        for j in Sequences:
            ListOfCandidates.append(i + j)

    for i in range(0, len(Sequences)):
        for j in range(i + 1, len(Sequences)):
            ListOfCandidates.append('(' + ListOfCandidates[i] + ListOfCandidates[j] + ')')

    return ListOfCandidates


def calculateSupport(min_support: int, items: list[str], list: list[str]) -> dict[str, int]:
    dic = {}
    for item in items:
        dic[item] = 0

        if item[0] == '(':
            for i in list:
                if item in i:
                    dic[item] += 1
            if dic[item] < min_support:
                del dic[item]
        else:
            for i in list:
                n = ''
                y = i
                z = y.find('(')
                #print(z)
                w = y.find(')')
                #print(w)
                for t in range(0, len(item)):
                    x = y.find(item[t])
                    #print(x)
                    if (x > w and w > -1):
                        x = x - w - 1
                        #print(x)
                        y = y[(w + 1):]

                        z = y.find('(')
                        w = y.find(')')
                    if (x != -1):
                        if (x > z and x < w):
                            y = y[(w + 1):]

                            z = y.find('(')
                           # print(z)
                            w = y.find(')')
                           # print(w)
                        else:
                            z -= (x + 1)
                            #print(z)
                            w -= (x + 1)
                            #print(w)
                            y = y[(x + 1):]

                        n += item[t]
                if (n == item):
                    dic[item] += 1
            if dic[item] < min_support:
                del dic[item]
    return dic

def generateKItemsCandidateSequences(list, min_support, *items):
    list = []
    for i in items:
        for j in items:
            if i == j:
                continue
            else:
                if(j[0] == '(' and i[0] != '('):
                    if(j.find(i[1:len(i)]) != -1):
                        list.append(i[0] + j)
                elif(j[0] != '(' and i[0] == '('):
                    if(i[2:(len(i)-1)] == j[0:(len(j)-1)]):
                        list.append(i+j[len(j)-1:])
                elif (j[0] != '(' and i[0] != '('):
                    if (i[1:(len(i))] == j[0:(len(j) - 1)]):
                        list.append(i + j[len(j) - 1:])


    return list


min_s = 2
t1 ="ab(fg)cd"
t2 ="bgd"
t3 ="bfg(ab)"
t4 ="f(ab)cd"
t5 ="a(bc)gf(de)"

print("join1:")
hello = calcSupportOneItem(min_s,t1,t2,t3,t4,t5)
print(hello)
print("join2:")
join_two_items = generateTwoItemsCandidateSequences(*hello)
print("join two items: " + str(join_two_items))
support = calculateSupport(min_s, join_two_items, [t1, t2, t3, t4, t5])
print("frequent 2 sequence: " + str(support))

print("join3:")
joined_items = generateKItemsCandidateSequences( [t1,t2,t3,t4,t5], min_s ,*support)
support_3_more = calculateSupport(min_s,list(joined_items),[t1, t2, t3, t4, t5])

print("joined items 3: ", list(joined_items))
print("support : ",support_3_more)


print("join4:")

joined_items1 = generateKItemsCandidateSequences( [t1,t2,t3,t4,t5], min_s ,*joined_items)
support_3_more1 = calculateSupport(min_s,list(joined_items1),[t1, t2, t3, t4, t5])

print("joined items 4: ", list(joined_items1))
print("support : ",support_3_more1)