def across5(a, b):
    assert len(a) > 0 and len(b) > 0
    n = 0
    while len(a) > 0:
        r = True
        i = 1
        while r and i < len(a):
            r = a[:i] in b
            if r:
                i = i + 1

        if i < len(a):
            a = a[i-1:]
        else:
            a = a[1:]
        n = n + 1

    return n

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

print(down2("RBYYYRRBYYYRBBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYRBBRBYYYRBBBBBRYYRYRYRBBRYBRYBBBRYRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBYRYRYRBRYBYYBRBYYYRBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRBRYBBRYBRYBRYBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRBRYBYBBRBRBRBRYBBRYBRYBRYBBRYYRRBYYYRRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYYBBRYBRYBRYBBBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYRBYRYBRYBRYBYRYRYRBRYBYYBRBYYYRBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBRBYYYRBRYBBBBBBRYYRYRYRBRYBYYBBRRBYYBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRBRYBBRYBRYBRYBBRYYRYRYRBRYBYYRBBRBRBRYBBRYBRYBRYBBRBRBRYBBRYBYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRBRYBBRYBRYBRYBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRYYRRBYYYRRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYBBRYBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYBRYBRYB"))
# print(down2("RBYYYRRBYYYRBBBRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBRYRBBRBYYYRBBBBBRYYRYRYRBBRYBRYBBBRYRBYYYRBBBBBRYYRYRYRBRYBYYBBRBRBRYBBR"))


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
