def max_num(a,b,c):
    return max([a,b,c])

print(max_num(123,122,124))

def mult_list(list):
    if len(list) == 0:
        return 0
    prod = list[0]

    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i

    return prod

print(mult_list([123,122,124]))

# should be 1,860,744

def rev_string(string_name):
    return string_name[::-1]

print(rev_string("these are words"))
print(rev_string("racecar"))

def num_within(z,b,c):
    return z in range(b,c+1)

print(num_within(122,123,124))

# absolutely couldn't do this one without using the solution as a guide. brain did not click on this one
triangle = [[1],[1,1]]
def pascal(z):
    if z < 1:
        print("no can do")
    elif z == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < z:
            row = []
            row_prev = triangle[row_number -1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else: row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)

pascal(2)
pascal(8)