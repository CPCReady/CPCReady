CPCEMU v2.5 - Der CPC-Emulator für moderne Computersysteme
----------------------------------------------------------

Was ist CPCEMU ?
  CPCEMU emuliert einen Amstrad-CPC auf Ihrem Computer. Sie benötigen
  mindestens einen AT 386 mit VGA-Grafik.  Die CPC-ROMs, wie sie mit
  deutschen CPCs ausgeliefert wurden, sind mit dabei.


Schneller Einstieg:
DOS:
  Kopieren Sie das Archiv CPCEMU15.ZIP in ein Verzeichnis auf Ihrer
  Festplatte und entpacken es durch  'PKUNZIP CPCEMU15.ZIP' .
  Danach rufen Sie einfach INSTALL.BAT auf. Dann starten Sie
  CPC6128.BAT und können schon einmal "reinschnuppern". 
Linux:
  Kopieren Sie das Archiv cpcemu-linux-*-2.x.tar.gz in ein Verzeichnis
  auf Ihrer Festplatte und entpacken Sie es durch
  'tar xvzf cpcemu-linux-*-2.x.tar.gz'. Dann wechseln Sie mit
  'cd cpcemu-2.x' in das Verzeichnis. Mit './cpc6128' können sie
  schon einmal reinschnuppern. (* durch arm, arm64, x86 oder x86_64 ersetzen)
Windows:
  Kopieren Sie das Installationsprogramm cpcemu-win32-x86-2.x.exe in ein
  Verzeichnis auf Ihrer Festplatte und starten Sie es. Wählen Sie ein
  geeignetes Installationsverzeichnis. Mit "CPCemu/CPC6128" im Startmenü
  können Sie schon einmal reinschnuppern.
MacOS:
  Kopieren Sie die Anwendung in ein Verzeichnis auf Ihrer Festplatte und
  starten Sie sie.
Android:
  Laden Sie die Anwendung auf Ihr Gerät und starten Sie sie.
iOS:
  Laden Sie die Anwendung auf Ihr Gerät und starten Sie sie.


  Die integrierte Online-Hilfe wird mit 'F1' aktiviert. Mit 'F7' und 'T'
  und '1' können Sie die deutsche Tastaturbelegung aktivieren.
  Tiefergehende Erläuterungen können Sie in der umfangreichen
  Dokumentation CPCEMU_D.TXT nachlesen. Keine Bange, sie ist nicht so lang
  wie sie aussieht. Mit Kapitel 6 ist der Anwenderteil zuende.


Neu in v2.5:
------------
  - Floppy LED
  - Virtuelle Tastatur:
    * einstellbar: Position, Größe, Transparenz
    * persistent: speichert Position, Größe, Transparenz automatisch (getrennt für Portrait und Landscape unter Android und iOS)
    * visuelle und akustische (abschaltbar) Rückkopplung
  - Virtueller Joystick in zwei verschiedenen Größen
  - Virtuelle Maus (wahlweise statt Joystick): AMX, Reisware/Gerdes oder Symbiface II (PS/2)
  - Originalgeräusche von Diskettenlaufwerk, Kassettenrelais und Tastatur (abschaltbar)
  - Zoom-Funktion (Anzeige ohne Border), alternierend mit und ohne Vollbild; persistent (getrennt für Portrait und Landscape unter Android und iOS)
  - Audio-Emulation stark überarbeitet und Ausgabequalität deutlich verbessert (4 Ausgabefrequenzen wählbar)
  - Vortex-Speichererweiterung SP64...SP512
  - Jarek-Speichererweiterung 576KB...4096KB
  - Bankswitching-Geschwindigkeit dramatisch verbessert; Korrekte Emulation des C3-Modus
  - IPv6-fähiger Webserver ähnlich M4-Board (Upload und Download in den/vom Emulator per Webinterface)
  - Autostartverhalten verbessert (automatische Dateiauswahl und Deaktivierung)
  - Minimale Audio-Latenz auf Android (Oboe)
  - Bedienung verbessert auf Android/iOS
  - Setup-Einstellungen werden sofort gespeichert
  - Erste Vorbereitungen für neue Benutzeroberfläche
  - An SDL-Version 2.0.22 angepasst
  - Fehler behoben: Hintergrund-Vordergrund-Wechselverhalten unter Android, Echtzeitgeschwindigkeit, Videoausgabegeschwindigkeit (vor allem unter Android, iOS und MacOS), Speicherlecks, M4-Sockets, Dateizugriffe unter Android und iOS


Neu in v2.4:
------------
  - Originale, aber virtuelle CPC-Tastatur in 4 verschiedenen Sprachen
  - Laden von Firmware-ROMs (0 und 255) bei laufendem Emulator
  - Upgrade auf neueste SDL-Version (2.0.18)
  - Behebung vieler Fehler (M4-Dateinamen, M4-Sockets, Tonausgabe, Emulator-Neustart,
    Fehlertoleranz, Bildschirmlayout, Z80-R-Register)


Neu in v2.3:
------------
  - Vollständige Emulation eines M4-Boards (http://www.spinpoint.org) unter
    Verwendung eines Host-Verzeichnisses als Laufwerk C: (SD-Card; auch für SymbOS),
    einschließlich Netzwerk-/Internetverbindungen, dynamischer ROM-Simulation und
    (ersetzbarem) Hack-ROM (lower ROM).
  - CRTC-Emulation für Typ 0 (Register 8) und Typ 1 (Register 6) erheblich verbessert.
  - HYSNC- und VSYNC-Emulation noch weiter verbessert.
  - Online-Hilfe aktualisiert.
  - Mauszeiger bei Bewegung sichtbar
  - Behebung vieler kleiner und großer Fehler (insbesondere funktionieren nun erstmals
    seit Jahrzehnten 576 KB RAM korrekt) und verbesserte Fehlermeldungen.


Neu in v2.2:
------------
  - Einstellungsoption, um Pfeiltasten als Joystick zu benutzen
  - Hauptmenü für kleine Bildschirme optimiert (Android, iOS)
  - Darstellung im CRT-Monitor-Modus ("Video-Modus=1") verbessert (mit
    besserem Fensterverhalten bei Desktop-Versionen außer Linux)
  - Verbesserte Emulation des HSYNC-Signals ("blacker than black",
    relevant für manche Demos wie Dreamend)
  - Fehler behoben: Verzeichnisfreigabe unter Android, Soundausgabe,
    Poke-Datenbank (Android, iOS)


Neu in v2.1:
------------
  - Läuft auf auch auf Linux-x86 (32 Bit) und ARM64 (64 Bit)
  - Weitere Eigenschaften von CRTC (Typen 0 und 1) und Gate Array nachgebildet
    (u. a. Verhalten von Register 6 sowie die Farben)
  - Benutzerschnittstelle verbessert: Textgröße unter Android und iOS,
    Drag & Drop von DSK-Dateien unter Windows, MacOS und Linux
  - Die Versionen für Android und iOS akzeptieren DSK- und ZIP-Dateien
    von anderen Anwendungen (z. B. Downloads aus dem Browser)
  - Weitere Eigenschaften des Diskettencontrollers (FDC) nachgebildet
   (Orion Prime in der 4-Disketten-Version wird jetzt korrekt geladen)
  - Diverse Verbesserungen (z. B. Autostart, Grünmonitor, Kassettenrelais)
   

Neu in v2.0:
------------
  - Läuft auf MacOS, Android, iOS, Linux (x86 und ARM, insbesondere auf
    Raspberry Pi) und Windows
  - Grafik-Engine überholt, bietet jetzt Border, Overscan, dynamische 
    horizontale Synchronisation (noch nicht perfekt), Scan-Doubling und 
	  optional eine gewisse CRT-Unschärfe
  - Komplett neue Emulation des CRTC (Grafikchip des CPC), ziemlich genau 
    und auswählbar zwischen den CRTC-Typen 0, 1 und 2 (die meisten Demos 
	  laufen wie auf einem echten  CPC)
  - Realistisches Timing der CPU-Instructionen und Interrupts
  - Soundemulation signifikant verbessert, jetzt mit Wiedergabe digitalisierter 
    Sounds (wie Sprachausgabe und Spezialeffekte)
  - Verschiedene beschleunigte Arbeitsmodi ("Turbo", mit und ohne
    CRTC-Synchronisation)
  - Debugger mit optionalem CRTC Single-Stepping neben dem CPC-Bildschirm, 
    einschließlich Fadenkreuz an der aktuellen Position des Elektronenstrahls
  - Grafisches Menü (zusätzlich zu den Funktionstasten)
  - Virtueller On-Screen-Joystick unter Android und iOS
  - Verarbeitung von  ZIP-Archiven ohne externes "unzip"
  - Unterstützung von "SNA"-Snapshot-Dateien in V3
  - Tastaturkonfiguration verbessert, erlaubt leichtere Anpassung
  - Viele kleine Verbesserungen vorgenommen und Fehler behoben

Neu in v1.7:
------------
  - Tastaturlayout einstell- und in cpcemu.dat konfigurierbar

Neu in v1.6:
------------
  - Anlagen für ein breiteres Spektrum von Betriebssystemen und CPUs
  - erste Versionen für Linux/x86 und Windows/x86 (ja, es gibt auch
    Windows-Versionen für Non-x86)
  - andere Plattformen sind in Planung (Linux/Alpha, FreeBSD/x86)
  - gesamte Benutzerführung umgesetzt in den Grafikmodus (1 Fenster)
  - ebenso Debugger und andere Eingaben
  - gesamte Grafik- und Soundroutinen neu verfaßt
  - dadurch bessere Multimodedarstellung (ohne Farbenflimmern)
  - gesamter RAM-Zugriff für lineare Adressierung umgebaut
  - Datei- und Verzeichniszugriffe für unixartige OS verallgemeinert
  - Hilfedatei angepaßt und zeichensatzunabhängig
  - außer "descript.ion" wird nun auch "00_index.txt" ausgewertet
  - kleinere Bugfixes
  - leider noch einige Funktionseinschränkungen (Tastaturlayout fest etc.)


Neu in v1.5:
------------
  - perfekter Soundblaster-Sound von Ulrich Doewich
  - vollständige spanische Dokumentation dank Gerardo Briseno
  - angepaßte französische Dokumentation dank Jean-Pierre Marquet
  - Autostart von BASIC-Programmen aus Disketten-Abbildern
  - 4DOS-Beschreibungen bei der Datei-Auswahl
  - die Online-Hilfe erlaubt jetzt Themen mit Leerzeichen
  - Pfade in Konfigurationen werden jetzt relativ abgespeichert
  - Dateiauswahl: Jetzt bis zu 1500 Einträge (vorher 500)
  - direkte Druckerport-Ansteuerung mit PRINTER=""
  - Datenrate bei CPCTRANS v2.3g setzen
  - SNA2GIF v1.2: benutzerdefinierbare Farbpalette, bessere Autoskalierung
  - CPCPARA v1.2: schnelles Senden abschaltbar (z.B. für Vortex)
  - Poke-Datenbank erweitert
  - einige kleinere Änderungen


Neu in v1.4:
------------
  - GUS-Soundunterstützung von Ulrich Doewich
  - Online-Hilfe in Deutsch, Englisch, Französisch und Spanisch
  - vollständige französische Dokumentation
  - Unterstützung für 2 Joysticks
  - VESA-Videomodes für hohe Auflösungen
  - Setup-Menü und Konfigurationsdatei überarbeitet
  - Konfigurationen laden und speichern vom Setup-Menü aus
  - verbesserte FDC-Routinen für Fremdformate
  - Erweitertes Disketten-Format
  - Benutzerdefinierbare Farben und Tasten
  - überarbeitetes CPCTRANS (v2.3)
  - neues SNA2GIF (v1.1) zum Kopieren von Bildern aus Snapshots



Neu in v1.3b:
-------------
  - Auf manchen Soundblaster-Karten (<>Pro) war kein Sound mehr zu hören.


Neu in v1.3a:
-------------
  - In der Version v1.3 funktionierte der Z80-Interrupt Modus 2 nicht mehr,
    so daß z.B. Boulder Dash nicht mehr funktionierte.


Neu in v1.3:
------------
  - Realtime-CPC: In diesem Modus versucht CPCEMU genauso schnell zu sein,
    wie ein echter CPC.
  - die ROMs sind (c) von Amstrad und Locomotive Software
  - französische Dokumentation
  - erweitertes Setup-Menü mit Mausunterstützung
  - Poke-Datenbank zum einfachen "Poken"
  - Disketten-Abbilder mit CPCEMU re-formatieren
  - Disketten-Abbilder mit read-only DOS Attribut einlegen möglich
  - Debug-Menu: 'find' hinzugefügt
  - 'schneller Z80': kann jetzt bei Z80-Befehlen mit Wortzugriff auf 0xffff
    nicht mehr abstürzen
  - paralleler Adapter: neues PCPARA, CPCPARA mit höherer Geschwindigkeit
  - CPCTRANS für 8086 compiliert, damit auf XT einsetzbar
  - usw. ...



  Weitere Informationen finden Sie in der deutschen, englischen,
  französichen oder spanischen Anleitung
    CPCEMU_D.TXT, CPCEMU_E.TXT, CPCEMU_F.TXT bzw. CPCEMU_S.TXT.


Schreiben Sie Ihre Kommentare an:

        Marco Vieth
        Auf dem Ükern 4
        33165 Lichtenau

        oder per E-mail:
          cpcemu@hotmail.com

        oder an:
        Rainer Loritz
        (rainer@loritz.net)

-------------------
