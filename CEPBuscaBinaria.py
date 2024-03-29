import struct
import sys
import time
 
if len(sys.argv) !=2:
    print("USO %s [CEP]" % sys.argv[0])
    quit()
   
#l� a linha inteira quando acha o CEP
def LeituraLinha(Tupla):
    print("\n# Informa��es encontradas!\n")
    for i in range(0,len(Tupla)-1):
        print(str(Tupla[i],'latin1'))
 
 
#monta o Struct para formatar a leitura
registroCEP = struct.Struct("72s72s72s72s2s8s2s")
CepColumn = 5
size = registroCEP.size
#abre o arquivo
f = open("cep_ordenado.dat","rb")
 
f.seek(0,2)
#O index da linha inicial come�a no 0
#O index da linha final come�a na (quantidade de linhas-1)
indexInicio=0
indexFim=(f.tell()/size)-1
 
 
#coloca o leitor pro inicio
f.seek(0)
#le a linha, coloca os valores numa tupla e em seguida extrai o cep
inicio_Linha = f.read(size)
inicio_Tupla = registroCEP.unpack(inicio_Linha)
inicio_CEP = str(inicio_Tupla[CepColumn],'latin1')
 
#coloca o leitor pra �ltima linha
f.seek(int(indexFim*size))
#le a linha, coloca os valores numa tupla e em seguida extrai o cep
fim_Linha = f.read(size)
fim_Tupla = registroCEP.unpack(fim_Linha)
fim_CEP = str(fim_Tupla[CepColumn],'latin1')
 
 
counter = 0
achei=False
 
while (inicio_CEP <= fim_CEP)& achei==False :
    tempo= time.time()
    counter= counter+1
    indexMeio=int((indexInicio+indexFim)/2)
 
    #leitura do meio
    f.seek(int(indexMeio*size))
    meio_Linha = f.read(size)
    meio_Tupla = registroCEP.unpack(meio_Linha)
    meio_CEP= str(meio_Tupla[CepColumn],'latin1')
 
    #testa pra ver se est� no meio
    if meio_CEP == sys.argv[1]:
        LeituraLinha(meio_Tupla)
        achei = True
 
    elif meio_CEP < sys.argv[1]:
 
        indexInicio = indexMeio+1
        f.seek(int(indexInicio*size))
 
        inicio_Linha = f.read(size)
        inicio_Tupla = registroCEP.unpack(inicio_Linha)
        inicio_CEP = str(inicio_Tupla[CepColumn],'latin1')
 
    elif meio_CEP > sys.argv[1]:
 
        indexFim= indexMeio-1
        f.seek(int(indexFim*size))
 
        fim_Linha = f.read(size)
        fim_Tupla = registroCEP.unpack(fim_Linha)
        fim_CEP = str(fim_Tupla[CepColumn],'latin1')
 
print("\nNumero de itera��es: %d " %counter)
tempoT=time.time()-tempo
print("Tempo total: %.2f segundos"%tempoT)