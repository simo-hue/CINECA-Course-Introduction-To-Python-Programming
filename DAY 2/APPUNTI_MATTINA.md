# DAY 2

## CONTAINERS

Contengono un numero arbitrario di oggetti

### LIST

si usano le parentesi [] oppure la funzione list()

è ordinata, gli elementi possono cambiare ed è dinamica ( può essere cambiata la dimensione )

Possono essere anche innestate una dentro l'altra

differenza tra extend o append sulla lista? Da rispondere in dettaglio

.insert(index, element)

SLICING DELLE LISTE: list[start: stop: step] dove di default lo step = 1

### TUPLE

SONO IMMUTABILI, quindi una volta dichiarate non possono più essere riassegnate per nessuna maniera: x[0] = "ciao" NON è fattibile ( nella lista lo sarebbe stato )

iterazione su tuple è più veloce che quella sulle liste

Utilizzate per costanti, per garantire che è una variabile read only

si usano le parentesi tonde () oppure la funzione tuple()



### COME VENGONO PASSATI AD UNA FUNZIONE?

- mutable: passato per referenza ( object reference ) -> modifico anche i dati del chiamante
- immutable: passato per valore -> creo nuovi valori all'interno dello scoping della funzione -> Chiamante NON vede nessuna modifica

La funzione potrebbe ritornare anche i valori calcolati tramite "return" che è più comune come cosa però va a costare di più in termini di efficienza

---

### SET

è un inseme NON ordinato che NON ammette duplicati

Non si può accedere direttamente ad un elemento ma bisogna ciclarci per trovarlo

utile per:
- rimuovere duplicati
- operazioni insiemistiche
'''
c = list("hello")

x = set(c)

print(c, x)
'''

ESempio di UNIONE: .union() oppure con la pipe "|"
ESempio di INTERSEZIONE: .intersection() oppure con and "&"
ESempio di DIFFERENZE: .difference() oppure con il meno "-"

posso aggiornare/inserire un elemento nel set attraverso

issubset per capire se è un sottoinsieme oppure no

### STRINGE

VUOTA: x = str() oppure x = ""

si concatenano con il "+"

sono immutabili quindi non posso assegnare str[0] = 'a' ad esempio -> una volta fatta non si può modificare se non con .replace(oldChar,newChar)

'''
x = 45
strx = str(x)
print("Il valore di x è " + strx)

for i in range(len(strx)):
    print("Posizione " + str(i) + " : " + strx[i])
    
print(str.find(strx, '5'))
'''

supportano lo slicing classico come le liste, ma anche con metodi specifici come .split(separatore, maxSplit)

metodo JOIN 

---


LISTE si sono comode e semplici da utilizzare ma ESTREMAMENTE inefficiente perchè non abbiamo spazio continuo in memoria ma random e per questo si utilizzano gli array di numpy

### I/O con i file

tramite open(nomeFile, modalità)

| mode |  |
| :--  | :-- |
| 'r'  |     open for reading (default) |
| 'w'  |     open for writing, truncating the file first |
| 'x'  |     create a new file and open it for writing |
| 'a'  |     open for writing, appending to the end of the file if it exists |
| 'b'  |     binary mode |
| 't'  |     text mode (default) |
| '+'  |     open a disk file for updating (reading and writing) |
| 'U'  |     universal newline mode (deprecated) |

ricordarsi di chiudere sempre il file, ma se vogliamo utilizzare la best practise allora va inserito "with [lettura file]:"
in modo tale che venga chiuso una volta che usciamo da with ( context manager ci pensa al posto mio ed è garantito che venga chiuso il file )

**BEST PRACTISE:** chiusura controllata, non ci si dimentica, gestisce anche anomalie ( programma muore nel with )

read() -> tutto il file
readLine() -> Legge una riga
readLine().strip() -> Legge una riga ( ma toglie caratteri tipo '\n')
readlines() -> ritorna una lista di tutto il file ( suddiviso per riga )

write() mi ritorna i caratteri scritti -> **NB che write accetta stringhe**