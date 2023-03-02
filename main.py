# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Point:

    def __init__(self, x, y):
        self.__x = x
        self._y = y
        self.z = 0

    def get_x(self):
        return self.__x

    def __set_x(self, new_x):
        print("SETTING " + str(new_x))
        self.__x = new_x
        print("SET " + str(self.__x))

    def _set_y(self, new_y):
        print("SETTING " + str(new_y))
        self._y = new_y
        print("SET " + str(self._y))

    def _set_z(self, new_z):
        print("SETTING " + str(new_z))
        self.z = new_z
        print("SET " + str(self.z))

    def __str__(self):
        return "({}, {}, {})".format(self.__x, self._y, self.z)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def bubble(list):
    ordered = False
#    while not ordered:
#        ordered = True
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
 #              ordered = False

    return list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("Geeks : %2d, Portal : %5.2f" % (1, 5.333))
    print("Total students : %3d, Boys : %2d" % (240, 120))
    print("%10.3E" % (356.08977))

    poema = 'Ai que prazer / Nao cumprir um dever, / Ter um livro para ler / E nao fazer! / Ler e maçada, / Estudar é nada. / O Sol doira / Sem literatura / O rio corre, bem ou mal, / Sem edicao original. / E a brisa, essa, / De tao naturalmente matinal, / Como o tempo nao tem pressa...'

    print(poema)

    estrofes = poema.split("/")

    print(estrofes)

    for e in estrofes:
        print(e)

    print("-----")

    print(estrofes[4])
    print(estrofes[5])

    poema = poema + 'Livros sao papeis pintados com tinta. / Estudar é uma coisa em que está indistinta / A distincao entre nada e coisa nenhuma.'

    estrofes = poema.split("/")

    print(estrofes)

    poema2 = poema.replace("/", "\n")

    print(poema2)

    vogais = {"a","e","i","o","u", "A","E","I","O","U"}
    contadores = {}.fromkeys(vogais)
    cnt = 0
    for c in poema:
        if c in vogais:
            cnt += 1
            if (contadores[c] == None):
                contadores[c] = 0
            else:
                contadores[c] = contadores[c] + 1
            print(c)

    print("Vogais: " + str(cnt))
    print(contadores)

    max = 0
    for k,v in contadores.items():
        print(k, str(v))
        if v == None:
           v = 0
        if v == max:
            s = "há vários"
        if v > max:
            s = k
            max = v

    print(s + ": ", str(max))

#    from timeit import default_timer
    import time
    t0 = time.perf_counter()
#    t0 = default_timer()
    print(bubble([8, 1, 6, 3, 9, 5, 4, 10]))
#    duration = default_timer() - t0
    duration = time.perf_counter() - t0

    print(f"Sorted in {duration:0.9f} seconds")

    p = Point(1, 2)

    print(p)

#    p._set_x(3)

#    print(p)

    p._Point__x = 3
    p._y = 3
    p.z = 3

    print(p)

    p.__x = 4

    print(p)

    p._Point__set_x(5)
    p._set_y(5)
    p._set_z(5)

    print(p)

    print(p)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
