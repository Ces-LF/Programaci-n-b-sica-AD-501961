#Peso molecular en kda de la proteína pectin methylesterase [Aspergillus aculeatus]
import numpy as np
cadena="MVKSVLASALFAVSALAASRTTAPSGAIVVAKSGGDYTTIGDAIDALSTSTTDTQTIFIEEGTYDEQVYLPAMTGKVIIYGQTENTDSYADNLVTITHAISYEDAGESDDLTATFRNKAVGSQVYNLNIANTCGQACHQALALSAWADQQGYYGCNFTGYQDTLLAQTGNQLYINSYIEGAVDFIFGQHARAWFQNVDIRVVEGPTSASITANGRSSETDTSYYVINKSTVAAKEGDDVAEGTYYLGRPWSEYARVVFQQTSMTNVINSLGWTEWSTSTPNTEYVTFGEYANTGAGSEGTRASFAEKLDAKLTITDILGSDYTSWVDTSYF"
lista=[]
for aminoácido in cadena:
    lista.append(aminoácido)
CADAA=lista
filtradoM=[x for x in CADAA if x=='M']
filtradoV=[x for x in CADAA if x=='V']
filtradoK=[x for x in CADAA if x=='K']
filtradoS=[x for x in CADAA if x=='S']
filtradoL=[x for x in CADAA if x=='L']
filtradoA=[x for x in CADAA if x=='A']
filtradoF=[x for x in CADAA if x=='F']
filtradoR=[x for x in CADAA if x=='R']
filtradoT=[x for x in CADAA if x=='T']
filtradoP=[x for x in CADAA if x=='P']
filtradoG=[x for x in CADAA if x=='G']
filtradoI=[x for x in CADAA if x=='I']
filtradoD=[x for x in CADAA if x=='D']
filtradoE=[x for x in CADAA if x=='E']
filtradoN=[x for x in CADAA if x=='N']
filtradoQ=[x for x in CADAA if x=='Q']
filtradoC=[x for x in CADAA if x=='C']
filtradoY=[x for x in CADAA if x=='Y']
filtradoH=[x for x in CADAA if x=='H']
filtradoW=[x for x in CADAA if x=='W']
Apariciones=[len(filtradoM),len(filtradoV),len(filtradoK),len(filtradoS),len(filtradoL),len(filtradoA),len(filtradoF),len(filtradoR),len(filtradoT),len(filtradoP),len(filtradoG),len(filtradoI),len(filtradoD),len(filtradoE),len(filtradoN),len(filtradoQ),len(filtradoC),len(filtradoY),len(filtradoH),len(filtradoW)]
#Pesos moleculares de aa
A1=np.array(Apariciones)
A2=np.array([149,117,146,105,131,89,165,174,119,115,75,131,133,147,132,146,121,181,155,204])
Pesos_Mol_aa=A1*A2
print(Pesos_Mol_aa)
#Peso molecular de la proteína
Peso_Mol_Prot=Pesos_Mol_aa.tolist()
print(sum(Peso_Mol_Prot))
#Porcentaje de cada aa
print(Apariciones)
Porcentaje=(A1/331)*100
print(Porcentaje) 
#índices de extinción
print(f"Y: {len(filtradoY)} \n W: {len(filtradoW)} \n C: {len(filtradoC)}")