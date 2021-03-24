def get_list(nfichero):
    dic = dict()
    f = open(nfichero, mode="rt", encoding="utf-8")
    if(f.read() != ""):
        i = 0
        f = open(nfichero, mode="rt", encoding="utf-8")
        for linea in f:
            while i < 20:
                if i == linea.__len__():
                    dic_aux = {i: linea}
                    dic.update(dic_aux)
                i = i +1
            i = 0
    else:
        raise ValueError("Fichero vacio")
    f.close()
    return dic





try:
    res = get_list("readme.txt")
    print(res)
except ValueError as err:
    print(err)
