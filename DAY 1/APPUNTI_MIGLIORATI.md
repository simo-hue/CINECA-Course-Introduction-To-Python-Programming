# Python - Giorno 1: Fondamenti e Ambiente di Sviluppo

## 📚 Introduzione a Python

### Caratteristiche del linguaggio

Python è un linguaggio **interpretato**, il che significa che il codice viene eseguito riga per riga senza una fase di compilazione preventiva completa. Questo comporta:

- ✅ **Vantaggi**: Facilità di sviluppo, testing rapido, portabilità
- ⚠️ **Svantaggi**: Performance inferiori rispetto a linguaggi compilati (C, C++, Rust)

#### Il Bytecode e la Cache

Quando esegui uno script Python, l'interprete:
1. Compila il codice sorgente in **bytecode**
2. Salva il bytecode nella cartella `__pycache__/`
3. Riutilizza il bytecode nelle esecuzioni successive (se il file non è modificato)

Questo meccanismo velocizza le esecuzioni successive dello stesso codice.

### Interpreti Python alternativi

Per migliorare le performance è possibile utilizzare interpreti alternativi:

| Interprete | Caratteristiche | Uso consigliato |
|------------|----------------|------------------|
| **CPython** | Implementazione standard, scritta in C | Uso generale, massima compatibilità |
| **PyPy** | JIT compiler, molto veloce | Applicazioni CPU-intensive |
| **Numba** | Compila funzioni specifiche in codice nativo | Calcolo scientifico, NumPy |
| **IPython** | Interprete interattivo avanzato | Jupyter Notebooks, esplorazione dati |

---

## 📦 Gestione Pacchetti e Ambienti

### Package Managers

I principali gestori di pacchetti Python sono:

#### 1. PIP (Python Package Installer)

**Comandi essenziali:**

```bash
# Ottenere aiuto
pip help

# Visualizzare pacchetti installati
pip list

# Informazioni dettagliate su un pacchetto
pip show <nome_pacchetto>

# Installare un pacchetto
pip install <nome_pacchetto>

# Disinstallare un pacchetto
pip uninstall <nome_pacchetto>
```

**Livelli di installazione:**

- **Global**: Pacchetti accessibili da tutti gli utenti (richiede permessi amministrativi)
- **User**: Installazione locale per singolo utente
  ```bash
  pip install --user <nome_pacchetto>
  ```
  Utile quando non si hanno permessi di root e si vogliono evitare conflitti.

#### 2. Conda

- Gestore di pacchetti e ambienti più complesso
- Include anche librerie non-Python (C, C++)
- ⚠️ **Nota**: Sta virando verso un modello commerciale, non più supportato su alcuni cluster HPC (es. CINECA)

#### 3. UV (Nuovo)

- Sviluppato da Astral (creatori di Ruff)
- Promette velocità superiori nella gestione degli ambienti
- Soluzione emergente da monitorare

---

## 🔒 Virtual Environments

### Perché usare gli ambienti virtuali?

Gli ambienti virtuali **isolano** le dipendenze dei progetti, evitando:
- Conflitti tra versioni di librerie
- Problemi di compatibilità
- Inquinamento dell'ambiente globale

### Creazione e gestione

```bash
# Creare un ambiente virtuale
python -m venv <nome_ambiente>

# Attivare l'ambiente (Linux/Mac)
source <nome_ambiente>/bin/activate

# Attivare l'ambiente (Windows)
<nome_ambiente>\Scripts\activate

# Disattivare l'ambiente
deactivate
```

### 💡 Best Practice: Requirements File

Salva tutte le dipendenze del progetto per replicare l'ambiente:

```bash
# Esportare le dipendenze
pip freeze > requirements.txt

# Installare da requirements
pip install -r requirements.txt
```

Questo è **fondamentale** per:
- Condividere progetti con colleghi
- Deployment su server
- Ricreare l'ambiente su altre macchine

---

## 🔢 Tipi di Dati Fondamentali

### Numeri

Python supporta diversi tipi numerici:

#### Interi (`int`)
- **Nessun limite di dimensione** (no overflow come in C/C++)
- Limitati solo dalla memoria disponibile

```python
grande_numero = 2**10000  # Perfettamente valido!
```

#### Float (`float`)
- Numeri in virgola mobile (IEEE 754)
- ⚠️ **Attenzione**: Possono avere problemi di precisione

```python
a = 2.0**1023
b = 2**1023
c = 1.0

# ⚠️ Problema di precisione!
print(a + c - b)  # Output: 0.0 (ERRATO!)
```

#### Numeri Complessi (`complex`)

```python
z = complex(3, 4)  # 3 + 4j
print(z.real)      # 3.0
print(z.imag)      # 4.0
```

### Operatori Aritmetici

| Operatore | Descrizione | Esempio |
|-----------|-------------|---------|
| `+` | Addizione | `5 + 3 = 8` |
| `-` | Sottrazione | `5 - 3 = 2` |
| `*` | Moltiplicazione | `5 * 3 = 15` |
| `/` | Divisione (float) | `5 / 2 = 2.5` |
| `//` | Divisione intera | `5 // 2 = 2` |
| `%` | Modulo (resto) | `5 % 2 = 1` |
| `**` | Potenza | `5 ** 2 = 25` |

**Operatori di assegnazione composti:**

```python
a += 4  # Equivale a: a = a + 4
a -= 4  # Equivale a: a = a - 4
a *= 4  # Equivale a: a = a * 4
a /= 4  # Equivale a: a = a / 4
```

---

## 📝 Stringhe

### Creazione e concatenazione

```python
# Virgolette singole o doppie
stringa1 = 'Hello'
stringa2 = "World"

# Concatenazione con +
messaggio = stringa1 + " " + stringa2  # "Hello World"

# Quando usare ' vs "
citazione = "L'arte della programmazione"  # Usa " per includere '
```

### 🔒 Immutabilità

Tutti i **tipi scalari** in Python sono **immutabili**:
- `int`, `float`, `str`, `bool`, `tuple`

```python
a = 2.4
print(id(a))  # ID: 140234567890

a = 15
print(id(a))  # ID: 140234567999 (DIVERSO!)
```

Quando "modifichi" una variabile, in realtà crei un **nuovo oggetto**.

---

## 🖨️ La Funzione `print()`

### Differenza tra `+` e `,`

```python
nome = "Mario"
eta = 30

# Con + (concatenazione)
print("Nome: " + nome)  # OK
# print("Età: " + eta)  # ❌ ERRORE! Non puoi sommare str e int

# Con , (argomenti separati)
print("Nome:", nome)    # OK: Nome: Mario
print("Età:", eta)      # OK: Età: 30 (aggiunge spazi automatici)
```

**Riassunto:**

| Metodo | Comportamento | Tipi accettati |
|--------|---------------|----------------|
| `+` | Concatenazione stretta | Solo str + str |
| `,` | Argomenti separati con spazi | Qualsiasi tipo |

### Parametro `end`

```python
# Di default va a capo
print("Prima riga")
print("Seconda riga")

# Con end='' rimane sulla stessa riga
print("Tutto sulla", end=" ")
print("stessa riga")
```

---

## ⚖️ Operatori di Confronto

### Confronto di valori

```python
a = 5
b = 5.0

# == confronta il VALORE
print(a == b)  # True (stesso valore)

# is confronta l'IDENTITÀ (stesso oggetto in memoria)
print(a is b)  # False (oggetti diversi)
```

### Operatori disponibili

| Operatore | Significato |
|-----------|-------------|
| `==` | Uguale (valore) |
| `!=` | Diverso |
| `>` | Maggiore |
| `<` | Minore |
| `>=` | Maggiore o uguale |
| `<=` | Minore o uguale |
| `is` | Stessa identità |
| `is not` | Identità diversa |

---

## 🔀 Costrutti Condizionali

### Struttura base

```python
if <condizione>:
    # Blocco eseguito se condizione è True
    istruzione_1
elif <altra_condizione>:
    # Blocco eseguito se la prima è False e questa è True
    istruzione_2
else:
    # Blocco eseguito se tutte le condizioni sono False
    istruzione_3
```

⚠️ **Importante**: Non dimenticare i due punti `:`!

### Operatori Logici

Combina più condizioni con operatori logici:

| Operatore | Descrizione | Esempio |
|-----------|-------------|---------|
| `and` | Congiunzione (entrambe vere) | `x > 0 and x < 10` |
| `or` | Disgiunzione (almeno una vera) | `x < 0 or x > 100` |
| `not` | Negazione | `not x == 5` |

**Esempio pratico:**

```python
temperatura = 25

if temperatura < 0:
    print("Gelo")
elif temperatura >= 0 and temperatura < 20:
    print("Freddo")
elif temperatura >= 20 and temperatura < 30:
    print("Temperato")
else:
    print("Caldo")
```

---

## 🎯 Best Practices

1. **Usa sempre ambienti virtuali** per ogni progetto
2. **Crea `requirements.txt`** per tracciare le dipendenze
3. **Attenzione ai tipi**: Python è tipizzato dinamicamente ma non perdona errori di tipo
4. **Occhio alla precisione dei float** in calcoli critici
5. **Usa `is` per confrontare con `None`**, `==` per i valori
6. **Indentazione**: 4 spazi (standard PEP 8)

---

## 📚 Risorse Utili

- [Documentazione ufficiale Python](https://docs.python.org/3/)
- [PEP 8 - Style Guide](https://pep8.org/)
- [Real Python](https://realpython.com/) - Tutorial e guide avanzate

---

## 🔁 Cicli Iterativi

### Ciclo WHILE

Il ciclo `while` esegue ripetutamente un blocco di codice finché una condizione rimane vera.

#### Sintassi base

```python
while <condizione>:
    # Blocco eseguito finché la condizione è True
    istruzione_1
    istruzione_2
```

#### WHILE con ELSE

Python permette un costrutto particolare: il blocco `else` dopo un ciclo `while`.

```python
while <condizione>:
    # Corpo del ciclo
    if <condizione_break>:
        break
else:
    # Eseguito SOLO se il ciclo termina naturalmente
    # (NON eseguito se si esce con break)
    print("Ciclo completato senza interruzioni")
```

**⚠️ Importante**: Il blocco `else` viene eseguito **se e solo se**:
- Il ciclo termina "correttamente" (condizione diventa `False`)
- **NON** è stato incontrato un `break`

**Esempio pratico:**

```python
# Ricerca di un numero
numero_cercato = 7
numeri = [1, 3, 5, 9, 11]
i = 0

while i < len(numeri):
    if numeri[i] == numero_cercato:
        print(f"Numero {numero_cercato} trovato!")
        break
    i += 1
else:
    # Eseguito solo se NON ho trovato il numero
    print(f"Numero {numero_cercato} non presente nella lista")
```

---

### Ciclo FOR

Il ciclo `for` itera su sequenze (liste, tuple, stringhe, range, ecc.).

#### Sintassi base

```python
for elemento in sequenza:
    # Blocco eseguito per ogni elemento
    print(elemento)
```

#### La funzione `range()`

`range()` genera una sequenza di numeri, molto utile per iterazioni numeriche.

**Sintassi:**
```python
range(start, stop, step)
```

| Parametro | Descrizione | Default |
|-----------|-------------|---------|
| `start` | Valore iniziale (incluso) | 0 |
| `stop` | Valore finale (escluso) | Obbligatorio |
| `step` | Incremento | 1 |

**Esempi:**

```python
# range(stop) - da 0 a stop-1
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# range(start, stop) - da start a stop-1
for i in range(2, 7):
    print(i)  # Output: 2, 3, 4, 5, 6

# range(start, stop, step) - con incremento personalizzato
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8

# step negativo - contare all'indietro
for i in range(10, 0, -1):
    print(i)  # Output: 10, 9, 8, ..., 1
```

#### FOR con ELSE

Anche il ciclo `for` supporta il blocco `else` con la stessa logica del `while`:

```python
for elemento in sequenza:
    if <condizione_break>:
        break
else:
    # Eseguito solo se il ciclo completa tutte le iterazioni
    print("Ciclo completato senza break")
```

**Esempio pratico:**

```python
# Verifica se un numero è primo
numero = 17
is_primo = True

for divisore in range(2, numero):
    if numero % divisore == 0:
        print(f"{numero} non è primo (divisibile per {divisore})")
        is_primo = False
        break
else:
    # Arrivato qui solo se nessun divisore trovato
    print(f"{numero} è un numero primo!")
```

#### Iterare su diverse strutture

```python
# Su stringhe
for carattere in "Python":
    print(carattere)  # P, y, t, h, o, n

# Su liste
frutti = ["mela", "banana", "arancia"]
for frutto in frutti:
    print(frutto)

# Con enumerate() - ottenere indice e valore
for indice, frutto in enumerate(frutti):
    print(f"{indice}: {frutto}")
# Output:
# 0: mela
# 1: banana
# 2: arancia
```

---

## 🎯 Controllo del Flusso nei Cicli

### Istruzioni di controllo

| Istruzione | Funzione |
|------------|----------|
| `break` | Esce immediatamente dal ciclo |
| `continue` | Salta alla prossima iterazione |
| `pass` | Non fa nulla (placeholder) |

**Esempi:**

```python
# break - interrompe il ciclo
for i in range(10):
    if i == 5:
        break  # Esce quando i vale 5
    print(i)  # Output: 0, 1, 2, 3, 4

# continue - salta l'iterazione corrente
for i in range(10):
    if i % 2 == 0:
        continue  # Salta i numeri pari
    print(i)  # Output: 1, 3, 5, 7, 9

# pass - placeholder per codice futuro
for i in range(5):
    if i == 3:
        pass  # Da implementare dopo
    print(i)  # Output: 0, 1, 2, 3, 4
```

---

## 🔧 Funzioni

Le funzioni permettono di **riutilizzare** blocchi di codice, migliorando leggibilità e manutenibilità.

### Definizione base

```python
def nome_funzione(parametro1, parametro2):
    """
    Docstring: descrizione della funzione
    """
    # Corpo della funzione
    risultato = parametro1 + parametro2
    return risultato
```

**Componenti chiave:**
- `def`: parola chiave per definire una funzione
- `nome_funzione`: nome descrittivo (snake_case)
- `parametri`: input della funzione
- `return`: valore restituito (opzionale)

### Esempi pratici

```python
# Funzione semplice
def saluta(nome):
    return f"Ciao, {nome}!"

messaggio = saluta("Marco")
print(messaggio)  # Output: Ciao, Marco!

# Funzione con valori di default
def potenza(base, esponente=2):
    return base ** esponente

print(potenza(5))      # 25 (esponente default = 2)
print(potenza(5, 3))   # 125

# Funzione senza return (restituisce None)
def stampa_info(nome, eta):
    print(f"Nome: {nome}, Età: {eta}")

stampa_info("Alice", 30)  # None viene restituito implicitamente
```

### Parametri posizionali e keyword

```python
def descrive_animale(nome, tipo, eta):
    print(f"{nome} è un {tipo} di {eta} anni")

# Chiamata posizionale
descrive_animale("Fido", "cane", 5)

# Chiamata con keyword arguments (ordine libero)
descrive_animale(eta=3, nome="Whiskers", tipo="gatto")

# Misto (posizionali prima, poi keyword)
descrive_animale("Rex", tipo="cane", eta=7)
```

### Parametri arbitrari

```python
# *args - numero variabile di argomenti posizionali
def somma_tutti(*numeri):
    totale = 0
    for num in numeri:
        totale += num
    return totale

print(somma_tutti(1, 2, 3))        # 6
print(somma_tutti(1, 2, 3, 4, 5))  # 15

# **kwargs - numero variabile di keyword arguments
def stampa_dati(**dati):
    for chiave, valore in dati.items():
        print(f"{chiave}: {valore}")

stampa_dati(nome="Mario", eta=30, citta="Roma")
# Output:
# nome: Mario
# eta: 30
# citta: Roma
```

### Return multipli

```python
# Restituire più valori (come tupla)
def dividi_con_resto(dividendo, divisore):
    quoziente = dividendo // divisore
    resto = dividendo % divisore
    return quoziente, resto

q, r = dividi_con_resto(17, 5)
print(f"Quoziente: {q}, Resto: {r}")  # Quoziente: 3, Resto: 2
```

### Scope delle variabili

```python
x = 10  # Variabile globale

def modifica_variabile():
    x = 5  # Variabile locale (non modifica quella globale)
    print(f"Dentro la funzione: x = {x}")

modifica_variabile()  # Output: Dentro la funzione: x = 5
print(f"Fuori dalla funzione: x = {x}")  # Output: Fuori dalla funzione: x = 10

# Per modificare una globale
def modifica_globale():
    global x
    x = 20

modifica_globale()
print(x)  # Output: 20
```

### Lambda Functions (funzioni anonime)

Funzioni brevi, su una sola riga, utili per operazioni semplici.

```python
# Sintassi: lambda parametri: espressione
quadrato = lambda x: x ** 2
print(quadrato(5))  # 25

# Usate spesso con map, filter, sorted
numeri = [1, 2, 3, 4, 5]
quadrati = list(map(lambda x: x**2, numeri))
print(quadrati)  # [1, 4, 9, 16, 25]

# Con filter
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(pari)  # [2, 4]
```

---

## 💡 Best Practices - Cicli e Funzioni

### Cicli
1. **Preferisci `for` a `while`** quando conosci il numero di iterazioni
2. **Usa `enumerate()`** invece di contatori manuali
3. **Evita cicli infiniti** assicurandoti che la condizione diventi `False`
4. **Usa il costrutto `else`** quando ha senso logico

### Funzioni
1. **Una funzione = un compito**: mantieni le funzioni focalizzate
2. **Nomi descrittivi**: `calcola_media()` è meglio di `calc()`
3. **Docstring**: documenta sempre cosa fa la funzione
4. **Valori di default**: rendono le funzioni più flessibili
5. **Return esplicito**: meglio `return None` che niente
6. **Evita `global`**: passa parametri esplicitamente

**Esempio di funzione ben documentata:**

```python
def calcola_area_cerchio(raggio):
    """
    Calcola l'area di un cerchio dato il raggio.
    
    Args:
        raggio (float): Il raggio del cerchio in unità arbitrarie
        
    Returns:
        float: L'area del cerchio
        
    Raises:
        ValueError: Se il raggio è negativo
    """
    if raggio < 0:
        raise ValueError("Il raggio non può essere negativo")
    
    import math
    return math.pi * raggio ** 2
```

*Prossimo: Giorno 2 - Strutture Dati (Liste, Tuple, Dizionari)*