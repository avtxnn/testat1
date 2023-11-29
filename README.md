## ALteP Testat ``1``

Das erste Testat ist nah am Probetestat orientiert. Es sollen zwei Funktionen vervollständigt und Probleme mit einer Funktion korrigiert werden.


## Allgemeines Vorgehen
- Repository clonen
- **Es muss kein neuer Branch angelegt werden, es darf direkt auf ``main`` gepusht werden**
- Aufgabe bearbeiten/Änderungen jederzeit pushen
- **HINWEIS: NUR DIE ``aufgabe_*.py``-FILES SOLLEN EDITIERT WERDEN!**
- Namen der Funktionen **nicht** ändern, nur den Inhalt ändern!


## Aufgaben

### Aufgabe 1: Vervollständige die Funktionen
- Vervollständige die Funktionen in aufgabe_1.py
- `add_numbers()` soll die zwei übergebenen Zahlen addieren und das Ergebnis zurückgeben
- `rectangle_calculate_area()` soll die Fläche eines Rechtecks berechnen und zurückgeben
  - An die Funktion übergeben werden die Argumente `length` und `width`, welche die zwei Seitenlängen des Rechtecks sind


### Aufgabe 2: Debugging
- Die Funktion `get_primenumbers(n)` soll die Primzahlen im Bereich 0..n (**inklusive** n) als Liste zurückgeben
- Aufgabenbeschreibung:
  - Das Skript bricht mit zwei Fehlern ab, finde und korrigiere beide Fehler
    - Bei beiden Fehlern muss **kein** Code hinzugefügt werden!
  - Die letzten Primzahlen sind nicht inklusive, finde und korrigiere den Fehler
- Hinweise:
  - Die Funktion besteht aus zwei For-Schleifen:
    - Die erste Schleife iteriert über den Bereich 2..n
    - Die zweite Schleife iteriert bis vor die aktuelle Zahl der ersten Schleife und versucht einen ganzzahligen Teiler zu finden. Gibt es keinen ganzzahligen Teiler, wird die Zahl der Primzahlen-Liste hinzugefügt.
  - Es kann bspw. der Debugger benutzt werden, um das Problem zu identifizieren
  - Die Fehlermeldung selbst gibt auch Auskunft darüber, wo das Problem sein könnte