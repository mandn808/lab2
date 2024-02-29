def compare(n, m, s1, s2):
    return (n.lower().replace('ё', 'е') == s1 and m.lower().replace('ё', 'е') == s2) or (n.lower().replace('ё', 'е') == s2 and m.lower().replace('ё', 'е') == s1)

def newColor(): 
    if compare(n, m, 'синий', 'красный'):
        return 'фиолетовый'
    if compare(n, m, 'красный', 'желтый'):
        return 'оранжевый'
    if compare(n, m, 'синий', 'желтый'):
        return 'зеленый'
    return 'Ничего не получилось'

while True:
    try:
        n, m = map(str, input().split())
    except:
        n, m = False, False

    if n and m:
        print(newColor())
        break

    
