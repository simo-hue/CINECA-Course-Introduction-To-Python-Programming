# DAY 1

## Intro

Pythonic programming

Essendo INTERPRETATO è MOLTO più LENTO

il BYTECODE viene salvato in una sotto cartella __pycache__ ( dove c'è il codice compilato dall'interprete python ), utile per le esecuzioni successive

Si può comunque migliorare la performance cambiando interprete rispetto a quello PYTHON ORIGINALE, ad esempio:
- Cpython
- numba
- PyPy

interprete ipython per i notebbok

## Packages

Un archivio con versioni dove ci sono tutti i moduli python

Ci sono 2 strade: ( Gestori dei pacchetti )
- pip: Easy con linux e mac
- conda: Consigliato per Windows

### PIP

Evitare conflitti tra versioni [IMPORTANTE]

! pip help ci viene restituito tutto il manuale di PIP per aiutarci

! pip list ci dice tutto quello che abbiamo nell'enviroment come pacchetti

! pip show andiamo in dettaglio sul modulo

#### Global

Tutti possono accedere e vedono quell'enviroment python.

Di solito ogni utente ha il suo Global ( ma non può accedere a quello degli altri )

#### User

pip install --user [username]

Anche senza permessi di root un utente può accederci ed evita conflitti con global


## Virtual Enviroment

! python -m venv [NomeAmbiente]
source [NomeAmbiente]/bin/activate

Ora ho il mio ambiente virtuale, e posso iniziare ad installare tutto quello che mi serve senza creare conflitti con la mia macchina e quello che ho installato su di essa

deactivate per uscire dall'ambiente virtuale 

! pip freeze > requirements.txt è UTILISSIMO perchè salvo in un file .txt tutto quello che serve per ricreare il mio ambiente virtuale su un altra macchina

### Conda

è una sorta di virtual enviroment ( ma molto più articolato )

sta virando verso una soluzione a pagamento ( nemmeno più supportato su CLUSTER DI CINECA )

### UV

Enviroment python veloce sviluppato da astral

Potenzialmente interessante


---

## Basics

2 Tipi di numeri:
- interi
- float

python capisce dinamicamente il tipo di una variabile ( provare con print(type(variabile)) )

Anche la variabile in python è sempre considerata un oggetto ( DAY 3 Si approfondisce )

Aggiungere end='' nel print se non voglio andare a capo

### differenza tra '+' e ','

#### L'Operatore Più (+)

Questo è il vero metodo per unire due stringhe in una sola.

Non aggiunge spazi: Incolla le stringhe esattamente come sono.

Richiede tipi identici: Non puoi sommare una stringa e un numero (ti darà errore).

#### La Virgola (,)

La virgola serve a separare gli argomenti. Quando la usi dentro la funzione print(), Python stampa gli elementi uno dopo l'altro.

Aggiunge uno spazio automatico: Tra un elemento e l'altro inserisce di default uno spazio vuoto.

Accetta tipi diversi: Puoi mischiare stringhe, numeri e liste senza problemi.

--- 

scalar instrinsic types and string in python sono IMMUTABILI, quindi significa che non si possono modificare:
'''
a = 2.4
print(id(a))

a = 15
print(id(a))'''

Si vedranno 2 ID diversi

---

### Operatori di Confronto

- is: se è lo stesso oggetto
- ==: se ha lo stesso valore
- classici operatori di confronto

---

### TIPI IN PYTHON ( overflow problems )

per quanto riguarda gli interi python non ha problemi di overflow per la rappresentazione ( cosa che ha nei float )

** elevo a potenza un determinato numero base**esponente

a += 4 [ a = a + 4]
a -= 4 [ a = a - 4]
a /= 4 [ a = a / 4]
a *= 4 [ a = a * 4]

/ divisione in floating point
// divisione con risultato intero

Stare attenti quando si hanno tipi diversi perchè è molto comune é molto comune sbagliare, ecco un esempio:
'''
a = 2.**1023
b = 2**1023
c = 1
print(a)
print(b)
print(c)

print(a + c - b)
'''
RISULTATO: 0.00 ( totalmente sbagliato )

### Stringhe

Si concatenano con il '+'

Posso utilizzare sia "" che '' [ se devo usare ' come simbolo allora devo utilizzare " per non confondere la fine della stringa con il mio carattere ]

### numeri complessi

si possono creare tramite "complex(reale, immaginaria)"

'''
a, b = 12, 3
z = complex(a, b)
print(z)
print(type(z))
'''

Problemi di divisione per zero ( anche quando ci sono degli errori di approssimazione: VEDI CASO PRECEDENTE )

## Costrutti Condizionali

IF - ELSE - ELIF: Suddividere in branch

Ricordarsi sempre i ":"

IF <condizione-1>:
    ISTRUZIONE 1
ELIF <condizione-2>:
    ISTRUZIONE 2
ELSE:
    ISTRUZIONE 3

Come posso concatenare le CONDIZIONI?
- "and" : congiunzione
- "or" : disgiunzione
- "not" : negazione
