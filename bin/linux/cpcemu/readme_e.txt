CPCEMU v2.5 - The CPC Emulator for modern computer systems
----------------------------------------------------------

What is CPCEMU ?
  CPCEMU emulates an Amstrad CPC on your computer. You need at least an
  AT 386 with VGA graphics.  The CPC ROMs as shipped in UK are included.


Fast start:
DOS:
  Copy the archive CPCEMU15.ZIP into a directory of your hard disk and
  decompress it with  'PKUNZIP CPCEMU15.ZIP' .
  Then use INSTALL.BAT. Now run CPC6128.BAT to have a first look.
Linux:
  Copy the archive cpcemu-linux-*-2.x.tar.gz into a directory of your
  hard disk and decompress it with 'tar xvzf cpcemu-linux-*-2.x.tar.gz'.
  Then change the directory with 'cd cpcemu-2.x'. Now run './cpc6128' to
  have a first look. (replace * by arm, arm64, x86 or x86_64)
Windows:
  Copy the setup program cpcemu-win32-x86-2.x.exe into a directory of your
  hard disk and start it. Select a directory to install. Now use
  'CPCemu/CPC6128' in start menu to have a first look.
MacOS:
  Copy the Application to a folder of your hard disk and start it.
Android:
  Download the Application on your device and start it.
iOS:
  Download the Application on your device and start it.


  You can try the new online help by pressing F1.
  When questions arise, simply read the completely new documentation
  CPCEMU_E.TXT. No panic, it is shorter as it seems at the first glance.
  The user part ends with chapter 6.


New in v2.5:
------------
  - Floppy LED
  - Virtual keyboard:
    * adjustable: position, size, transparency
    * persistent: saves position, size, transparency automatically (separately for portrait and landscape on Android and iOS)
    * visual und acoustic (switchable) feedback
  - Virtual joystick in two different sizes
  - Virtual mouse (selectable instead of joystick): AMX, Reisware/Gerdes or Symbiface II (PS/2)
  - Original sounds von disk drive, cassette relay and keyboard (switchable)
  - Zoom function (display without border), alternating with and without full screen; persistent (separately for portrait and landscape on Android and iOS)
  - Audio emulation deeply revised; output quality significantly improved (select between 4 output frequencies)
  - Vortex memory extension SP64...SP512
  - Jarek memory extension 576KB...4096KB
  - Bank-switching speed dramatically improved; correct emulation of C3 mode
  - IPv6-enabled web server similar to M4 board (upload and download into/from the emulator via web interface)
  - Autostart behaviour improved (automatic file selection and deactivation)
  - Minimale audio latency on Android (Oboe)
  - User interface improved on Android/iOS
  - Setup settings are saved immediately
  - First preparations for new user interface
  - Adjusted to SDL version 2.0.22
  - Fixed bugs: background-foreground-changing behaviour on Android, real-time speed, video output speed (in particular on Android, iOS and MacOS), memory leaks, M4 sockets, file access on Android and iOS


New in v2.4:
------------
  - Original, but virtual CPC keyboard in 4 different languages
  - Loading firmware ROMs (0 and 255) from the running emulator
  - Upgrade to latest SDL version (2.0.18)
  - Correction of many errors (M4 file names, M4 sockets, sound output, restart of emulation,
    error tolerance, screen layout, Z80 R register)


New in v2.3:
------------
  - Complete emulation of an M4 Board (http://www.spinpoint.org) using a host
    directory as drive C: (SD card; even for SymbOS), including network/internet
    connections, dynamic ROM simulation and (replaceable) Hack ROM (lower ROM).
  - CRTC emulation of type 0 (register 8) and type 1 (register 6) vastly improved.
  - HYSNC and VSYNC emulation improved even further.
  - Online help updated.
  - Mouse pointer visible on movements
  - Correction of many small and big errors (in particular, 576 KB RAM work
    correctly now for the first time after decades) and improved error reporting.


New in v2.2:
------------
  - Setup option to use arrow keys as joystick
  - Main menu improved for small screens (Android, iOS)
  - Improved output in CRT-monitor mode ("Video mode=1", including
    better window behaviour for desktop versions)
  - Improved emulation of the HSYNC signals ("blacker than black",
    relevant for some demos as Dreamend)
  - Fixed errors: Folder sharing on Android, sound output,
    poke database (Android, iOS)


New in v2.1:
------------
  - Runs also on Linux-x86 (32 Bit) and ARM64 (64 Bit)
  - Further features of CRTC (types 0 and 1) and Gate Array imitated
    (e. g. behaviour of register 6, and the colours)
  - User interface improved: text size on Android and iOS,
    Drag & Drop of DSK files on  Windows, MacOS and Linux
  - The versions for Android and iOS accept DSK and ZIP files
    from other applications (e. g. downloads from the browser)
  - Further features of the disk controller (FDC) imitated
   (Orion Prime in the 4 disk version loads correctly now)
  - Multiple improvements (e. g. autostart, green monitor, cassette relay)

New in v2.0:
------------
  - Runs on MacOS, Android, iOS, Linux (x86 and ARM, in particular on
    Raspberry Pi) and Windows
  - Graphics engine overhauled, introducing border, overscan, dynamic 
    horizontal synchronisation (not perfect yet), scan doubling and 
	some optional CRT blurring
  - Completely new CRTC (CPC's graphics chip) emulation, quite accurate 
    and selectable between CRTC types 0, 1 and 2 (most demos work as on a 
	real CPC)
  - Realistic timing of CPU instructions and interrupts
  - Sound emulation significantly improved, now able to play digitized 
    sounds (such as speech and special effects)
  - Different accelerated modes of operation ("Turbo", with and without 
    CRTC synchronisation)
  - Debugger with optional CRTC single-stepping alongside the CPC screen, 
    including crosshairs indicating the current electron beam position
  - Graphical menu (in addition to function keys)
  - Virtual on-screen joystick on Android and iOS
  - Support for ZIP archives without external "unzip"
  - Support for V3 "SNA" Snapshot files
  - Keyboard configuration improved, enabling easier customization
  - Many small improvements and bug fixes

New in v1.7:
------------
  - Keyboard layout is adjustable and, in cpcemu.dat, configurable

New in v1.6:
------------
  - Changes for a wider spectrum of operating systems and CPUs
  - first versions for Linux/x86 and Windows/x86 (yes, there are
    indeed versions of Windows for Non-x86)
  - other plattforms are being planned (Linux/Alpha, FreeBSD/x86)
  - whole user interface converted to graphics mode (1 window)
  - same for debugger and other user inputs
  - completetly new graphics and sound routines
  - hence, better multimodes are depicted better (without flickering colours)
  - whole RAM access converted to linear addressing mode
  - file and directory access generalized for unixish OSes
  - help file adjusted and independent from character set
  - besides of "descript.ion", now "00_index.txt" is used
  - small bugfixes
  - unfortunately, some limitations (keyboard layout hard coded etc.)


New in v1.5:
------------
  - perfect Soundblaster sound support by Ulrich Doewich
  - complete Spanish documentation thanks to Gerardo Briseno
  - updated French documentation thanks to Jean-Pierre Marquet
  - autostart of BASIC programs from disk images
  - 4DOS descriptions in file selection menus
  - online help now allows topics including spaces
  - path names in configurations are saved relative
  - file selection: now up to 1500 directory entries (formerly 500)
  - direct printer port access when using PRINTER=""
  - set data rate with CPCTRANS v2.3g
  - SNA2GIF v1.2: user-configurable colour palette, better auto-scale
  - CPCPARA v1.2: possible to disable fast sending (e.g. for Vortex)
  - extended poke database
  - some minor changes


New in v1.4:
------------
  - GUS sound support by Ulrich Doewich
  - online help system in English, German, French and Spanish
  - complete French documentation
  - support for 2 joysticks
  - VESA videomodes for higher resolutions
  - improved setup menu and configuration file
  - load and save configurations from setup menu
  - improved FDC routines for non-standard formats
  - Extended disk format
  - user-configurable colours and keys
  - improved CPCTRANS (v2.3)
  - new SNA2GIF (v1.1): grab screens from snapshots


New in v1.3b:
------------

  - Since v1.3 there was no Soundblaster sound with some (non Pro)
    cards.


New in v1.3a:
------------

  - With v1.3 of CPCEMU, the interrupt mode 2 of the Z80 did not work
    (try Boulder Dash).


New in v1.3:
------------
  - realtime CPC: In this mode CPCEMU tries to be as fast as a real CPC.
  - the ROMs are (c) by Amstrad and Locomotive Software
  - French documentation
  - menu system with mouse support
  - poke database for easy "poking"
  - re-format disk images with CPCEMU
  - insert disk images with read-only DOS attribute
  - debug menu: 'find' added
  - 'fast Z80': does not crash the computer when using Z80 instructions
    with word access at 0xffff
  - parallele adapter: new PCPARA, CPCPARA with up to 19000 baud
  - CPCTRANS: compiled for 8086 to use it also on an XT
  - ...



  You can find further information in the English, German, French or
  Spanish documentation CPCEMU_E.TXT, CPCEMU_D.TXT, CPCEMU_F.TXT,
  CPCEMU_S.TXT respectively.


Write your comments to:

        Marco Vieth
        Auf dem Uekern 4
        33165 Lichtenau
        Germany

        or by e-mail:
          cpcemu@hotmail.com
          (ali@uni-paderborn.de  only valid until 10/01/98)

        or to:
        Rainer Loritz
        (rainer@loritz.net)

-------------------
