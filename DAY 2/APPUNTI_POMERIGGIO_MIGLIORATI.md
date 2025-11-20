# Python - Giorno 2 (Parte 2): Dizionari, Funzioni Avanzate e Libreria Standard

## 🗂️ Dizionari (Dictionary)

### Caratteristiche principali

- **Sintassi**: `{}` oppure `dict()`
- ❌ **NON ordinato** (prima di Python 3.7)
- ✅ **Ordinato** (da Python 3.7+, mantiene ordine di inserimento)
- ✅ **Mutabile**: valori modificabili
- 🔑 **Chiavi uniche**: NON ammette chiavi duplicate
- 🔒 **Chiavi immutabili**: solo tipi immutabili come chiavi (str, int, tuple)

### Struttura: Coppie chiave-valore

Un dizionario è una collezione di **coppie chiave-valore**, dove:
- La **chiave** è univoca e immutabile
- Il **valore** può essere di qualsiasi tipo e modificabile

```python
# Chiave    -> Valore
{"nome"     -> "Mario",
 "età"      -> 30,
 "città"    -> "Roma"}
```

### Creazione e accesso

```python
# Creazione
dizionario_vuoto = {}
dizionario_vuoto2 = dict()

# Dizionario con dati
persona = {
    "nome": "Mario",
    "età": 30,
    "città": "Roma"
}

# Accesso ai valori tramite chiave
print(persona["nome"])      # "Mario"
print(persona.get("età"))   # 30

# Differenza tra [] e get()
# print(persona["paese"])    # ❌ KeyError!
print(persona.get("paese"))  # None (nessun errore)
print(persona.get("paese", "Italia"))  # "Italia" (valore default)
```

### Modifica e aggiunta

```python
persona = {"nome": "Mario", "età": 30}

# Modificare un valore esistente
persona["età"] = 31

# Aggiungere una nuova coppia chiave-valore
persona["professione"] = "Ingegnere"

# Aggiornare con update()
persona.update({"città": "Milano", "hobby": "fotografia"})

print(persona)
# {'nome': 'Mario', 'età': 31, 'professione': 'Ingegnere', 
#  'città': 'Milano', 'hobby': 'fotografia'}
```

### Rimozione elementi

```python
persona = {"nome": "Mario", "età": 30, "città": "Roma"}

# Rimuovere con del
del persona["città"]

# Rimuovere con pop() (ritorna il valore)
eta = persona.pop("età")
print(eta)  # 30

# Rimuovere con pop() con default
paese = persona.pop("paese", "Non specificato")

# Rimuovere l'ultima coppia inserita (Python 3.7+)
ultimo = persona.popitem()

# Svuotare il dizionario
persona.clear()
```

### Iterazione sui dizionari

```python
persona = {"nome": "Mario", "età": 30, "città": "Roma"}

# Iterare sulle chiavi (default)
for chiave in persona:
    print(chiave)  # nome, età, città

# Iterare esplicitamente sulle chiavi
for chiave in persona.keys():
    print(chiave, persona[chiave])

# Iterare sui valori
for valore in persona.values():
    print(valore)  # Mario, 30, Roma

# Iterare su chiave-valore insieme (CONSIGLIATO)
for chiave, valore in persona.items():
    print(f"{chiave}: {valore}")
# Output:
# nome: Mario
# età: 30
# città: Roma
```

### Metodi utili

```python
persona = {"nome": "Mario", "età": 30}

# Verificare l'esistenza di una chiave
if "nome" in persona:
    print("Chiave 'nome' presente")

# Ottenere tutte le chiavi
chiavi = list(persona.keys())      # ['nome', 'età']

# Ottenere tutti i valori
valori = list(persona.values())    # ['Mario', 30]

# Ottenere coppie chiave-valore
items = list(persona.items())      # [('nome', 'Mario'), ('età', 30)]

# Lunghezza
print(len(persona))  # 2

# Copiare un dizionario
copia = persona.copy()
```

### 🔗 Funzione `zip()` - Creare dizionari da sequenze

La funzione `zip()` **accoppia** elementi di due o più sequenze, creando tuple.

**Sintassi**: `zip(iterabile1, iterabile2, ...)`

```python
# Esempio base
nomi = ["Mario", "Luigi", "Peach"]
età = [30, 28, 25]

# zip crea un iteratore di tuple
coppie = zip(nomi, età)
print(list(coppie))  # [('Mario', 30), ('Luigi', 28), ('Peach', 25)]

# Creare un dizionario da due liste con zip
persone = dict(zip(nomi, età))
print(persone)
# {'Mario': 30, 'Luigi': 28, 'Peach': 25}
```

**Comportamento con lunghezze diverse:**

```python
# zip si ferma alla sequenza più corta
nomi = ["Mario", "Luigi", "Peach"]
età = [30, 28]  # Più corta

risultato = dict(zip(nomi, età))
print(risultato)  # {'Mario': 30, 'Luigi': 28} (Peach ignorato)
```

**Esempio pratico: dati da CSV**

```python
# Intestazione e dati da CSV
intestazione = ["nome", "età", "città"]
riga1 = ["Mario", 30, "Roma"]
riga2 = ["Laura", 25, "Milano"]

# Creare dizionari per ogni riga
persona1 = dict(zip(intestazione, riga1))
persona2 = dict(zip(intestazione, riga2))

print(persona1)  # {'nome': 'Mario', 'età': 30, 'città': 'Roma'}
print(persona2)  # {'nome': 'Laura', 'età': 25, 'città': 'Milano'}

# Lista di dizionari
persone = [dict(zip(intestazione, riga)) 
           for riga in [riga1, riga2]]
```

**Unzip - operazione inversa:**

```python
coppie = [('Mario', 30), ('Luigi', 28), ('Peach', 25)]

# Separare in due liste
nomi, età = zip(*coppie)  # * unpacking
print(list(nomi))  # ['Mario', 'Luigi', 'Peach']
print(list(età))   # [30, 28, 25]
```

### Dizionari nested (annidati)

```python
# Dizionario di dizionari
rubrica = {
    "Mario": {
        "telefono": "123-456",
        "email": "mario@email.com",
        "città": "Roma"
    },
    "Laura": {
        "telefono": "789-012",
        "email": "laura@email.com",
        "città": "Milano"
    }
}

# Accesso ai dati nested
print(rubrica["Mario"]["email"])  # mario@email.com

# Iterazione
for nome, dati in rubrica.items():
    print(f"{nome}: {dati['città']}")
```

---

## 🎛️ Funzioni con Parametri Opzionali

### Tipi di parametri in Python

Python supporta diversi tipi di parametri per le funzioni, che devono seguire un **ordine specifico**.

#### 1. Parametri Posizionali (Formali)

Parametri **obbligatori** passati in base alla loro posizione.

```python
def saluta(nome, cognome):
    return f"Ciao {nome} {cognome}!"

print(saluta("Mario", "Rossi"))  # Ciao Mario Rossi!

# ❌ Errore se mancano parametri
# saluta("Mario")  # TypeError: missing 1 required positional argument
```

#### 2. Parametri con Valori Default

Parametri **opzionali** con un valore predefinito.

```python
def saluta(nome, saluto="Ciao"):
    return f"{saluto} {nome}!"

print(saluta("Mario"))              # Ciao Mario!
print(saluta("Mario", "Buongiorno")) # Buongiorno Mario!

# ⚠️ Default mutabili - ATTENZIONE!
def aggiungi_elemento(elemento, lista=[]):  # ❌ SBAGLIATO!
    lista.append(elemento)
    return lista

print(aggiungi_elemento(1))  # [1]
print(aggiungi_elemento(2))  # [1, 2] <- Lista condivisa!

# ✅ Soluzione corretta
def aggiungi_elemento_corretto(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista

print(aggiungi_elemento_corretto(1))  # [1]
print(aggiungi_elemento_corretto(2))  # [2] <- Lista nuova!
```

#### 3. `*args` - Parametri Posizionali Variabili

Accetta un **numero variabile** di argomenti posizionali come **tupla**.

```python
def somma(*numeri):
    """Somma un numero arbitrario di valori"""
    totale = 0
    for num in numeri:
        totale += num
    return totale

print(somma(1, 2, 3))           # 6
print(somma(1, 2, 3, 4, 5))     # 15
print(somma())                  # 0

# All'interno della funzione, numeri è una tupla
def mostra_args(*args):
    print(f"Tipo: {type(args)}")  # <class 'tuple'>
    print(f"Valori: {args}")
    
mostra_args(1, 2, 3, "hello")
# Tipo: <class 'tuple'>
# Valori: (1, 2, 3, 'hello')
```

**Esempio pratico: funzione di stampa personalizzata**

```python
def stampa_formattato(titolo, *elementi):
    """Stampa un titolo seguito da elementi"""
    print(f"=== {titolo} ===")
    for i, elemento in enumerate(elementi, 1):
        print(f"{i}. {elemento}")

stampa_formattato("Frutti", "Mela", "Banana", "Arancia")
# === Frutti ===
# 1. Mela
# 2. Banana
# 3. Arancia
```

#### 4. `**kwargs` - Parametri Keyword Variabili

Accetta un **numero variabile** di argomenti keyword come **dizionario**.

```python
def crea_profilo(**dati):
    """Crea un profilo con campi arbitrari"""
    print("Profilo creato:")
    for chiave, valore in dati.items():
        print(f"  {chiave}: {valore}")

crea_profilo(nome="Mario", età=30, città="Roma")
# Profilo creato:
#   nome: Mario
#   età: 30
#   città: Roma

# All'interno della funzione, dati è un dizionario
def mostra_kwargs(**kwargs):
    print(f"Tipo: {type(kwargs)}")  # <class 'dict'>
    print(f"Valori: {kwargs}")

mostra_kwargs(a=1, b=2, c="hello")
# Tipo: <class 'dict'>
# Valori: {'a': 1, 'b': 2, 'c': 'hello'}
```

**Esempio pratico: configurazione flessibile**

```python
def configura_server(host, porta, **opzioni):
    """Configura un server con opzioni aggiuntive"""
    print(f"Server: {host}:{porta}")
    print("Opzioni:")
    for chiave, valore in opzioni.items():
        print(f"  {chiave} = {valore}")

configura_server(
    "localhost", 
    8080, 
    debug=True, 
    timeout=30, 
    max_connections=100
)
# Server: localhost:8080
# Opzioni:
#   debug = True
#   timeout = 30
#   max_connections = 100
```

### ⚠️ Ordine OBBLIGATORIO dei parametri

Python richiede un **ordine specifico** nella definizione dei parametri:

```
def funzione(posizionali, default, *args, **kwargs):
    pass
```

**Ordine corretto**:
1. **Parametri posizionali obbligatori** (senza default)
2. **Parametri con default**
3. **`*args`** (parametri posizionali variabili)
4. **`**kwargs`** (parametri keyword variabili)

```python
# ✅ CORRETTO
def funzione_completa(a, b, c=10, *args, **kwargs):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

funzione_completa(1, 2)
# a=1, b=2, c=10
# args=()
# kwargs={}

funzione_completa(1, 2, 3, 4, 5, x=100, y=200)
# a=1, b=2, c=3
# args=(4, 5)
# kwargs={'x': 100, 'y': 200}

# ❌ SBAGLIATO - ordine errato
# def funzione_sbagliata(*args, a, **kwargs):  # SyntaxError!
#     pass
```

### Unpacking di argomenti

Puoi "spacchettare" liste e dizionari in argomenti di funzione:

```python
def somma(a, b, c):
    return a + b + c

# Unpacking di lista con *
numeri = [1, 2, 3]
risultato = somma(*numeri)  # Equivale a somma(1, 2, 3)
print(risultato)  # 6

# Unpacking di dizionario con **
dati = {"a": 10, "b": 20, "c": 30}
risultato = somma(**dati)  # Equivale a somma(a=10, b=20, c=30)
print(risultato)  # 60
```

### Esempio completo: funzione universale

```python
def logger(messaggio, livello="INFO", *tag, **metadata):
    """
    Logger universale con configurazione flessibile
    
    Args:
        messaggio: testo del log
        livello: livello di log (default: INFO)
        *tag: tag aggiuntivi
        **metadata: metadati vari
    """
    print(f"[{livello}] {messaggio}")
    
    if tag:
        print(f"  Tag: {', '.join(tag)}")
    
    if metadata:
        print("  Metadata:")
        for chiave, valore in metadata.items():
            print(f"    {chiave}: {valore}")

# Utilizzo in vari modi
logger("Sistema avviato")
# [INFO] Sistema avviato

logger("Errore critico", "ERROR", "database", "connessione")
# [ERROR] Errore critico
#   Tag: database, connessione

logger(
    "Utente autenticato", 
    "INFO",
    "auth", "security",
    user_id=123,
    ip="192.168.1.1",
    timestamp="2025-01-15"
)
# [INFO] Utente autenticato
#   Tag: auth, security
#   Metadata:
#     user_id: 123
#     ip: 192.168.1.1
#     timestamp: 2025-01-15
```

---

## 🔍 Introspezione (Introspection)

L'**introspezione** è la capacità di esaminare oggetti a runtime per scoprire tipo, attributi e metodi.

### Funzioni di base

#### `type()` - Tipo di un oggetto

```python
x = 42
print(type(x))  # <class 'int'>

l = [1, 2, 3]
print(type(l))  # <class 'list'>

def mia_funzione():
    pass

print(type(mia_funzione))  # <class 'function'>
```

#### `isinstance()` - Verificare il tipo

Controlla se un oggetto è di un **tipo specifico** o sottoclasse.

```python
x = 42

# Singolo tipo
print(isinstance(x, int))     # True
print(isinstance(x, str))     # False

# Multipli tipi (tupla)
print(isinstance(x, (int, float)))  # True (è int)

# Con liste
l = [1, 2, 3]
print(isinstance(l, list))    # True
print(isinstance(l, (list, tuple)))  # True
```

**Quando usare `isinstance()` vs `type()`**:

```python
# type() - confronto esatto
print(type(True) == bool)  # True
print(type(True) == int)   # False (anche se bool eredita da int)

# isinstance() - considera ereditarietà (PREFERIBILE)
print(isinstance(True, bool))  # True
print(isinstance(True, int))   # True (bool è sottoclasse di int)
```

### Esplorare attributi e metodi

#### `dir()` - Elencare tutto

Ritorna una **lista** di tutti gli attributi e metodi di un oggetto.

```python
l = []

# Tutti gli attributi e metodi
print(dir(l))
# ['__add__', '__class__', ..., 'append', 'clear', 'copy', 
#  'count', 'extend', 'index', 'insert', 'pop', 'remove', 
#  'reverse', 'sort']

# Filtrare solo metodi pubblici (senza __)
metodi_pubblici = [m for m in dir(l) if not m.startswith('_')]
print(metodi_pubblici)
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 
#  'insert', 'pop', 'remove', 'reverse', 'sort']
```

#### `hasattr()` - Verificare esistenza

Controlla se un oggetto ha un **attributo o metodo specifico**.

```python
l = []

# Verificare metodi
print(hasattr(l, 'append'))  # True (liste hanno append)
print(hasattr(l, 'items'))   # False (items è dei dizionari)

# Verificare attributi
class Persona:
    def __init__(self, nome):
        self.nome = nome

p = Persona("Mario")
print(hasattr(p, 'nome'))  # True
print(hasattr(p, 'età'))   # False
```

#### `getattr()` - Ottenere attributo

Recupera il valore di un attributo **dinamicamente**.

```python
l = [1, 2, 3]

# Ottenere metodo
metodo_append = getattr(l, 'append')
metodo_append(4)
print(l)  # [1, 2, 3, 4]

# Con default se non esiste
valore = getattr(l, 'items', None)
print(valore)  # None

# Equivalente a
if hasattr(l, 'items'):
    valore = l.items
else:
    valore = None
```

#### `callable()` - Verificare se è chiamabile

Controlla se un oggetto può essere **chiamato come funzione**.

```python
l = []

# Metodi (sono callable)
print(callable(l.append))  # True

# Attributi (non callable)
print(callable(l.__class__))  # True (metaclasse)

# Funzioni
def mia_funzione():
    pass

print(callable(mia_funzione))  # True

# Valori normali
x = 42
print(callable(x))  # False
```

### Esempio pratico: funzione generica

```python
def esegui_se_possibile(oggetto, nome_metodo, *args, **kwargs):
    """
    Esegue un metodo su un oggetto se esiste ed è chiamabile
    """
    if hasattr(oggetto, nome_metodo):
        metodo = getattr(oggetto, nome_metodo)
        if callable(metodo):
            return metodo(*args, **kwargs)
        else:
            print(f"{nome_metodo} non è un metodo chiamabile")
    else:
        print(f"{nome_metodo} non esiste in {type(oggetto).__name__}")

# Test
l = [1, 2, 3]
esegui_se_possibile(l, 'append', 4)  # Funziona
print(l)  # [1, 2, 3, 4]

esegui_se_possibile(l, 'items')  # items non esiste in list
esegui_se_possibile(l, '__class__')  # __class__ non è chiamabile
```

### Introspezione avanzata

```python
# Ottenere documentazione
print(list.append.__doc__)
# L.append(object) -> None -- append object to end

# Ottenere nome della classe
print(type([1, 2, 3]).__name__)  # list

# Verificare se un oggetto ha un attributo __dict__
class MiaClasse:
    def __init__(self):
        self.x = 10

obj = MiaClasse()
print(hasattr(obj, '__dict__'))  # True
print(obj.__dict__)  # {'x': 10}
```

---

## 📚 Libreria Standard di Python

Python include una **libreria standard** ricca di moduli pronti all'uso. Ecco i più comuni per gestione file, sistema e applicazioni.

### 📁 Modulo `os` - Interazione con il Sistema Operativo

Il modulo `os` fornisce funzioni per interagire con il sistema operativo in modo **portabile**.

```python
import os

# Directory corrente
print(os.getcwd())  # /home/user/progetto

# Cambiare directory
os.chdir('/tmp')
print(os.getcwd())  # /tmp

# Listare contenuto di una directory
files = os.listdir('.')
print(files)  # ['file1.txt', 'dir1', 'file2.py']

# Creare directory
os.mkdir('nuova_cartella')  # Crea una directory
os.makedirs('path/to/nested/dir')  # Crea percorso completo

# Rimuovere directory
os.rmdir('nuova_cartella')  # Rimuove directory vuota
os.removedirs('path/to/nested/dir')  # Rimuove percorso (se vuoto)

# Verificare esistenza
if os.path.exists('file.txt'):
    print("File esiste")

if os.path.isfile('file.txt'):
    print("È un file")

if os.path.isdir('cartella'):
    print("È una directory")

# Informazioni su file
stat_info = os.stat('file.txt')
print(stat_info.st_size)  # Dimensione in byte
print(stat_info.st_mtime)  # Timestamp ultima modifica

# Variabili d'ambiente
print(os.environ.get('HOME'))  # /home/user
os.environ['MIA_VAR'] = 'valore'

# Eseguire comandi shell (⚠️ attenzione alla sicurezza!)
os.system('ls -la')  # Sconsigliato, usa subprocess
```

**Esempio pratico: esplorare directory**

```python
import os

def lista_file_ricorsiva(percorso):
    """Elenca tutti i file in modo ricorsivo"""
    for root, dirs, files in os.walk(percorso):
        print(f"\nDirectory: {root}")
        for file in files:
            percorso_completo = os.path.join(root, file)
            dimensione = os.path.getsize(percorso_completo)
            print(f"  {file} ({dimensione} bytes)")

lista_file_ricorsiva('.')
```

---

### 🔧 Modulo `shutil` - Operazioni su File ad Alto Livello

`shutil` offre operazioni su file e directory più avanzate rispetto a `os`.

```python
import shutil

# Copiare file
shutil.copy('source.txt', 'destination.txt')  # Copia file
shutil.copy2('source.txt', 'dest.txt')  # Copia con metadata

# Copiare directory
shutil.copytree('dir_origine', 'dir_destinazione')

# Spostare file o directory
shutil.move('file.txt', '/nuova/posizione/file.txt')

# Rimuovere directory (anche non vuote!)
shutil.rmtree('cartella_da_eliminare')

# Ottenere spazio disco
totale, usato, libero = shutil.disk_usage('/')
print(f"Totale: {totale / (1024**3):.2f} GB")
print(f"Libero: {libero / (1024**3):.2f} GB")

# Creare archivi
shutil.make_archive('backup', 'zip', 'directory_da_archiviare')
# Crea backup.zip

# Estrarre archivi
shutil.unpack_archive('backup.zip', 'directory_destinazione')
```

**Esempio pratico: backup automatico**

```python
import shutil
from datetime import datetime

def crea_backup(cartella_origine, cartella_backup):
    """Crea backup con timestamp"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_backup = f"backup_{timestamp}"
    percorso_backup = os.path.join(cartella_backup, nome_backup)
    
    shutil.copytree(cartella_origine, percorso_backup)
    print(f"Backup creato: {percorso_backup}")

crea_backup('/home/user/documenti', '/home/user/backups')
```

---

### 🛤️ Modulo `pathlib` - Gestione Percorsi Moderna

`pathlib` è l'approccio **object-oriented** moderno per gestire percorsi.

```python
from pathlib import Path

# Creare oggetto Path
p = Path('.')  # Directory corrente
p = Path('/home/user/documenti')
p = Path.home()  # Home directory dell'utente

# Navigare percorsi
documenti = Path.home() / 'documenti' / 'progetti'
file = documenti / 'progetto.py'

print(file)  # /home/user/documenti/progetti/progetto.py

# Proprietà
print(file.name)       # progetto.py
print(file.stem)       # progetto (senza estensione)
print(file.suffix)     # .py
print(file.parent)     # /home/user/documenti/progetti
print(file.parents[1]) # /home/user/documenti

# Verifiche
print(file.exists())    # True/False
print(file.is_file())   # True/False
print(file.is_dir())    # True/False

# Creare directory
nuova_dir = Path('test_dir')
nuova_dir.mkdir(exist_ok=True)  # Non errore se esiste
nuova_dir.mkdir(parents=True)   # Crea percorso completo

# Leggere/Scrivere file
file = Path('dati.txt')
file.write_text('Contenuto del file')
contenuto = file.read_text()

# Con file binari
file.write_bytes(b'\x00\x01\x02')
dati = file.read_bytes()

# Iterare sui file
for file in Path('.').iterdir():
    if file.is_file():
        print(file.name)

# Glob patterns (ricerca file)
for py_file in Path('.').glob('*.py'):
    print(py_file)

# Ricerca ricorsiva
for py_file in Path('.').rglob('*.py'):  # ** in tutti i livelli
    print(py_file)
```

**Esempio pratico: organizzare file per estensione**

```python
from pathlib import Path

def organizza_per_estensione(directory):
    """Sposta file in cartelle per estensione"""
    directory = Path(directory)
    
    for file in directory.iterdir():
        if file.is_file():
            estensione = file.suffix[1:]  # Rimuove il punto
            if estensione:
                cartella_dest = directory / estensione
                cartella_dest.mkdir(exist_ok=True)
                file.rename(cartella_dest / file.name)
                print(f"Spostato {file.name} in {estensione}/")

organizza_per_estensione('download')
```

---

### 📝 Modulo `logging` - Logging Professionale

Il modulo `logging` permette di creare log strutturati e configurabili.

```python
import logging

# Configurazione base
logging.basicConfig(
    level=logging.DEBUG,  # Livello minimo
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',   # Salva su file
    filemode='a'          # Append
)

# Creare logger
logger = logging.getLogger(__name__)

# Livelli di log (dal meno al più grave)
logger.debug('Messaggio di debug')     # Dettagli per debugging
logger.info('Informazione')            # Informazioni generali
logger.warning('Attenzione!')          # Warning
logger.error('Errore!')                # Errore
logger.critical('Errore critico!')     # Errore molto grave

# Con variabili
utente = "Mario"
logger.info(f"Utente {utente} ha effettuato il login")

# Logging di eccezioni
try:
    risultato = 10 / 0
except ZeroDivisionError:
    logger.exception("Errore nella divisione")  # Include traceback
```