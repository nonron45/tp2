def string_Calculator1(n: str)-> int:
    if  n== "":
        return ""

    if ',' in n:
        a, b = n.split(',')
        return int(a) + int(b)
    return int(n)