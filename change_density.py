'''
change_density.py    
Subrotina para alterar a densidade do material
da geometria


                Autor: Hitalo Rodrigues Mendes
                (hitalo.rm@gmail.com)
                
                Data: 2021/09/21
'''


def change_density(filename,dens):
    file = open(filename)
    lines = file.readlines()
    file.close()
    string = 'Mass density = '+str("{:.8E}".format(dens)) +' g/cm**3\n'
    #print(str("{:E}".format(dens)))
    lines[2] = string
    file = open(filename,'w')
    for line in lines:
        file.write(line)
    file.close()

change_density('run/mat/W.mat',100045)

