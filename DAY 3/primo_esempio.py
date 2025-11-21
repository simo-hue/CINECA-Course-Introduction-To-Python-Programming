class veicolo:
    type = "veicolo"
    def __init__(self, marca = "", modello = ""):
        self.marca = marca
        self.modello = modello
        
    def __str__(self):
        return str(self.marca) + " " + str(self.modello)
    
class automobile(veicolo):
    type = "automobile"
    def __init__(self, marca = "", modello = "", cilindrata = 0):
        super().__init__(marca, modello)
        self.cilindrata = cilindrata    

x = veicolo("Fiat", "Panda")

print("\n", x.__str__())
print(f"\n\nLa macchina del mio amore è una {x.marca} modello {x.modello}\n\n")