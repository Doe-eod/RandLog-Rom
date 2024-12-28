
# RandLog-Rom
```
RandLog-Rom
  von: Sven Rommerskirch
```
* Autor: Sven Rommerskirch
* Getestet: Kali Linux und Windows 11


## Beschreibung
RandLog-Rom wurde von mir geschrieben, um eine Log-Datei mit Testdaten als .csv und .db (SQL) zu erstellen. Diese Datei kann für Analysen zu Trainingszwecken, beispielsweise für angehende Forensiker, genutzt werden. Insgesamt sind 50 User hinterlegt, die zwischen 1 und 5 IP-Adressen besitzen.
Die folgenden Default-Werte sind beim Programmstart hinterlegt:

1. Startdatum der Logs: [01.01.2024]
2. Startuhrzeit der Logs: [01:01:01 Uhr]
3. Enddatum der Logs: [24.12.2024]
4. Enduhrzeit der Logs: [01:01:01 Uhr] 


## Programmstart mit vorkompilierter EXE
Das Python-Programm wurde für Windows-Nutzer vorkompiliert und kann direkt als .exe-Datei heruntergeladen werden. Im Anschluss daran kann diese wie folgt ausgeführt werden:
```
.\RandLog-Rom.exe
```

Die unten aufgeführten Argumente können ebenfalls nach Bedarf mitgegeben werden. Eine Programmausführung mit individuellen Werten kann wie folgt aussehen:
```
.\RandLog-Rom.exe -c 400000 -sd 2023-12-12 -st 01:00:00 -ed 2025-12-12 -et 15:20:56
```


## Programmstart mit Source-Code
Wenn der Sourcode unter Linux oder Windows genutzt werden soll, einfach die folgenden Schritte durchführen:

1. Code herunterladen
2. Entpacken
3. Python installieren
4. Datei RandLog-Rom.py ggf. mit Argumenten ausführen

Insgesamt kann das Programm mit Python, wie folgt, ausgeführt werden:
```
python3 RandLog-Rom.py
```

Hier werden die Default-Werte genutzt.


## Kompilierung mit PyInstaller
Der Source-Code kann für Windows auch mit PyInstaller als EXE kompiliert werden. Dafür kann der folgende Kommand genutzt werden:
```
Powershell öffnen
cd <PFAD ZUR RandLog-Rom.py-DATEI>
pyinstaller --onefile .\RandLog-Rom.py
```



## Argumente
Wenn keine Default-Werte genutzt werden sollen, können die folgenden Argumente mitgegeben werden:

#### Anzahl der Log-Einträge ändern
Syntax:
```
python3 RandLog-Rom.py -c <COUNT>
```

Beispiel:
```
python3 RandLog-Rom.py -c 400000
```


#### Startdatum der Logeinträge ändern
Syntax:
```
python3 RandLog-Rom.py -sd <YYYY-MM-TT>
```

Beispiel:
```
python3 RandLog-Rom.py -sd 2023-12-12
```


#### Startuhrzeit der Logeinträge ändern
Syntax:
```
python3 RandLog-Rom.py -st <HH:MM:SS>
```

Beispiel:
```
python3 RandLog-Rom.py -st 01:00:00
```


#### Enddatum der Logeinträge ändern
Syntax:
```
python3 RandLog-Rom.py -ed <YYYY-MM-TT>
```

Beispiel:
```
python3 RandLog-Rom.py -ed 2025-12-12
```


#### Enduhrzeit der Logeinträge ändern
Syntax:
```
python3 RandLog-Rom.py -et <HH:MM:SS>
```

Beispiel:
```
python3 RandLog-Rom.py -et 15:20:56
```


#### Beispiel mit mehreren Argumenten
```
python3 RandLog-Rom.py -c 400000 -sd 2023-12-12 -st 01:00:00 -ed 2025-12-12 -et 15:20:56
```



## Results
Die Log-Einträge werden in eine CSV-Datei mit der folgenden Namenskonvention gespeichert:
```
test-log_<STARTZEIT>_<ENDZEIT>_<COUNT>.csv
```

Die erstellen Datenbankeinträge werden ebenfalls in diesem Format, allerdings in einer .db-Datei, gespeichert.

