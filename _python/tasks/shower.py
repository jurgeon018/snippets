N, M = input('Input N and M: ').split(' ')
ways = 0
lst = []
cols = 0
while cols < int(N):
    current = input().split(' ')
    if len(current) != int(M):
        print('amount or symbols must be {}'.format(M))
    else:
        cols += 1
        lst.append(current)
        for el in range(0,int(M)):
            try:
                if current[el] == '.' and current[el+1] == '.':
                    ways += 1
            except IndexError:
                pass

for row_index in range(len(lst)):
    for i in range(len(lst[row_index])):
        try:
            if lst[row_index][i] == '.' and lst[row_index+1][i] == '.':
                ways += 1
        except IndexError:
            pass
print('ways: ',ways)
