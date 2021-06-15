mes =["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dex"]
tipo_mes =["","Ground","Figthing","Normal","Steel","Flyng","Psiyhc","Normal","Ground","Flyng","Psiyhc","Figthing","Steel"]
tipo_dia=["","Eletric","Dark","Bug","Fairy","Fire","Ice","Poison","Ghiost","Grass","Water","Rock","Dragon","Eletric","Dark","Bug","Fire","Poison","Rock","Dragon","Fairy","Grass","Ghiost","Water","Ice","Bug","Dark","Ice","","Poison","Dragon","Fairy"]

num_tp = 0;
num_tps = 0;
tipo = ""

imp_mes = input("Digite o Mes: ")
imp_dia = int(input("Digite o Dia: "))

for x in mes :
  num_tp = num_tp+1
  if x == imp_mes:
    tipo = "" + tipo_mes[num_tp] + " "

while num_tps < 31 :
  num_tps = num_tps +1  
  if num_tps == imp_dia:
    tipo= tipo + "" +tipo_dia[num_tps] 
print (tipo)
