def across10(t_n, t_a, t_b, t_x, t_y):
    AliceWon = 0
    i = 0
    while i < len(t_n):
        if play10(t_n[i], t_a[i], t_b[i], t_x[i], t_y[i]):
            AliceWon = AliceWon + 1
        i = i + 1

    return AliceWon + 123

def play10(n, A, B, X, Y):
    removals = [3, 2, 1]
    # Alice starts
    (a, b) = sorted((A, B))
    (x, y) = sorted((X, Y))
    N = n
    turnAlice = True
    while N > 0:
        (c, d) = (a, b) if turnAlice else (x, y)

        index = 0
        toRemove = 0
        while index < len(removals):
            result = N - removals[index]
            if result > 0 and (result % c == 0 or result % d == 0):
                index = index + 1
                continue
            elif result >= 0:
                if result >= c and result >=d:
                    if result % c != 0 and result % d != 0:
                        toRemove = removals[index]
                elif result >= c and result < d:
                    if result % c != 0:
                        toRemove = removals[index]
                else:
                    toRemove = removals[index]
                break

            index = index + 1

        if toRemove == 0:
            return not turnAlice
        else:
            # print("c, d: " + str(c) + ", "+ str(d))
            # print(str(turnAlice) + " : " + str(N) + ", " + str(toRemove))
            N = N - toRemove
            turnAlice = not turnAlice

    return not turnAlice

# print(play10(23, 4, 5, 3, 6))
# print(play10(12, 2, 3, 6, 15))
# print(play10(37, 4, 5, 4, 5))
# print(play10(79, 6, 6, 6, 6))
# print(play10(20, 3, 16, 7, 8))

# f = open("across10.txt", "r")
# rows = f.read().split("\n")
# n = ()
# a = ()
# b = ()
# x = ()
# y = ()
# for r in rows:
#     vals = r.split(",")
#     n = n + (int(vals[0]),)
#     a = a + (int(vals[1]),)
#     b = b + (int(vals[2]),)
#     x = x + (int(vals[3]),)
#     y = y + (int(vals[4]),)

# print(across10(n, a, b, x, y))


def down4(l, r):
    n = r
    fibos = base_fibonacci(n)
    N = 0
    while n >= l:
        if len(valid_fibos(fibos, n)) <= 0:
            N = N + 1
        n = n - 1

    return N

def valid_fibos(fibos, N):
    # remove unneeded fibos
    n = 0
    valid = []
    while n < len(fibos):
        if N % fibos[n] == 0:
            valid.append(fibos[n])

        n = n + 1

    return valid

def base_fibonacci(n):
    prev = 1
    fibo = 2 # omit 1,1 since any power is 1
    fibos = []
    fibos.append(fibo)
    while fibo <= n:
        temp = fibo
        fibo = fibo + prev
        fibos.append(fibo)
        prev = temp

    return fibos[:-1]

# print(base_fibonacci(123456))
# print(valid_fibos(base_fibonacci(123456), 123456))
# print(valid_fibos(base_fibonacci(654321), 654321))
# print(valid_fibos(base_fibonacci(1000), 288))
# print(down4(123456, 654321))

def down1(n, c):

    # number of pairs not in range
    N = 0
    for t in c:
        if t[0] > n or t[1] > n:
            N = N + 1

    e = len(c) - N
    return 2**e % (10**9 + 7)

# f = open("down1.txt", "r")
# i = f.read().split("\n")
# comb = i[1].split()
# print(len(comb))
# print(len(list(set(comb))))
# tupples = ()
# for n in range(len(comb))[::2]:
#     new_tuple = ((int(comb[n]), int(comb[n+1])),)
#     tupples = tupples + new_tuple

# r = down1(i[0], tupples)
# print(r)

def down8(n, m, r, c, k):
    w = [x - c[i - 1] - 1 for i, x in enumerate(c)][1:] # widhts
    h = [x - r[i - 1] - 1 for i, x in enumerate(r)][1:] # heights

    w = [c[0] - 1] + w + [m - c[-1] - 0]
    h = [r[0] - 1] + h + [n - r[-1] - 0]

    w = sorted(w)
    h = sorted(h)

    # print(w)
    # print(h)

    if k == 0:
        return None

    M = len(w) - 1 # horizontal limit
    N = len(h) - 1 # vertical limit

    s = w[0] * h[0] # area
    C = 1 # counter
    #areas = []
    #areas.append(s)

    Hi = 1
    Hj = 0
    Vi = 0
    Vj = 1

    H = h[Hj] * w[Hi]
    V = h[Vj] * w[Vi]

    while C < k:
        # print("\n")
        # print("H: "+ str(H))
        # print("V: "+ str(V))
        # print("Vi, Vj: " + str(Vi) + ", " + str(Vj))
        # print("Hi, Hj: " + str(Hi) + ", " + str(Hj))

        if H is None or V is None:
            if V is not None:
                s = V
                #areas.append(s)
                V = None
                C = C + 1
                continue
            elif H is not None:
                s = H
                #areas.append(s)
                H = None
                C = C + 1
                continue
            else:
                break

        if H <= V:
            s = H
            if not Hi + 1 < M:
                Hi = Vi + 1
                Hj = Hj + 1
            else:
                Hi = Hi + 1

            if Hi < M and Hj < N:
                H = h[Hj] * w[Hi]
            else:
                H = None
        else:
            s = V
            if not Vj + 1 < N:
                Vj = Hj + 1
                Vi = Vi + 1
            else:
                Vj = Vj + 1

            if Vi < M and Vj < N:
                V = h[Vj] * w[Vi]
            else:
                V = None

        C = C + 1
        #areas.append(s)

    return s


# a = down8(50, 50, (1,7,12,15,21,23), (1,7,11,14,24,31), 5)
# print(a)
# for i in range(37):
#     a = down8(50, 50, (1,10,16,18,28,39), (1,6,10,13,19,26), i)
#     print(a)

# f = open("down8.txt", "r")
# v = f.read().split("\n")
# dim = v[0].split()
# n = int(dim[0])
# m = int(dim[1])
# k = int(v[3])
# r = tuple(map(int, v[1].split()))
# c = tuple(map(int, v[2].split()))
# a = down8(n, m, r, c, k)
# print(a)

def down88(n, m, r, c, k):
    w = sorted([x - c[i - 1] for i, x in enumerate(c)][1:]) # widhts
    h = sorted([x - r[i - 1] for i, x in enumerate(r)][1:]) # heights

    n = n - 1
    m = m - 1
    N = 1
    visited = []
    pending = []
    area = w[0] * h[0]
    areas = []
    areas.append(w[0] * h[0])
    my_area = 0
    i = 0
    j = 0

    assert k <= (m)*(n)

    while N < k or (j < n - 1 or i < m - 1):
        left = None
        right = None
        hasLeft = j < n - 1 and i < m
        hasRight = j < n and i < m - 1

        if hasLeft :
            if isVisited(visited, i, j+1): # left already visited
                j = j + 1
                continue

        if hasRight:
            if isVisited(visited, i+1, j): # right already visited
                i = i + 1
                continue

        left_right = []
        if hasRight:
            right = w[i+1] * h[j]
            visited = visited + [[i+1, j]]
            left_right.append(right)

        if hasLeft:
            left = w[i] * h[j+1]
            visited = visited + [[i, j+1]]
            left_right.append(left)

        if len(pending) > 0:
            last = pending[-1]
            if len(left_right) == 0:
                # remove as needed
                while N < k:
                    pending = pending[:-1]
                    #visited = removeVisited(visited, last[1], last[2])
                    # print("\nremove")
                    # print(pending)
                    areas.append(last[0])
                    my_area = last[0]

                    N = N + 1
                    if len(pending) > 0:
                        last = pending[-1]
                    else:
                        break

            else:
                while last[0] < min(left_right) and last[0] < max(left_right) and N < k:
                    il = last[1] + 1
                    jl = last[2]
                    if jl < n and il < m:
                        if not isVisited(visited, il, jl):
                            area = w[il] * h[jl]
                            pending = add_pending(pending, (area, il, jl))
                            # print("\nsub right")
                            # print(pending)
                            visited = visited + [[il, jl]]

                    il = last[1]
                    jl = last[2] + 1
                    if jl < n and il < m:
                        if not isVisited(visited, il, jl):
                            area = w[il] * h[jl]
                            pending = add_pending(pending, (area, il, jl))
                            # print("\nsub left")
                            # print(pending)
                            visited = visited + [[il, jl]]

                    pending = pending[:-1]
                    #visited = removeVisited(visited, last[1], last[2])
                    # print("\nremove")
                    # print(pending)
                    areas.append(last[0])
                    my_area = last[0]

                    N = N + 1
                    if len(pending) > 0:
                        last = pending[-1]
                    else:
                        break

        if N >= k:
            break

        if hasLeft and hasRight:
            if right <= left:
                pending = add_pending(pending, (left, i, j+1))
                # print("\nleft")
                # print(pending)
                i = i + 1
                areas.append(right)
                my_area = right
            else:
                pending = add_pending(pending, (right, i+1, j))
                # print("\nright")
                # print(pending)
                j = j + 1
                areas.append(left)
                my_area = left
            N = N + 1
        elif hasLeft:
            pending = add_pending(pending, (left, i, j+1))
            # print("\nleft")
            # print(pending)
            j = j + 1
        elif hasRight:
            pending = add_pending(pending, (right, i+1, j))
            # print("\nright")
            # print(pending)
            i = i + 1

    return areas

def removeVisited(visited, i, j):
    if len(visited) == 0:
        return []
    else:
        index = 0
        while index < len(visited):
            current = visited[index]
            if current[0] == i and current[1] == j:
                visited = visited[:index] + visited[:index+1]
                break

            index = index + 1

    return visited

def isVisited(visited, i, j):
    if len(visited) == 0:
        return False
    else:
        index = 0
        while index < len(visited):
            current = visited[index]
            if current[0] == i and current[1] == j:
                return True

            index = index + 1

    return False

def add_pending(listed, elem):
    inserted = False

    if len(listed) == 0:
        listed.append(elem)
    else:
        index = 0
        while index < len(listed):
            if listed[index][0] > elem[0]:
                index = index + 1
            else:
                break

        listed = listed[:index] + [elem] + listed[index:]

    return listed


# f = open("down8.txt", "r")
# v = f.read().split("\n")
# dim = v[0].split()
# n = int(dim[0])
# m = int(dim[1])
# k = int(v[3])
# r = tuple(map(int, v[1].split()))
# c = tuple(map(int, v[2].split()))
# a = down8(n, m, r, c, 5000)
# print(a)




def across12(n, x, r):
    assert n == len(x) and n == len(r)

    X = list(x)
    R = list(r)

    XR = []
    for xx, rr in zip(X, R):
        XR.append([xx, rr])

    XR = sorted(XR, key=lambda x:x[1], reverse=True) # sort by power
    ex = [0] * n
    order = [0] * n
    own = [0] * n
    n = 0

    index1 = 0
    while index1 < len(XR):
        if ex[index1] == 1:
            index1 = index1 + 1
            continue

        p1 = XR[index1][0]
        r1 = XR[index1][1]
        min1 = p1 - r1 # min limit to influence others
        max1 = p1 + r1 # max limit to influence others
        ex[index1] = 1
        order[index1] = ex.count(1)
        own[index1] =  1
        n = n + 1

        if ex.count(0) == 0:
            break

        QP = XR[index1 + 1:]
        index2 = 0

        while index2 < len(QP):
            if ex[index1 + 1 + index2] == 1:
                index2 = index2 + 2
                continue

            p2 = QP[index2][0]
            r2 = QP[index2][1]
            min2 = p2 - r2 # min limit to influence others
            max2 = p2 + r2 # max limit to influence others
            #print("min: " + str(min1) + " max: " + str(max1) + " p2: " + str(p2))

            ####################
            # Verify if element is affected by influence
            if p2 >= min1 and p2 <= max1:
                ex[index1 + 1 + index2] = 1
                order[index1 + 1 + index2] = ex.count(1)

                max1 = max2 if max2 > max1 else max1
                min1 = min2 if min2 < min1 else min1
            ####################

            index2 = index2 + 1

        index1 = index1 + 1


    #print(n)
    #print(XR)
    #print(own)
    return n * 10000

# print(across12(10, (9,2,21,4,11,50,29,3,5,20), (1,1,9,2,1,10,3,3,2,5)))

def down11(a):
    assert a >= 100 and a <= 10000

    n = 0
    next_I = 10

    while next_I <= a:
        s = str(next_I)
        index = 0
        l = len(s)

        while index < l:
            ss = s[:index] + s[index+1:]
            si = int(ss)

            # is it square?
            sq = int(str(si**.5).split('.')[1])
            if sq == 0:
                n = n + 1
                # print(s + "---" + ss + " YES")
                break
            # else:
            #     print(s + "---" + ss + " NO")

            index = index + 1

        next_I = next_I + 1

    return n

# print(down11(1234))

def across5(a, b):
    assert len(a) > 0 and len(b) > 0
    n = 0
    index = 0
    bb = b
    while index < len(a):
        char = a[index]
        index_in_b = bb.find(char)

        if index_in_b >= 0:
            bb = bb[index_in_b + 1:]
            index = index + 1
        else:
            n = n + 1
            bb = b

    return n + 1


# f = open("across5.txt")
# ab = f.read().split()
# print(across5("abcdef", "bcdahalremf"))
# print(across5(ab[0], ab[1]))

def down2(s):
    s_right = s # removing chars from right
    n = 0

    while len(s_right) >= 3:
        s_left = s_right # removing chars from left
        hasRYB = True
        while len(s_left) >= 3:
            hasRYB = len(set(s_left)) == 3
            if hasRYB is not True:
                break

            lR = s_left.count("R")
            lY = s_left.count("Y")
            lB = s_left.count("B")

            if lR != lY and lY != lB and lB != lR:
                n = n + 1
                # print(s_left)

            # reduce one char from left
            #print("L: " + s_left)
            s_left = s_left[:-1]


        # reduce one char from right
        #print("R:" + s_right)
        s_right = s_right[1:]

    return n + 10000

#print(down2("RBYYYRRBYYYRBBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYRBBRBYYYRBBBBBRYYRYRYRBBRYBRYBBBRYRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBYRYRYRBRYBYYBRBYYYRBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRBRYBBRYBRYBRYBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRBRYBYBBRBRBRBRYBBRYBRYBRYBBRYYRRBYYYRRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYYBBRYBRYBRYBBBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYRBYRYBRYBRYBYRYRYRBRYBYYBRBYYYRBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBRBYYYRBRYBBBBBBRYYRYRYRBRYBYYBBRRBYYBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRBRYBBRYBRYBRYBBRYYRYRYRBRYBYYRBBRBRBRYBBRYBRYBRYBBRBRBRYBBRYBYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRBRYBBRYBRYBRYBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRYYRRBYYYRRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRYBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYB"))

def down3(s):
    assert len(s) >= 4

    l = len(s)
    index = 2
    s_left = s[:index]
    s_right = s[index:]

    costs = []

    while index <= l - 2:
        l1 = len(s_left)
        index1 = 1
        s_left_left = s_left[:index1]
        s_left_right = s_left[index1:]

        while index1 <= l1 - 1:
            a = longest_palindrome(s_left_left)
            b = longest_palindrome(s_left_right)
            l2 = len(s_right)
            index2 = 1
            s_right_left = s_right[:index2]
            s_right_right = s_right[index2:]

            while index2 <= l2 - 1:
                c = longest_palindrome(s_right_left)
                d = longest_palindrome(s_right_right)
                # print(d)
                # print(s_left_left + "|" + s_left_right + "|" + s_right_left + "|" + s_right_right)
                cos = a + b + c + d
                costs.append(cos)
                # print(cos)
                #print("\n")

                index2 = index2 + 1
                s_right_left = s_right[:index2]
                s_right_right = s_right[index2:]

            index1 = index1 + 1
            s_left_left = s_left[:index1]
            s_left_right = s_left[index1:]

        index = index + 1
        s_left = s[:index]
        s_right = s[index:]

    costs_sorted = sorted(costs)
    return costs_sorted[0]

def longest_palindrome(s):
    la = s.count("a")
    lb = s.count("b")
    lc = s.count("c")
    ld = s.count("d")
    le = s.count("e")
    lf = s.count("f")
    lg = s.count("g")

    l = []
    if la > 0:
        l.append(la)
    if lb > 0:
        l.append(lb)
    if lc > 0:
        l.append(lc)
    if ld > 0:
        l.append(ld)
    if le > 0:
        l.append(le)
    if lf > 0:
        l.append(lf)
    if lg > 0:
        l.append(lg)

    if len(set(l)) == 1 and l[0] == 1:
        return 1

    l = [la, lb, lc, ld, le, lf, lg]
    s = sorted(l, reverse=True)
    highest = s[0]

    s = s[1:]
    h = []
    for e in s:
        if e == 1:
            h.append(e)
        else:
            h.append(e - e % 2)

    return highest + sum(h)

# print(down3("abccaa"))

# r = down3("aabbbbbbbaabbaaaabbbabbbaaabbabbaaaaabbaaaaababbaaaaabaabbbaabaaabaababbbaaaaaabaaabbaaababaababbbaabbbbaabbbaaaaaaaaababbbbbaabbbabbabababbaaabaabababbbaabbbaabaaabbbaabbbabbbabbabaabbabababbbabbaabb")
# print(r)



# def across7():

#     dictionary =

#     c = "Commercial in side or front of building."
#     ws = c.split()

#     r1 = 1
#     for w in ws:
#         r2 = 0
#         for l in w:
#             val = hex(ord(l))
#             r2 = r2 + int(val, 16)

#         r1 = r1 * r2

#     return r1

# def down3(s):
#     # count number of sequences of same char
#     n = 0
#     indices = []
#     lengths = []
#     j = 0
#     while len(s) > 0:
#         i = 0
#         r = True
#         while r and i < len(s):
#             i = i + 1
#             j = j + 1
#             r = len(set(s[:i])) <= 1

#         lengths.append(len(s[:i-1]))
#         s = s[i - 1:]
#         n = n + 1
#         j = j - 1
#         indices.append(j - 1)

#         if(len(set(s)) <= 1):
#             indices.append(j)
#             lengths.append(len(s))
#             n = n + 1
#             break

#     even_odd = []
#     for l in lengths:
#         if l % 2 == 0:
#             even_odd.append(0)
#         else:
#             even_odd.append(1)
#     return even_odd

# r = down3("aabbbbbbbaabbaaaabbbabbbaaabbabbaaaaabbaaaaababbaaaaabaabbbaabaaabaababbbaaaaaabaaabbaaababaababbbaabbbbaabbbaaaaaaaaababbbbbaabbbabbabababbaaabaabababbbaabbbaabaaabbbaabbbabbbabbabaabbabababbbabbaabb")
# # r = down3("wwwewewerrrrrrrrrrrr")
# print("\n")
# print(r)

