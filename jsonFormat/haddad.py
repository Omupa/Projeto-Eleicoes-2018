import json, os, shutil

####################################
# Leitura dos arquivos
####################################

def read_file(file):
    with open(data_dir+"/"+file, 'r') as f:                   # Abre arquivo atual
        with open(output_dir + "/" + file, 'w') as g:         # Abre novo arquivo que ira receber os dados tratados
            tweets = f.readlines()                            # Leitura do arquivo atual
            for line in tweets:                               # Para cada linha do arquivo atual
                line = line.split('\\r\\n\"')                 # Separa os tweets de acordo com o Carriage Return e EOF
                for item in line:                             # Último item ' '. Tem que tratar...
                    if item != '':                            # Tratando final do arquivo aqui!
                        item = item.replace('\"{\\\"created','{\\\"created')
                        item = item.replace('\\\"','\"')
                        item = item.replace('\\\\','\\')
                        try:
                            item = json.loads(item)               # Converte a string em dicionario JSON para testar se está OK.
                            g.write(json.dumps(item) + "\n")      # Salva o dicionario no novo arquivo.
                            print("OK")
                        except:
                            print("Erro no json.dumps()")
                    else:
                        print("Fim do Arquivo!")
                        
########################### main

def main():
    os.system('cls')
    print ("\n####################################################################### inicio\n")
    i = 0
    for file in os.listdir(data_dir):                          # Para cada arquivo no diretorio do candidato
        if not os.path.isfile(data_dir+file):
            print ("Impossivel ler arquivo: "+str(data_dir+file))
        else:
            print(file)
            try:
                read_file(file)                                    # Chama a funcao para criar o novo arquivo JSON tratado
            except:
                print("ERROOOO")
                shutil.copy(data_dir+file, output_dir_erro)
            i+=1
    print("Total de arquivos tratados: "+str(i))

    print("######################################################################")
    print("Script finalizado!")
    print("######################################################################\n")

####################################
# INICIO DO PROGRAMA
####################################

candidato = "haddad"
data_dir = "./data/"+candidato+"/"          # Substituir "eleicao" pelo nome do diretorio do candidato
output_dir = "./data_new/"+candidato+"_new/"    # Substituir "eleicao" conforme linha acima e manter o "_new" para criar um novo diretorio
output_dir_erro = "./data_erro/"+candidato+"_erro"

#Cria os diretorios para armazenamento dos novos arquivos
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(output_dir_erro):
    os.makedirs(output_dir_erro)

if __name__ == "__main__": main()