dict_tipo_mes = {"jan":"Ground","fev":"Figthing","mar":"Normal","abr":"Steel","mai":"Flyng","jun":"Normal","jul":"Psiyhc","ago":"Steel","set":"Figthing","out":"Ground","nov":"Flyng","dez":"Normal"}

tipo_dia=["","Eletric","Dark","Bug","Fairy","Fire","Ice","Poison","Ghiost","Grass","Water","Rock","Dragon","Eletric","Dark","Bug","Fire","Poison","Rock","Dragon","Fairy","Grass","Ghiost","Water","Ice","Bug","Dark","Ice","","Poison","Dragon","Fairy"]

imp_mes = input("Digite o Mes: ")
imp_dia = int(input("Digite o Dia: "))

print(dict_tipo_mes[imp_mes]+ " "+tipo_dia[imp_dia])
