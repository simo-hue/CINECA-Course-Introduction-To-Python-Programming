# 🐍 Corso Python - CINECA

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()
[![CINECA](https://img.shields.io/badge/CINECA-2025-orange.svg)](https://www.cineca.it/)

Repository contenente materiali didattici, appunti ed esercizi del corso **"Introduction to Python Programming"** organizzato da CINECA.

---

## 📚 Contenuti del Corso

### [DAY 1](./DAY%201) - Fondamenti di Python
- **Argomenti**: Introduzione a Python, ambienti virtuali, sintassi base, controllo del flusso, funzioni
- **Materiali**:
  - [Appunti migliorati](./DAY%201/APPUNTI_MIGLIORATI.md)
  - [Appunti pomeriggio](./DAY%201/APPUNTI_POMERIGGIO.md)
  - [Risorse originali](./DAY%201/RISORSE)
- **Esercizi**: `hands_on_2.1.py`, `hands_on_3.1.py`, `hands_on_3.2.py`, `hands_on_4.1.py`

### [DAY 2](./DAY%202) - Strutture Dati e Libreria Standard
- **Argomenti**: Dizionari, liste, tuple, set, funzioni avanzate, introspezione, moduli standard (os, pathlib, datetime, logging, ecc.)
- **Materiali**:
  - [Appunti mattina migliorati](./DAY%202/APPUNTI_MATTINA_MIGLIORATI.md)
  - [Appunti pomeriggio migliorati](./DAY%202/APPUNTI_POMERIGGIO_MIGLIORATI.md)
  - [Risorse ed esercizi](./DAY%202/RISORSE)
- **Esercizi pratici**: Caesar Cipher, Triangle Wave, statistiche 100m

### [DAY 3](./DAY%203) - Programmazione Avanzata
- **Argomenti**: Decoratori, eccezioni, classi e OOP, iterables/iterators/generators
- **Materiali**:
  - [Appunti completi](./DAY%203/APPUNTI.md)
  - [Risorse ed esempi](./DAY%203/RISORSE)
- **Esempi**: `decoratori.py`, `primo_esempio.py`

---

## 🚀 Setup Ambiente di Sviluppo

### Prerequisiti
- Python 3.13 (o superiore)
- pip

### Installazione

1. **Clona la repository**
   ```bash
   git clone <url-repository>
   cd <nome-repository>
   ```

2. **Crea un ambiente virtuale**
   ```bash
   python -m venv corso-python
   ```

3. **Attiva l'ambiente virtuale**
   
   - **Linux/Mac**:
     ```bash
     source corso-python/bin/activate
     ```
   
   - **Windows**:
     ```bash
     corso-python\Scripts\activate
     ```

4. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

### Dipendenze principali
- `jupyter` - Notebook interattivi
- `ipython` - Shell interattiva avanzata
- `numpy` - Calcolo numerico
- `matplotlib` - Visualizzazione dati
- Altre librerie specificate in `requirements.txt`

---

## 📂 Struttura della Repository

```
.
├── DAY 1/                          # Giorno 1: Fondamenti
│   ├── APPUNTI_MIGLIORATI.md      # Appunti completi e formattati
│   ├── RISORSE/                    # Notebook e materiali originali
│   └── hands_on_*.py               # Esercizi pratici
│
├── DAY 2/                          # Giorno 2: Strutture dati
│   ├── APPUNTI_MATTINA_MIGLIORATI.md
│   ├── APPUNTI_POMERIGGIO_MIGLIORATI.md
│   ├── RISORSE/                    # Esercizi e notebook
│   └── *.py                        # Script di esempio
│
├── DAY 3/                          # Giorno 3: OOP e avanzati
│   ├── APPUNTI.md
│   ├── RISORSE/                    # Materiali avanzati
│   └── esempio_*.py                # Esempi di codice
│
├── python-intro-2025/              # Repository originale del corso
├── back up/                        # Backup dei materiali
├── corso-python/                   # Ambiente virtuale
├── requirements.txt                # Dipendenze Python
├── to_do_exercises.txt             # Lista esercizi da completare
└── README.md                       # Questo file
```

---

## 🔗 Link Utili

### Risorse del Corso
- 📖 [**Materiali Didattici Ufficiali**](https://learn.cineca.it/course/view.php?id=2173)
- 🎓 [**Pagina Evento CINECA**](https://eventi.cineca.it/en/hpc/introduction-python-programming/line-event-20251119)
- 💻 [**Teams - Lezioni Online**](https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZjExMmNkM2MtZGJmZC00NTU2LWFkYjgtZjFhMjA4NjE4MzRm%40thread.v2/0?context=%7b%22Tid%22%3a%22c5492249-84a0-43af-bd29-a7892e94b5b7%22%2c%22Oid%22%3a%227dc2a2cf-e65b-4b39-90c4-cba2c4a6b653%22%7d)

### Corsi Avanzati
- 🚀 [**Python Scientific/Advanced - CINECA**](https://gitlab.hpc.cineca.it/cineca-hpyc/python-scientific-2024/-/tree/main/lectures?ref_type=heads)

### Documentazione Python
- 📚 [Python Official Documentation](https://docs.python.org/3/)
- 🎯 [Real Python Tutorials](https://realpython.com/)
- 📖 [Python Package Index (PyPI)](https://pypi.org/)

---

## 📝 Esercizi e Hands-On

### Esercizi Completati
- ✅ Triangle Wave (`DAY 2/RISORSE/05_exercise_triangle_wave.ipynb`)
- ✅ Caesar Cipher (`DAY 2/RISORSE/06_exercise_caesar_cipher.ipynb`)
- ✅ Statistiche 100m (`DAY 2/times_100m.dat`)

### Esercizi da Completare
Consulta il file [`to_do_exercises.txt`](./to_do_exercises.txt) per la lista aggiornata degli esercizi da svolgere.

---

## 🛠️ Strumenti Utilizzati

- **IDE/Editor**: VSCode, PyCharm, Jupyter Lab
- **Versione Python**: 3.13
- **Gestione Pacchetti**: pip, venv
- **Notebook**: Jupyter Notebook/Lab
- **Version Control**: Git/GitHub

---

## 📊 Argomenti Trattati

<details>
<summary><b>Fondamenti (DAY 1)</b></summary>

- Introduzione a Python e storia del linguaggio
- Installazione e configurazione ambiente
- Ambienti virtuali (venv)
- Tipi di dati base (int, float, str, bool)
- Operatori e espressioni
- Strutture di controllo (if, for, while)
- Funzioni e scope delle variabili
- Liste, tuple e operazioni base

</details>

<details>
<summary><b>Strutture Dati Avanzate (DAY 2)</b></summary>

- Dizionari e operazioni avanzate
- Set e operazioni insiemistiche
- List/Dict comprehensions
- Funzione `zip()` e unpacking
- Parametri funzioni: `*args` e `**kwargs`
- Introspezione (`type`, `isinstance`, `hasattr`, `callable`)
- Moduli libreria standard:
  - `os` - Interazione con il sistema operativo
  - `shutil` - Operazioni su file
  - `pathlib` - Path object-oriented
  - `logging` - Sistema di logging
  - `argparse` - Parser argomenti CLI
  - `subprocess` - Esecuzione processi esterni
  - `datetime` - Gestione date e orari

</details>

<details>
<summary><b>Programmazione Avanzata (DAY 3)</b></summary>

- Decoratori (function decorators)
- Gestione eccezioni (try, except, finally)
- Classi e Object-Oriented Programming
  - Attributi e metodi
  - Ereditarietà e polimorfismo
  - Metodi speciali (`__init__`, `__str__`, ecc.)
- Iterables, Iterators e Generators
- Context managers (`with` statement)

</details>

---

## 🎯 Obiettivi di Apprendimento

Al termine del corso sarai in grado di:

- ✨ Scrivere programmi Python efficienti e leggibili
- 🔧 Utilizzare le strutture dati appropriate per ogni situazione
- 📦 Gestire progetti Python con ambienti virtuali e dipendenze
- 🐛 Debuggare e gestire errori in modo professionale
- 📝 Documentare il codice seguendo le best practices
- 🚀 Applicare principi di programmazione Object-Oriented
- 🔍 Utilizzare i moduli della libreria standard Python

---

## 💡 Best Practices Imparate

1. **Naming Conventions**: Seguire PEP 8 per nomi di variabili, funzioni e classi
2. **Docstrings**: Documentare funzioni e classi con docstring descrittive
3. **Type Hints**: Utilizzare annotazioni di tipo per migliorare la leggibilità
4. **List Comprehensions**: Preferire comprehensions ai loop quando appropriato
5. **Context Managers**: Usare `with` per gestire risorse (file, connessioni)
6. **Logging**: Implementare logging invece di `print()` per debugging
7. **Virtual Environments**: Sempre usare ambienti virtuali per progetti
8. **Error Handling**: Gestire eccezioni in modo specifico, evitare `except:` generico

---

## 📌 Note

- Gli appunti con suffisso `_MIGLIORATI.md` sono versioni estese e formattate degli appunti originali
- La cartella `RISORSE/` in ogni DAY contiene i notebook Jupyter originali del corso
- La cartella `back up/` contiene una copia di sicurezza di tutti i materiali
- L'ambiente virtuale `corso-python/` non è tracciato da Git

---

## 📧 Contatti e Supporto

Per domande o chiarimenti sul corso:
- **CINECA Support**: Consulta la piattaforma [learn.cineca.it](https://learn.cineca.it)
- **Repository Issues**: Apri una issue su GitHub per problemi con il codice

---

## 📜 Licenza

Materiali didattici forniti da **CINECA** per scopi educativi.

---

## 🙏 Ringraziamenti

Un ringraziamento speciale a:
- **CINECA** per l'organizzazione del corso
- Gli **istruttori** per i materiali didattici di qualità
- La community **Python** per la documentazione eccellente

---

<div align="center">

**Happy Coding! 🚀**

*Ultimo aggiornamento: Novembre 2025*

</div>