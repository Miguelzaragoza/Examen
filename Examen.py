from libro import Libro
from autor import Autor
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

def mas_antiguo(lista, año):
    lista_res = list()
    for i in lista:
        if(int(i.año) >= 1900 and int(i.año) <= 2021):
            if(int(i.año) <= int(año)):
                lista_res.append(i.titulo)
        else:
            raise ValueError("Año incorrecto")   
    return lista_res





try:
    res = get_list("readme.txt")
    print(res)
    lista = [Libro(Autor("1", "Isaac", "Asimov"), "Breve historia de la ficica", "2000"), Libro(Autor("2", "Miguel", "Cervantes"), "El Quijote", "1950"), Libro(Autor("3", "Albert", "Einstein"), "Sobre la gravedad", "1980")]
    res1 = mas_antiguo(lista, "1950")
    print(res1)
except ValueError as err:
    print(err)
