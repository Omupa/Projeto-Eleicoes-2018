# -*- coding: latin1 -*-
################################################################################################
import json, os

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Vers�o 1 - Ler arquivos TXT que foram coletados e transforma-los em dicion�rios JSON
######################################################################################################################################################################

######################################################################################################################################################################
#
# Leitura dos arquivos
#
######################################################################################################################################################################
def read_file(file):
    with open(data_dir+"/"+file, 'r') as f:                   # Abre arquivo atual
        with open(output_dir + "/" + file, 'w') as g:         # Abre novo arquivo que ir� receber os dados tratados.
            tweets = f.readlines()                            # Leitura do arquivo atual
            for line in tweets:                               # Para cada linha do arquivo atual
                line = line.split('\\r\\n\"')                 # Separa os tweets de acordo com o Carriage Return e EOF
                for item in line:                             # �ltimo item � ' '. Tem que tratar...
                    if item != '':                            # Tratando final do arquivo aqui!
                        item = item.replace('\"{\\\"created','{\\\"created')
                        item = item.replace('\\\"','\"')
                        item = item.replace('\\\\','\\')
                        item = json.loads(item)               # Converte a string em dicion�rio JSON para testar se est� OK.
                        g.write(json.dumps(item) + "\n")      # Salva o dicion�rio no novo arquivo.
                    else:
                        print("Fim do Arquivo!")

######################################################################################################################################################################
#
# M�todo principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
    os.system('clear')
    print ("\n#######################################################################\n")
    i = 0
    for file in os.listdir(data_dir):                          # Para cada arquivo no diret�rio do candidato
        if not os.path.isfile(data_dir+file):
            print ("Imposs�vel ler arquivo: "+str(data_dir+file))
        else:
            read_file(file)                                    # Chama a fun��o para criar o novo arquivo JSON tratado.
            i+=1
    print("Total de arquivos tratados: "+str(i))

    #######################################################################
    print
    print("######################################################################")
    print("Script finalizado!")
    print("######################################################################\n")

######################################################################################################################################################################
#
# IN�CIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
data_dir = "/home/amaury/eleicao/"          ### Substituir "eleicao" pelo nome do diret�rio do candidato
output_dir = "/home/amaury/eleicao_new/"    ### Substituir "eleicao" conforme linha acima e manter o "_new" para criar um novo diret�rio.

#Cria os diret�rios para armazenamento dos novos arquivos
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if __name__ == "__main__": main()