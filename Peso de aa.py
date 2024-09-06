#Peso molecular en kda de la proteína pectin methylesterase [Aspergillus aculeatus]
cadena="MVKSVLASALFAVSALAASRTTAPSGAIVVAKSGGDYTTIGDAIDALSTSTTDTQTIFIEEGTYDEQVYLPAMTGKVIIYGQTENTDSYADNLVTITHAISYEDAGESDDLTATFRNKAVGSQVYNLNIANTCGQACHQALALSAWADQQGYYGCNFTGYQDTLLAQTGNQLYINSYIEGAVDFIFGQHARAWFQNVDIRVVEGPTSASITANGRSSETDTSYYVINKSTVAAKEGDDVAEGTYYLGRPWSEYARVVFQQTSMTNVINSLGWTEWSTSTPNTEYVTFGEYANTGAGSEGTRASFAEKLDAKLTITDILGSDYTSWVDTSYF"
lista=[]
for aminoácido in cadena:
    lista.append(aminoácido)
CADAA=lista
print(len(CADAA))
print(len(CADAA)*110/1000)
filtradoG=[x for x in CADAA if x=='G']
filtradoA=[x for x in CADAA if x=='A']
filtradoV=[x for x in CADAA if x=='V']
filtradoL=[x for x in CADAA if x=='L']
filtradoI=[x for x in CADAA if x=='I']
filtradoP=[x for x in CADAA if x=='P']
filtradoF=[x for x in CADAA if x=='F']
filtradoY=[x for x in CADAA if x=='Y']
filtradoW=[x for x in CADAA if x=='W']
filtradoS=[x for x in CADAA if x=='S']
filtradoC=[x for x in CADAA if x=='C']
filtradoB=[x for x in CADAA if x=='B']
filtradoQ=[x for x in CADAA if x=='Q']
filtradoM=[x for x in CADAA if x=='M']
filtradoK=[x for x in CADAA if x=='K']
filtradoR=[x for x in CADAA if x=='R']
filtradoH=[x for x in CADAA if x=='H']
Apariciones=[len(filtradoG),len(filtradoA),len(filtradoV),len(filtradoL),len(filtradoI),len(filtradoP),len(filtradoF),len(filtradoY),len(filtradoW),len(filtradoS),len(filtradoC),len(filtradoB),len(filtradoQ),len(filtradoM),len(filtradoK),len(filtradoR),len(filtradoH)]
print(len(Apariciones))
