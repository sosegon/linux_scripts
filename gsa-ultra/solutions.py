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
# def down1(n, c):

#     return 1

# f = open("down1.txt", "r")
# i = f.read().split("\n")
# comb = i[1].split()
# print(len(comb))
# print(len(list(set(comb))))
# tupples = ()
# for n in range(len(comb))[::2]:
#     new_tuple = ((comb[n], comb[n+1]),)
#     tupples = tupples + new_tuple

# print(tupples)

# r = down1(i[0], tupples)
# print(r)
