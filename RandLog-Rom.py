# Datei asdfghjkl.py

import sys
import time
import argparse
import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import sqlite3


class Colors:
    RESET = "\033[0m"           # Farbe zurücksetzen
    BOLD = "\033[1m"            # Fett
    UNDERLINE = "\033[4m"       # Unterstrichen
    BLINK = "\033[5m"           # Blinkend
    INVERTED = "\033[7m"        # Invertiert
    BLACK = "\033[30m"          # Schwarz
    RED = "\033[31m"            # Rot
    GREEN = "\033[32m"          # Grün
    YELLOW = "\033[33m"         # Gelb
    BLUE = "\033[34m"           # Blau
    MAGENTA = "\033[35m"        # Magenta
    CYAN = "\033[36m"           # Türkis
    WHITE = "\033[37m"          # Weiß
    ORANGE = "\033[38;5;208m"   # Orange


nutzer_ip_map = {
    'Alice': ['91.156.182.127', '205.58.213.134', '35.241.112.12', '17.199.232.224'],
    'Bob': ['148.60.72.87', '191.249.37.159', '251.62.91.97', '43.154.64.24'],
    'Charlie': ['187.222.189.175', '187.43.211.112', '54.217.95.192'],
    'David': ['247.161.14.148', '121.149.12.43'],
    'Eve': ['5.132.222.73', '200.36.238.37'],
    'Frank': ['79.166.155.79', '124.15.108.41', '152.129.203.14', '45.247.110.239', '83.154.54.222'],
    'Grace': ['198.43.105.216', '17.237.126.84', '226.146.167.87', '108.238.71.169', '215.180.146.63'],
    'Heidi': ['142.25.53.43', '151.239.56.53', '99.160.34.162', '221.175.172.13'],
    'Ivan': ['108.248.11.249', '104.252.6.226'],
    'Judy': ['140.106.237.207', '4.155.216.68', '193.96.228.132', '130.60.4.188', '117.161.100.157'],
    'Kevin': ['199.109.40.117', '132.39.22.232', '46.181.206.133'],
    'Laura': ['148.22.208.160'],
    'Mike': ['241.173.3.57', '225.11.217.98', '72.33.70.115', '221.1.225.134', '126.92.207.55'],
    'Nancy': ['42.228.151.226', '226.178.252.106', '233.75.239.113', '216.137.44.50'],
    'Oscar': ['216.221.135.132', '49.72.35.195', '41.23.80.95', '38.140.68.100'],
    'Pamela': ['73.162.193.245', '202.224.43.27', '53.148.19.66', '55.140.198.87', '13.184.180.190'],
    'Quinn': ['82.151.224.150'],
    'Riley': ['32.140.7.89', '85.9.209.112', '40.63.133.203', '223.94.112.109'],
    'Steve': ['239.195.53.231', '102.164.112.250'],
    'Tina': ['163.232.216.82', '17.82.83.144', '157.7.110.132', '93.62.0.22'],
    'Uma': ['169.248.50.39', '149.31.90.71'],
    'Victor': ['243.46.251.28', '208.168.254.43'],
    'Wendy': ['136.14.154.82', '165.141.132.1', '209.126.122.245', '133.41.127.231'],
    'Xander': ['221.219.4.133', '211.4.140.88', '208.171.217.129', '52.138.61.183', '235.4.191.77'],
    'Yasmine': ['80.224.123.129','151.145.190.95', '184.31.197.79', '107.255.64.217'],
    'Zara': ['147.4.95.129'],
    'Karle': ['186.91.91.37', '120.38.121.43'],
    'Oskar': ['61.68.36.244', '156.217.216.73', '8.182.87.122', '165.77.239.64'],
    'Udo': ['200.157.1.242', '242.75.66.46'],
    'Thomas': ['58.218.207.210'],
    'Johannes': ['125.179.100.84', '87.193.71.69', '107.244.122.236', '147.69.161.174', '40.46.201.87'],
    'Gregor': ['51.110.248.180', '75.68.157.32', '137.64.98.10'],
    'Sophie': ['194.175.169.71', '3.70.216.61', '58.138.47.59', '207.156.23.98'],
    'Lara': ['14.50.232.190', '66.88.61.49', '131.75.57.30'],
    'Clara': ['22.190.228.188', '223.81.114.40', '126.181.164.65', '133.168.174.93'],
    'Maya': ['159.73.145.36'],
    'Theo': ['128.217.163.28', '202.146.43.13', '249.103.68.225', '153.112.34.128'],
    'Luca': ['3.106.36.187', '57.214.202.29'],
    'Paul': ['79.92.79.60', '45.129.241.95', '73.232.63.6', '137.22.58.129'],
    'Emily': ['196.77.11.119', '214.222.32.142', '5.29.68.78', '8.165.135.127'],
    'Felix': ['121.33.126.13', '45.105.215.130', '177.18.117.79'],
    'Amelie': ['178.77.11.203', '225.143.45.225', '15.171.192.178', '84.96.152.90', '55.161.167.132'],
    'Mia': ['169.133.240.47'],
    'Mariam': ['94.230.67.83', '84.31.193.200', '108.75.61.140'],
    'Thea': ['171.73.34.31', '162.60.251.99'],
    'Paulina': ['71.193.98.223', '138.192.31.150', '254.57.41.215'],
    'Valeria': ['74.24.103.221', '112.223.236.137', '218.226.81.243'],
    'Benedikt': ['170.137.60.146', '48.52.132.200', '73.100.176.186'],
    'Leonardo': ['147.193.156.56'],
    'Aron': ['245.61.134.248', '124.175.31.29', '30.64.153.195', '52.6.219.241']
}


aktionen = ["Login", "Logout", "File Access", "File Modification", "File Creation", "File Deletion", "File Copy", "File Move", "File Rename",
            "File Download", "File Upload", "File Share", "File Unshare", "File Read", "File Write", "File Execute", "Failed Login", "Successfull Login"]


# Startzeit für die zufälligen Zeitstempel
# Format: Jahr, Monat, Tag, Stunde, Minute, Sekunde
default_start_zeit = datetime(2024, 1, 1, 1, 1, 1)

# Endzeit für die zufälligen Zeitstempel
# Format: Jahr, Monat, Tag, Stunde, Minute, Sekunde
default_end_zeit = datetime(2024, 12, 24, 1, 1, 1)

# Anzahl der Test-Einträge
default_anzahl_log_eintraege = 10000

# Benutzereingaben
user_start_date = None
user_start_time = None
user_end_date = None
user_end_time = None
user_counter = None


# Terminalausgabe löschen
def clear_terminal():
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()






# Funktion zur Konsolenausgabe von Text mit delay
def print_with_delay(string_to_print, delay, color):
    for char in string_to_print:
        print(f"{color}{char}{Colors.RESET}", flush=True, end="")
        time.sleep(delay)
    #print()



def show_users_and_ip():
    print_with_delay("\n\n-----------------Output-----------------", 0.01, Colors.ORANGE)
    print_with_delay("\n[*] Testnutzer und IP-Adressen", 0.01, Colors.WHITE)
    
    for user, ips in nutzer_ip_map.items():
        print_with_delay("\n-----------------------------------------------------------------------------------------------------------------\n", 0.0005, Colors.WHITE)
        print_with_delay(f"{user}", 0.0005, Colors.ORANGE)
        for ip in ips:
            print_with_delay(f"   - {ip}", 0.0005, Colors.GREEN)
    
    

def zufaellige_zeitstempel(default_start_zeit, default_end_zeit):  
    # Berechnung der Differenz zwischen Start- und Endzeitpunkt
    delta = default_end_zeit - default_start_zeit
    
    # Generierung eines zufälligen Zeitstempels innerhalb des definierten Zeitraums
    random_date = random.randint(0, int(delta.total_seconds()))
    
    # Rückgabe des zufälligen Zeitstempels
    return default_start_zeit + timedelta(seconds=random_date)




def log_file_generieren(start_zeit, end_zeit, anzahl_log_eintraege):
    start_zeit_str = start_zeit.strftime("%Y-%m-%d_%H-%M-%S")
    end_zeit_str = end_zeit.strftime("%Y-%m-%d_%H-%M-%S")
    dateiname = f"test-log_{start_zeit_str}_{end_zeit_str}_{anzahl_log_eintraege}.csv"
    print_with_delay("\n\n-----------------Output-----------------", 0.01, Colors.ORANGE)
    print_with_delay("\n[*] Generiere Datei für Testlogs: " + dateiname, 0.01, Colors.WHITE)

    with open(dateiname, mode='w', newline='') as file:

        # Ein Writer-Objekt wird erstellt
        writer = csv.writer(file)
        writer.writerow(["Zeitstempel", "Name", "IP-Adresse", "Aktion"])

        # Schleife für die Anzahl der Log-Einträge
        for anzahl in range(anzahl_log_eintraege):
            # Zufälliger Zeitstempel
            time = zufaellige_zeitstempel(start_zeit, end_zeit).strftime("%Y-%m-%d %H:%M:%S")
            
            # Zufälliger Nutzername
            name = random.choice(list(nutzer_ip_map.keys()))
            
            # Zufällige IP-Adresse
            ip = random.choice(nutzer_ip_map[name])
            
            # Zufällige Aktion
            action = random.choice(aktionen)
            
            # Schreibt die generierten Daten in die Datei
            writer.writerow([time, name, ip, action])

    print_with_delay("\n[*] Datei wurde erfolgreich erstellt.", 0.01, Colors.WHITE)
    return dateiname



def create_sql_file(dateiname_):
    print_with_delay("\n\n-----------------Output-----------------", 0.01, Colors.ORANGE)
    print_with_delay("\n[*] Exportiere Log-Einträge als SQL-Datei", 0.01, Colors.WHITE)
    
    # CSV-Datei einlesen
    with open(dateiname_, mode='r') as file:
        
        # Ein Reader-Objekt wird erstellt
        reader = csv.reader(file)
        
        # Header wird übersprungen
        next(reader)

        # Ersetze Dateiendung .csv durch .sql
        dateiname_db = dateiname_.replace(".csv", ".db")
    
        # DB-Datei erstellen
        con = sqlite3.connect(dateiname_db)
        
        # Cursor-Objekt erstellen
        cur = con.cursor()
        
        # Tabelle erstellen
        cur.execute("""CREATE TABLE IF NOT EXISTS testlogs (Zeitstempel TEXT, Name TEXT, IP_Adresse TEXT, Aktion TEXT)""")
        
        # Daten aus CSV in die Datenbank schreiben
        for row in reader:
            cur.execute("""INSERT INTO testlogs VALUES (?, ?, ?, ?)""", row)

        # Änderungen speichern
        con.commit()
        
        # Verbindung schließen
        con.close() 

    print_with_delay("\n[*] SQL-Datei wurde erfolgreich erstellt.", 0.01, Colors.WHITE)




def main():
    # Terminal löschen
    clear_terminal()
    
    # Banner anzeigen
    banner = """

    .:::d88888a88888888888a88888b:::.
   ::::dP:::::::888888888:::::::Yb::::
  ::::dP::::::::Y8888888P::::::::Yb::::
 ::::b8::::::::::Y88888P::::::::::8b::::
.:::88::::::::::::Y888P:::::::::::88::::.
::::Y8baaaaaaaaa88P:T:Y88aaaaaaaad8P:::::
::::::Y8888888888P::I::Y888888888P:::::::
   
                RandLog-Rom
    Developed by Sven Rommerskirch
    """
    print_with_delay(banner, 0.001, Colors.RED)
    
    # Erstelle ein Argumentparser-Objekt mit einer Beschreibung
    arg_parser = argparse.ArgumentParser(
        description=("Das Programm erstellt eine beliebig große Log-Datei im Format YYYY-MM-TT HH:MM:SS,NAME,IP-ADRESSE,AKTION.\n"
                     "Es wurden insgesamt 50 Nutzernamen hinterlegt, die zwischen 1 und 5 IP-Adressen besitzen.\n\n"
                     "-----------------Default-Argumente-----------------\n"
                     "Werden dem Programm keine Argumente mitgegeben, werden die folgenden Default-Werte für die Generierung der Testeinträge gesetzt:\n"
                     "Startdatum: 01.01.2024\n"
                     "Enddatum: 01.01.2024\n"
                     "Startuhrzeit: 01:01:01 Uhr\n"
                     "Enduhrzeit: 01:01:01 Uhr\n\n"
                     "-----------------Entwickler-----------------\n"
                     "Autor: Sven Rommerskirch\n"
                     "Datum: 24.12.2024\n"
                     ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Argumente werden gesetzt
    arg_parser.add_argument("-sd", "--start-date", help="Hier kann das Startdatum im Format YYYY-MM-TT mitgegeben werden. Der Default-Wert für das Startdatum wird auf den 01.01.2024 gesetzt.", required=False)
    arg_parser.add_argument("-st", "--start-time", help="Hier kann die Startuhrzeit im Format HH:MM:SS mitgegeben werden. Der Default-Wert für die Startuhrzeit wird auf 01:01:01 Uhr gesetzt.", required=False)
    arg_parser.add_argument("-ed", "--end-date", help="Hier kann das Enddatum im Format YYYY-MM-TT mitgegeben werden. Der Default-Wert für das Enddatum wird auf den 24.12.2024 gesetzt.", required=False)
    arg_parser.add_argument("-et", "--end-time", help="Hier kann die Enduhrzeit im Format HH:MM:SS mitgegeben werden. Der Default-Wert für die Enduhrzeit wird auf 01:01:01 Uhr gesetzt.", required=False)
    arg_parser.add_argument("-c", "--counter", help="Mit dem Counter kann die Anzahl der Log-Einträge festgelegt werden. Der Default-Wert beträgt 10.000 Einträge über den gesetzten Zeitraum.", required=False)
    
    # Argumente werden geparst
    arg_parser = arg_parser.parse_args()
    
    
    # Prüft, ob das Argument mitgegeben wurde und ein gültiges Datum ist
    if arg_parser.start_date:
        try:
            user_start_date = datetime.strptime(arg_parser.start_date, "%Y-%m-%d")
        except ValueError as e:
            print_with_delay(f"Ungültiges Datumsformat: {arg_parser.start_date}. Das Format muss YYYY-MM-TT sein.", 0.05, Colors.RED)
            # Programm wird mit einem Fehler beendet (exit(0) ist beenden ohne Fehler)
            exit(1)
    else:
        user_start_date = default_start_zeit.date()
    
    # Prüft, ob das Argument mitgegeben wurde und eine gültige Zeit ist
    if arg_parser.start_time:
        try:
            user_start_time = datetime.strptime(arg_parser.start_time, "%H:%M:%S").time()
        except ValueError as e:
            print_with_delay(f"Ungültiges Zeitformat: {arg_parser.start_time}. Das Format muss HH:MM:SS sein.", 0.05, Colors.RED)
            exit(1)
    else:
        user_start_time = default_start_zeit.time()
    
    # Prüft, ob das Argument mitgegeben wurde und ein gültiges Datum ist
    if arg_parser.end_date:
        try:
            user_end_date = datetime.strptime(arg_parser.end_date, "%Y-%m-%d")
        except ValueError as e:
            print_with_delay(f"Ungültiges Datumsformat: {arg_parser.end_date}. Das Format muss YYYY-MM-TT sein.", 0.05, Colors.RED)
            exit(1)
    else:
        user_end_date = default_end_zeit.date()
    
    # Prüft, ob das Argument mitgegeben wurde und eine gültige Zeit ist
    if arg_parser.end_time:
        try:
            user_end_time = datetime.strptime(arg_parser.end_time, "%H:%M:%S").time()
        except ValueError as e:
            print_with_delay(f"Ungültiges Zeitformat: {arg_parser.end_time}. Das Format muss HH:MM:SS sein.", 0.05, Colors.RED)
            exit(1)
    else:
        user_end_time = default_end_zeit.time()
    
    # Prüft, ob das Argument mitgegeben wurde und eine positive Ganzzahl > 0 ist
    if arg_parser.counter:
        try:
            user_counter = int(arg_parser.counter)
            if user_counter <= 0:
                raise ValueError("Counter muss größer als 0 sein.")
        except ValueError:
            print_with_delay(f"Ungültiger Counter: {arg_parser.counter}. Der Counter muss eine positive Ganzzahl > 0 sein.", 0.05, Colors.RED)
            exit(1)
    else:
        user_counter = default_anzahl_log_eintraege
    
    
    # Zusammenführung der Benutzereingaben in Startdatum und Startuhrzeit
    final_start_datetime = datetime.combine(
        user_start_date if user_start_date else default_start_zeit.date(),
        user_start_time if user_start_time else default_start_zeit.time()
    )
    
    # Zusammenführung der Benutzereingaben in Enddatum und Enduhrzeit
    final_end_datetime = datetime.combine(
        user_end_date if user_end_date else default_end_zeit.date(),
        user_end_time if user_end_time else default_end_zeit.time()
    )
    
    # Setzt den Counter
    final_anzahl_log_eintraege = user_counter if user_counter else default_anzahl_log_eintraege
    
    # Ausgabe der verwendeten Daten
    print_with_delay(f"\nStartdatum und Uhrzeit: {final_start_datetime}", 0.01, Colors.GREEN)
    print_with_delay(f"\nEnddatum und Uhrzeit: {final_end_datetime}", 0.01, Colors.GREEN)
    print_with_delay(f"\nCounter: {final_anzahl_log_eintraege}", 0.01, Colors.GREEN)
    

    # Ausgabe der Testnutzer und IP-Adressen
    show_users_and_ip()
    
    # Generierung der Log-Datei als CSV
    dateiname_ = log_file_generieren(final_start_datetime, final_end_datetime, final_anzahl_log_eintraege)

    # Logs als SQL-Datei exportieren
    create_sql_file(dateiname_)





if __name__ == '__main__':
    main()
    
