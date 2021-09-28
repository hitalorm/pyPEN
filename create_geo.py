'''
create_geo.py    
Subrotina para alterar o arquivo de geometria


                Autor: Hitalo Rodrigues Mendes
                (hitalo.rm@gmail.com)
                
                Data: 2021/09/21
'''


def create_geometry_file(filename,thick):
    file = open(filename)
    lines = file.readlines()
    file.close()
    geo_number = thick
    lines[6] = lines[6].replace(lines[6][10:15], str("{0:.3f}".format(thick)))
    file = open('run/box.geo','w')
    for line in lines:
        file.write(line)
    file.close()

create_geometry_file('run/box.geo',2)