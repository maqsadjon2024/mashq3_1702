#14
def parol_kuchli(parol):
    if len(parol) < 8:
        return False
    if not any(c.isdigit() for c in parol):
        return False
    if not any(c.isupper() for c in parol):
        return False
    return True

print(parol_kuchli("Test1234"))

#15
def kalkulyator(a, b, amal):
    if amal == "+":
        return a + b
    elif amal == "-":
        return a - b
    elif amal == "*":
        return a * b
    elif amal == "/":
        return a / b
    else:
        return "Noto‘g‘ri amal"

print(kalkulyator(10, 5, "*"))

#16
def tubmi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(tubmi(29))

#17
def tub_sanash(lst):
    count = 0
    for n in lst:
        if tubmi(n):
            count += 1
    return count

print(tub_sanash([2,3,4,5,6,7,8,11]))

#18
def orta(lst):
    return sum(lst) / len(lst)

print(orta([10,20,30,40]))

#19
def raqam_yigindi(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

print(raqam_yigindi(5832))

#20
def raqam_soni(n):
    return len(str(n))

print(raqam_soni(123456))

#21
def min_top(lst):
    m = lst[0]
    for n in lst:
        if n < m:
            m = n
    return m

print(min_top([5,2,8,1,9]))

#22
def teskari_list(lst):
    new = []
    for i in range(len(lst)-1, -1, -1):
        new.append(lst[i])
    return new

print(teskari_list([1,2,3,4]))

#23
def unique(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

print(unique([1,2,2,3,4,4,5]))
