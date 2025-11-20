# Python - Giorno 2: Strutture Dati e I/O

## 📦 Containers (Contenitori)

I containers sono strutture dati che possono contenere un **numero arbitrario di oggetti**. Python offre diversi tipi di container, ognuno con caratteristiche specifiche.

---

## 📋 Liste (List)

### Caratteristiche principali

- **Sintassi**: `[]` oppure `list()`
- ✅ **Ordinata**: mantiene l'ordine di inserimento
- ✅ **Mutabile**: gli elementi possono essere modificati
- ✅ **Dinamica**: la dimensione può cambiare
- ✅ **Duplicati ammessi**
- ✅ **Nidificazione**: possono contenere altre liste

### Creazione e accesso

```python
# Creazione
lista_vuota = []
lista_vuota2 = list()
numeri = [1, 2, 3, 4, 5]
mista = [1, "hello", 3.14, True]

# Accesso agli elementi (indice parte da 0)
print(numeri[0])   # 1 (primo elemento)
print(numeri[-1])  # 5 (ultimo elemento)
print(numeri[-2])  # 4 (penultimo elemento)

# Liste nidificate
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrice[0][1])  # 2 (primo array, secondo elemento)
```

### Modificare le liste

```python
numeri = [1, 2, 3, 4, 5]

# Modifica singolo elemento
numeri[0] = 10  # [10, 2, 3, 4, 5]

# Aggiungere elementi
numeri.append(6)        # Aggiunge alla fine: [10, 2, 3, 4, 5, 6]
numeri.insert(1, 15)    # Inserisce all'indice 1: [10, 15, 2, 3, 4, 5, 6]

# Rimuovere elementi
numeri.remove(15)       # Rimuove il primo 15 trovato
elemento = numeri.pop() # Rimuove e ritorna l'ultimo elemento
del numeri[0]           # Rimuove l'elemento all'indice 0
```

### 🔍 Differenza tra `append()` e `extend()`

Questa è una distinzione **fondamentale**:

```python
lista = [1, 2, 3]

# append() - aggiunge l'intero oggetto come singolo elemento
lista.append([4, 5])
print(lista)  # [1, 2, 3, [4, 5]] <- lista dentro lista!

# extend() - aggiunge ogni elemento della sequenza
lista2 = [1, 2, 3]
lista2.extend([4, 5])
print(lista2)  # [1, 2, 3, 4, 5] <- elementi aggiunti singolarmente
```

| Metodo | Comportamento | Uso tipico |
|--------|---------------|------------|
| `append(x)` | Aggiunge `x` come **singolo elemento** | Aggiungere un oggetto (anche se è una lista) |
| `extend(iterable)` | Aggiunge **ogni elemento** dell'iterabile | Unire due liste |

**Esempio pratico:**

```python
# append - aggiunge come singolo elemento
squadre = ["Juventus", "Milan"]
squadre.append(["Inter", "Roma"])
print(squadre)  # ["Juventus", "Milan", ["Inter", "Roma"]]
print(len(squadre))  # 3 elementi

# extend - aggiunge ogni elemento
squadre2 = ["Juventus", "Milan"]
squadre2.extend(["Inter", "Roma"])
print(squadre2)  # ["Juventus", "Milan", "Inter", "Roma"]
print(len(squadre2))  # 4 elementi
```

### Slicing delle liste

Lo **slicing** permette di estrarre sottosezioni di una lista:

**Sintassi**: `lista[start:stop:step]`

| Parametro | Descrizione | Default |
|-----------|-------------|---------|
| `start` | Indice di partenza (incluso) | 0 |
| `stop` | Indice di fine (escluso) | len(lista) |
| `step` | Incremento | 1 |

```python
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing base
print(numeri[2:7])      # [2, 3, 4, 5, 6]
print(numeri[:5])       # [0, 1, 2, 3, 4] (dall'inizio)
print(numeri[5:])       # [5, 6, 7, 8, 9] (fino alla fine)
print(numeri[:])        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copia completa)

# Con step
print(numeri[::2])      # [0, 2, 4, 6, 8] (elementi pari)
print(numeri[1::2])     # [1, 3, 5, 7, 9] (elementi dispari)

# Step negativo (inversione)
print(numeri[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numeri[7:2:-1])   # [7, 6, 5, 4, 3]
```

### Metodi utili delle liste

```python
numeri = [3, 1, 4, 1, 5, 9, 2]

# Ordinamento
numeri.sort()              # Ordina in place: [1, 1, 2, 3, 4, 5, 9]
ordinata = sorted(numeri)  # Ritorna una nuova lista ordinata

# Inversione
numeri.reverse()           # Inverte in place

# Ricerca
indice = numeri.index(4)   # Ritorna l'indice del primo 4
conta = numeri.count(1)    # Conta le occorrenze di 1

# Lunghezza
lunghezza = len(numeri)
```

---

## 🔒 Tuple

### Caratteristiche principali

- **Sintassi**: `()` oppure `tuple()`
- ✅ **Ordinata**: mantiene l'ordine
- 🔒 **Immutabile**: NON può essere modificata dopo la creazione
- ⚡ **Più veloce**: iterazione più efficiente rispetto alle liste
- 💾 **Meno memoria**: occupano meno spazio

### Quando usare le tuple?

1. **Dati costanti**: coordinate, configurazioni
2. **Read-only**: garantire che i dati non vengano modificati
3. **Chiavi di dizionario**: le liste non possono essere usate come chiavi
4. **Performance**: quando serve efficienza

### Creazione e accesso

```python
# Creazione
tupla_vuota = ()
tupla_vuota2 = tuple()
coordinate = (10, 20)
dati = (1, "hello", 3.14, True)

# Tupla con un solo elemento (nota la virgola!)
singolo = (5,)  # Tupla
non_tupla = (5) # NON è una tupla, è solo il numero 5

# Accesso (come le liste)
print(coordinate[0])  # 10
print(dati[-1])       # True

# ❌ Modifica NON permessa
# coordinate[0] = 15  # TypeError: 'tuple' object does not support item assignment
```

### Unpacking delle tuple

```python
# Unpacking
coordinate = (10, 20)
x, y = coordinate
print(f"x={x}, y={y}")  # x=10, y=20

# Scambio di variabili elegante
a, b = 5, 10
a, b = b, a  # Scambia i valori senza variabile temporanea
print(a, b)  # 10, 5

# Unpacking parziale
dati = (1, 2, 3, 4, 5)
primo, *resto, ultimo = dati
print(primo)   # 1
print(resto)   # [2, 3, 4]
print(ultimo)  # 5
```

---

## 🔄 Passaggio di parametri alle funzioni

Python gestisce i parametri in modo diverso a seconda della **mutabilità** dell'oggetto.

### Oggetti Mutabili vs Immutabili

| Tipo | Mutabilità | Passaggio | Esempi |
|------|------------|-----------|--------|
| **Immutabili** | 🔒 Non modificabili | Per valore (copia) | `int`, `float`, `str`, `tuple`, `bool` |
| **Mutabili** | ✏️ Modificabili | Per riferimento | `list`, `dict`, `set` |

### Comportamento pratico

```python
# IMMUTABILI - passaggio per valore
def modifica_numero(n):
    n = n + 10
    print(f"Dentro la funzione: {n}")

x = 5
modifica_numero(x)  # Dentro la funzione: 15
print(f"Fuori dalla funzione: {x}")  # Fuori dalla funzione: 5 (NON modificato!)

# MUTABILI - passaggio per riferimento
def modifica_lista(lista):
    lista.append(99)
    print(f"Dentro la funzione: {lista}")

numeri = [1, 2, 3]
modifica_lista(numeri)  # Dentro la funzione: [1, 2, 3, 99]
print(f"Fuori dalla funzione: {numeri}")  # Fuori dalla funzione: [1, 2, 3, 99] (MODIFICATO!)
```

### ⚠️ Attenzione con gli oggetti mutabili!

```python
# Per evitare modifiche indesiderate, passa una copia
def funzione_sicura(lista):
    lista_locale = lista.copy()  # Oppure lista[:]
    lista_locale.append(99)
    return lista_locale

originale = [1, 2, 3]
modificata = funzione_sicura(originale)
print(originale)   # [1, 2, 3] (intatta)
print(modificata)  # [1, 2, 3, 99]
```

### 💡 Return vs modifica in-place

```python
# Approccio 1: Return (più comune e chiaro)
def aggiungi_elemento_return(lista, elemento):
    lista.append(elemento)
    return lista

# Approccio 2: Modifica in-place (più efficiente per liste grandi)
def aggiungi_elemento_inplace(lista, elemento):
    lista.append(elemento)
    # Non ritorna nulla, modifica l'originale
```

**Best Practice**: Preferisci il `return` per chiarezza, a meno che l'efficienza sia critica.

---

## 🎲 Set (Insiemi)

### Caratteristiche principali

- **Sintassi**: `{}` oppure `set()`
- ❌ **NON ordinato**: nessun indice
- ❌ **NO duplicati**: ogni elemento è unico
- ✅ **Mutabile**: puoi aggiungere/rimuovere elementi
- ⚡ **Ricerca veloce**: operazioni O(1) in media

### Creazione e utilizzo

```python
# Creazione
insieme_vuoto = set()  # ⚠️ {} crea un dizionario vuoto!
numeri = {1, 2, 3, 4, 5}
lettere = set("hello")  # {'h', 'e', 'l', 'o'} (duplicati rimossi)

# Aggiungere elementi
numeri.add(6)          # {1, 2, 3, 4, 5, 6}
numeri.update([7, 8])  # {1, 2, 3, 4, 5, 6, 7, 8}

# Rimuovere elementi
numeri.remove(3)       # Errore se non esiste
numeri.discard(3)      # Non dà errore se non esiste
elemento = numeri.pop() # Rimuove un elemento casuale

# ❌ Non posso accedere per indice
# print(numeri[0])  # TypeError

# ✅ Posso iterare
for num in numeri:
    print(num)
```

### Casi d'uso principali

#### 1. Rimuovere duplicati

```python
lista_con_duplicati = [1, 2, 2, 3, 3, 3, 4, 5, 5]
lista_unica = list(set(lista_con_duplicati))
print(lista_unica)  # [1, 2, 3, 4, 5]
```

#### 2. Operazioni insiemistiche

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# UNIONE (elementi in a OR b)
unione1 = a.union(b)
unione2 = a | b
print(unione1)  # {1, 2, 3, 4, 5, 6, 7, 8}

# INTERSEZIONE (elementi in a AND b)
intersezione1 = a.intersection(b)
intersezione2 = a & b
print(intersezione1)  # {4, 5}

# DIFFERENZA (elementi in a ma non in b)
differenza1 = a.difference(b)
differenza2 = a - b
print(differenza1)  # {1, 2, 3}

# DIFFERENZA SIMMETRICA (elementi in a o b, ma non in entrambi)
diff_simmetrica = a.symmetric_difference(b)
print(diff_simmetrica)  # {1, 2, 3, 6, 7, 8}
```

### Operazioni di test

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

# Sottoinsieme
print(a.issubset(b))    # True (a ⊆ b)
print(a <= b)           # True

# Sovrainsieme
print(b.issuperset(a))  # True (b ⊇ a)
print(b >= a)           # True

# Disgiunti (nessun elemento in comune)
c = {6, 7, 8}
print(a.isdisjoint(c))  # True
```

---

## 📝 Stringhe (String)

### Caratteristiche principali

- **Sintassi**: `""` o `''` oppure `str()`
- 🔒 **Immutabile**: non può essere modificata dopo la creazione
- ✅ **Sequenza**: supporta indicizzazione e slicing
- ✅ **Iterabile**: puoi ciclare sui caratteri

### Creazione e operazioni base

```python
# Creazione
stringa_vuota = ""
stringa_vuota2 = str()
testo = "Hello, World!"

# Concatenazione
saluto = "Hello" + " " + "World"  # "Hello World"
ripetizione = "Ha" * 3            # "HaHaHa"

# Conversione
numero = 45
stringa_numero = str(numero)      # "45"
messaggio = "Il valore è " + stringa_numero

# ❌ Immutabilità - NON posso modificare
# testo[0] = 'h'  # TypeError: 'str' object does not support item assignment

# ✅ Posso creare una nuova stringa
testo_modificato = testo.replace("World", "Python")
print(testo)            # "Hello, World!" (originale intatto)
print(testo_modificato) # "Hello, Python!"
```

### Accesso e slicing

```python
testo = "Python Programming"

# Accesso ai caratteri
print(testo[0])    # 'P'
print(testo[-1])   # 'g'

# Slicing (come le liste)
print(testo[0:6])  # "Python"
print(testo[7:])   # "Programming"
print(testo[::-1]) # "gnimmargorP nohtyP" (inversione)

# Iterazione
for carattere in testo:
    print(carattere)

# Con enumerate
for i, char in enumerate(testo):
    print(f"Posizione {i}: {char}")
```

### Metodi comuni delle stringhe

```python
testo = "  Hello, World!  "

# Case
print(testo.upper())        # "  HELLO, WORLD!  "
print(testo.lower())        # "  hello, world!  "
print(testo.capitalize())   # "  hello, world!  "
print(testo.title())        # "  Hello, World!  "

# Pulizia
print(testo.strip())        # "Hello, World!" (rimuove spazi)
print(testo.lstrip())       # "Hello, World!  " (solo a sinistra)
print(testo.rstrip())       # "  Hello, World!" (solo a destra)

# Ricerca
print(testo.find("World"))  # 9 (indice dove inizia)
print(testo.find("Python")) # -1 (non trovato)
print("World" in testo)     # True

# Sostituzione
nuovo = testo.replace("World", "Python")
print(nuovo)                # "  Hello, Python!  "

# Verifica
print("hello".isalpha())    # True (solo lettere)
print("123".isdigit())      # True (solo cifre)
print("hello123".isalnum()) # True (lettere e cifre)
```

### Split e Join

#### `split()` - dividere una stringa

```python
# split(separatore, maxsplit)
frase = "Python è un linguaggio potente"

# Split base (divide per spazi)
parole = frase.split()
print(parole)  # ['Python', 'è', 'un', 'linguaggio', 'potente']

# Split con separatore personalizzato
dati = "Mario,30,Roma"
campi = dati.split(",")
print(campi)  # ['Mario', '30', 'Roma']

# Con maxsplit (numero massimo di divisioni)
testo = "a-b-c-d-e"
parti = testo.split("-", 2)  # Dividi al massimo 2 volte
print(parti)  # ['a', 'b', 'c-d-e']
```

#### `join()` - unire elementi in una stringa

```python
# separatore.join(iterabile)
parole = ['Python', 'è', 'fantastico']

# Unione con spazio
frase = " ".join(parole)
print(frase)  # "Python è fantastico"

# Unione con altri separatori
csv = ",".join(['Mario', '30', 'Roma'])
print(csv)  # "Mario,30,Roma"

# Con numeri (convertili prima in stringhe!)
numeri = [1, 2, 3, 4, 5]
stringa_numeri = "-".join(str(n) for n in numeri)
print(stringa_numeri)  # "1-2-3-4-5"
```

### Formattazione stringhe

```python
nome = "Mario"
eta = 30

# f-strings (Python 3.6+, CONSIGLIATO)
messaggio = f"Mi chiamo {nome} e ho {eta} anni"
print(messaggio)  # "Mi chiamo Mario e ho 30 anni"

# Con espressioni
print(f"L'anno prossimo avrò {eta + 1} anni")

# format()
messaggio2 = "Mi chiamo {} e ho {} anni".format(nome, eta)

# % operator (vecchio stile)
messaggio3 = "Mi chiamo %s e ho %d anni" % (nome, eta)
```

---

## 📊 Liste vs Array NumPy

### ⚠️ Limitazioni delle liste Python

Le liste sono **comode** ma **inefficienti** per calcoli numerici:

```python
# Liste - elementi sparsi in memoria
lista = [1, 2, 3, 4, 5]
# Memoria: [ptr1] -> 1, [ptr2] -> 2, [ptr3] -> 3, ...
```

**Problemi**:
- ❌ Memoria non contigua (accessi lenti)
- ❌ Ogni elemento è un oggetto Python (overhead)
- ❌ Operazioni vettoriali non native

### ✅ Array NumPy (Preview)

```python
import numpy as np

# Array NumPy - memoria contigua
array = np.array([1, 2, 3, 4, 5])
# Memoria: [1][2][3][4][5] <- tutto di seguito

# Operazioni vettoriali efficienti
risultato = array * 2  # [2, 4, 6, 8, 10]
```

**Vantaggi**:
- ✅ Memoria contigua (cache-friendly)
- ✅ Operazioni vettorizzate veloci
- ✅ Meno overhead per elemento

> **Nota**: NumPy sarà approfondito nei prossimi giorni!

---

## 📁 I/O con File

### Funzione `open()`

**Sintassi**: `open(nome_file, modalità)`

#### Modalità di apertura

| Modalità | Descrizione | Crea file | Sovrascrive |
|----------|-------------|-----------|-------------|
| `'r'` | **Read** - lettura (default) | ❌ | ❌ |
| `'w'` | **Write** - scrittura | ✅ | ✅ |
| `'x'` | **eXclusive** - crea file nuovo | ✅ | ❌ (errore se esiste) |
| `'a'` | **Append** - aggiunge in fondo | ✅ | ❌ |
| `'b'` | **Binary** - modalità binaria | - | - |
| `'t'` | **Text** - modalità testo (default) | - | - |
| `'+'` | **Update** - lettura e scrittura | ❌ | ❌ |

**Combinazioni comuni**:
- `'rb'`: lettura binaria
- `'wb'`: scrittura binaria
- `'r+'`: lettura e scrittura
- `'w+'`: scrittura e lettura (sovrascrive)
- `'a+'`: append e lettura

### Lettura da file

```python
# Metodo BASE (non consigliato)
file = open("dati.txt", "r")
contenuto = file.read()
print(contenuto)
file.close()  # ⚠️ Facile dimenticarsi!

# ✅ BEST PRACTICE: Context Manager (with)
with open("dati.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)
# File chiuso automaticamente qui!
```

**Vantaggi del Context Manager (`with`)**:
1. ✅ **Chiusura automatica**: anche in caso di errori
2. ✅ **Codice più pulito**: meno righe
3. ✅ **Gestione eccezioni**: garantisce la chiusura

### Metodi di lettura

```python
# read() - legge tutto il file
with open("dati.txt", "r") as f:
    tutto = f.read()
    print(tutto)

# readline() - legge una riga alla volta
with open("dati.txt", "r") as f:
    prima_riga = f.readline()
    seconda_riga = f.readline()
    print(prima_riga)

# readline().strip() - rimuove \n e spazi
with open("dati.txt", "r") as f:
    riga_pulita = f.readline().strip()
    print(repr(riga_pulita))  # Mostra senza \n

# readlines() - ritorna lista di tutte le righe
with open("dati.txt", "r") as f:
    righe = f.readlines()
    for riga in righe:
        print(riga.strip())

# Iterazione diretta (MEMORIA EFFICIENTE)
with open("dati.txt", "r") as f:
    for riga in f:  # Legge una riga alla volta
        print(riga.strip())
```

### Scrittura su file

```python
# write() - scrive una stringa
with open("output.txt", "w") as f:
    caratteri_scritti = f.write("Hello, World!\n")
    print(f"Scritti {caratteri_scritti} caratteri")

# ⚠️ write() accetta SOLO stringhe!
with open("numeri.txt", "w") as f:
    numero = 42
    # f.write(numero)  # ❌ ERRORE!
    f.write(str(numero))  # ✅ OK

# writelines() - scrive una lista di stringhe
righe = ["Prima riga\n", "Seconda riga\n", "Terza riga\n"]
with open("output.txt", "w") as f:
    f.writelines(righe)

# Append - aggiunge senza sovrascrivere
with open("log.txt", "a") as f:
    f.write("Nuova riga di log\n")
```

### Esempio pratico: processare un file CSV

```python
# Leggere e processare CSV
with open("dati.csv", "r") as f:
    intestazione = f.readline().strip().split(",")
    print(f"Colonne: {intestazione}")
    
    for riga in f:
        valori = riga.strip().split(",")
        print(valori)

# Scrivere CSV
dati = [
    ["Nome", "Età", "Città"],
    ["Mario", "30", "Roma"],
    ["Laura", "25", "Milano"]
]

with open("output.csv", "w") as f:
    for riga in dati:
        f.write(",".join(riga) + "\n")
```

### Gestione errori con file

```python
# Gestire file non esistenti
try:
    with open("file_inesistente.txt", "r") as f:
        contenuto = f.read()
except FileNotFoundError:
    print("❌ File non trovato!")
except PermissionError:
    print("❌ Permessi insufficienti!")
except Exception as e:
    print(f"❌ Errore: {e}")
```

---

## 💡 Best Practices - Strutture Dati

### Liste
1. **Usa list comprehension** per creare liste: `[x**2 for x in range(10)]`
2. **`extend()` vs `append()`**: comprendi la differenza!
3. **Slicing per copie**: `lista[:]` crea una copia superficiale

### Tuple
1. **Usa tuple per dati costanti** e coordinate
2. **Return multipli**: `return x, y, z` (è una tupla!)
3. **Virgola per singolo elemento**: `(5,)` non `(5)`

### Set
1. **Rimuovi duplicati velocemente**: `list(set(lista))`
2. **Test di appartenenza**: `if elem in my_set:` è O(1)
3. **Operazioni insiemistiche** invece di cicli complessi

### Stringhe
1. **f-strings** per formattazione (Python 3.6+)
2. **`join()` per concatenare** molte stringhe (più efficiente di `+`)
3. **`strip()` dopo `readline()`** per rimuovere `\n`

### File I/O
1. **Sempre usare `with`** per aprire file
2. **Itera direttamente** sul file invece di `readlines()` (meno memoria)
3. **`str()` prima di `write()`** se hai numeri

---

## 📚 Riepilogo Comparativo

| Struttura | Ordinata | Mutabile | Duplicati | Sintassi | Uso principale |
|-----------|----------|----------|-----------|----------|----------------|
| **Lista** | ✅ | ✅ | ✅ | `[1, 2, 3]` | Collezioni modificabili |
| **Tupla** | ✅ | ❌ | ✅ | `(1, 2, 3)` | Dati costanti, return multipli |
| **Set** | ❌ | ✅ | ❌ | `{1, 2, 3}` | Unicità, operazioni insiemistiche |
| **Stringa** | ✅ | ❌ | ✅ | `"hello"` | Testo immutabile |

---

*Prossimo: Giorno 3 - Dizionari, Comprehension e Programmazione Orientata agli Oggetti*