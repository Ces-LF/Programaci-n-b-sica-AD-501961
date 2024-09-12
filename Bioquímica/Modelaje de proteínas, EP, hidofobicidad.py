# Ejemplo simplificado del algoritmo de Zimmerman

# Definición de propiedades de aminoácidos
polaridad_aminoacidos = {
    'A': 'apolar', 'R': 'polar', 'N': 'polar', 'D': 'polar', 'C': 'polar',
    'E': 'polar', 'Q': 'polar', 'G': 'apolar', 'H': 'polar', 'I': 'apolar',
    'L': 'apolar', 'K': 'polar', 'M': 'apolar', 'F': 'apolar', 'P': 'apolar',
    'S': 'polar', 'T': 'polar', 'W': 'polar', 'Y': 'polar', 'V': 'apolar'
}

def calcular_polaridad_proteina(secuencia):
    puntaje_polar = 0
    puntaje_apolar = 0
    
    for aminoacido in secuencia:
        if polaridad_aminoacidos.get(aminoacido, 'apolar') == 'polar':
            puntaje_polar += 1
        else:
            puntaje_apolar += 1
    
    # Determinamos la polaridad global
    if puntaje_polar > puntaje_apolar:
        return 'Polar'
    else:
        return 'Apolar'

# Ejemplo de uso
secuencia_proteina1 = 'MVKSVLASALFAVSALAASRTTAPSGAIVVAKSGGDYTTIGDAIDALSTSTTDTQTIFIEEGTYDEQVYLPAMTGKVIIYGQTENTDSYADNLVTITHAISYEDAGESDDLTATFRNKAVGSQVYNLNIANTCGQACHQALALSAWADQQGYYGCNFTGYQDTLLAQTGNQLYINSYIEGAVDFIFGQHARAWFQNVDIRVVEGPTSASITANGRSSETDTSYYVINKSTVAAKEGDDVAEGTYYLGRPWSEYARVVFQQTSMTNVINSLGWTEWSTSTPNTEYVTFGEYANTGAGSEGTRASFAEKLDAKLTITDILGSDYTSWVDTSYF'
resultado1 = calcular_polaridad_proteina(secuencia_proteina1)
print(f"La proteína es: {resultado1}")
