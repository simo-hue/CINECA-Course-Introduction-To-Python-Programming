import random as rm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Dado:
    def __init__(self, nFaccie):
        self.nFaccie = nFaccie
        
    def lancio(self):
        return rm.randint(1, self.nFaccie)

# --- Configurazione ---
d1 = Dado(6)
results = {faccia: 0 for faccia in range(1, d1.nFaccie + 1)}

fig, ax = plt.subplots()
x = list(results.keys())
# Iniziamo con altezze a 0
y = [0] * len(x) 

barre = ax.bar(x, y, color='lightgreen', edgecolor='black')

# Linea rossa tratteggiata che indica la probabilità teorica (1/6 = 16.66%)
prob_teorica = (1 / 6) * 100
ax.axhline(y=prob_teorica, color='red', linestyle='--', linewidth=2, label=f"Teorica ({prob_teorica:.1f}%)")
ax.legend() # Mostra la legenda della linea rossa

ax.set_title("Convergenza alla probabilità teorica")
ax.set_xlabel("Faccia")
ax.set_ylabel("Percentuale (%)")

# Fissiamo l'asse Y tra 0 e 40%. 
# Non serve arrivare a 100% perché dopo pochi lanci nessuno avrà il 100%.
ax.set_ylim(0, 40) 

def update(frame):
    # 'frame' parte da 0, quindi il numero totale di lanci è frame + 1
    totale_lanci = frame + 1
    
    # 1. Lancia il dado e aggiorna i conteggi
    uscita = d1.lancio()
    results[uscita] += 1
    
    # 2. Aggiorna l'altezza delle barre calcolando la percentuale
    for rect, faccia in zip(barre, x):
        conteggio = results[faccia]
        # Calcolo percentuale: (conteggio / totale) * 100
        percentuale = (conteggio / totale_lanci) * 100
        rect.set_height(percentuale)

    # 3. Aggiorna il titolo
    ax.set_title(f"Lanci totali: {totale_lanci}")

# Intervallo ridotto a 10ms per vederlo correre veloce
ani = FuncAnimation(fig, update, interval=10, cache_frame_data=False)

plt.show()