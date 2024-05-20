CPCEMU v2.5, Emulateur de CPC pour des calculateurs moderns
-----------------------------------------------------------

Qu'est-ce que CPCEMU ?
  CPCEMU �mule un Amstrad CPC sur votre calculateur. Il vous faut au moins
  un AT 386 avec carte graphique VGA.  Les ROMs des CPCs comme distribu�
  dans le Royaume-Uni sont incluses. Va vous chercher les ROMs fran�aises
  dans l'Internet, s'il vous plait.


D�marrage rapide :
DOS:
  Copiez l'archive CPCEMU15.ZIP vers un sous-r�pertoire de votre disque dur,
  et d�compressez-la avec "PKUNZIP CPCEMU15.ZIP".
  Ensuite, utilisez INSTALL.BAT.
  Apr�s cela, lancez CPC6128.BAT pour avoir une premi�re id�e.
Linux:
  Copiez l'archive cpcemu-linux-*-2.x.tar.gz vers un sous-r�pertoire de
  votre disque dur, et d�compressez-la avec
  'tar xvzf cpcemu-linux-*-2.x.tar.gz'. Ensuite, changez le r�pertoire
  avec 'cd cpcemu-2.x'. Lancez './cpc6128' pour avoir une premi�re id�e.
  (remplacent * par arm, arm64, x86 ou x86_64)
Windows:
  Copiez le programme d'installation cpcemu-win32-x86-2.x.exe vers un sous-
  r�pertoire de votre disque dur et lancez le programme. Choisissez un
  r�pertoire pour l'installation. Lancez 'CPCemu/CPC6128' dans le menu de
  d�marrage pour avoir une premi�re id�e.
MacOS, Android, iOS:
  Copiez le programme vers votre appareil et lancez-le.
  

  Vous pouvez essayer la nouvelle aide en ligne en appuyant sur 'F1'. Avec
  'F7', 'T', '2' vous pouvez choisir le clavier fran�aise si vous avez
  install� les ROMs fran�aises dans le sous-r�pertoire 'ROM'.
  Lorsque vous vous posez des questions, lisez simplement la documentation
  (compl�tement nouvelle et en fran�ais) CPCEMU_F.TXT. 
  Pas de panique, elle est plus courte qu'elle le semble au premier abord :
  la partie concernant l'utilisateur "normal" prend fin au chapitre 6.


Quoi de neuf dans les versions 2.0-2.5?
----------------------------------------
  - Compl�te �mulation d'un M4 Board (http://www.spinpoint.org)
  - Clavier original mais virtuel en 4 langues diff�rentes
  - Emulation exceptionelle du CRTC
  - Extension de la RAM (type Vortex 512 Ko ou type Jarek 4 Mo)
  - Souris
  - Mise � niveau de la version la plus r�cente de SDL (2.0.22)
  - Lisez "readme_e.txt", s.v.p.

Quoi de neuf dans les versions 1.7?
------------------------------------
  - le clavier du CPC est ajustable et, dans cpcemu.dat, configurable,
    mais pas encore parfait

Quoi de neuf dans les versions 1.6?
------------------------------------
  - Lisez "readme_e.txt", s.v.p.

Quoi de neuf dans la version 1.5 ?
-----------------------------------

  - un parfait soutien du son SoundBlaster, par Ulrich Doewich
  - documentation en espagnol
  - auto-d�marrage des programmes Basic � partir des images de disquettes
  - descriptions 4DOS dans les menus de s�lection de fichiers
  - l'aide en ligne comprend � pr�sent les rubriques contenant des espaces
  - les noms de chemin dans les configurations sont sauvegard�s relativement
  - taux de donn�es fix� avec CPCTRANS v2.3g
  - palette de couleurs d�finie par l'utilisateur pour SNA2GIF v1.2
  - CPCPARA v1.2 : on peut d�sactiver l'envoi rapide (par exemple pour Vortex)
  - base de donn�es de POKEs �tendue
  - quelques modifications mineures

Quoi de neuf dans la version 1.4 ?
----------------------------------

  - soutien de la carte sonore GUS, par Ulrich Doewich
  - syst�me d'aide en ligne, en anglais, allemand, fran�ais et espagnol
  - documentation compl�te en fran�ais
  - deux joysticks accept�s
  - modes graphiques VESA pour des r�solutions sup�rieures
  - am�lior� le menu des r�glages et le fichier de configuration
  - chargement et sauvegarde des configurations depuis le menu des r�glages
  - am�lior� les routines FDC pour les formats non standard
  - format de disquettes "Extended"
  - couleurs et touches configurables par l'utilisateur
  - am�lior� CPCTRANS (v2.3)
  - nouveau SNA2GIF (v1.1) : extrait les �crans depuis les snapshots
  
Quoi de neuf dans la version 1.3b ?
-----------------------------------

  - Depuis la version 1.3, il n'y avait plus de son SoundBlaster avec
    certaines cartes non Pro
  

Quoi de neuf dans la version 1.3a ?
-----------------------------------

  - Avec la version 1.3, le mode d'interruption 2 du Z80 ne fonctionnait
    pas (essayez Boulder Dash).

 Quoi de neuf dans la version 1.3 ?
 ----------------------------------

  - temps r�el, �quivalent � celui du CPC : dans ce mode, CPCEMU essaie
    d'�tre aussi rapide qu'un vrai CPC.
  - les ROMs sont "(c) by Amstrad and Locomotive Software"
  - documentation fran�aise
  - susy�me de menu admettant la souris
  - base de donn�es de POKEs pour tricher facilement aux jeux
  - reformater les images de disquettes avec CPCEMU
  - insertion d'images de disquettes avec l'attribut "lecture seule"
  - meny Debug : ajout� l'option "find" (recherche)
  - "fast Z80" : ne plante pas l'ordinateur lorsqu'on utilise les
    instructions du Z80 avec un acc�s "mot" � l'adresse 0xFFFF
  - adaptateur parall�le : nouveaux PCPARA, et CPCPARA jusqu'� 19 000 bauds
  - CPCTRANS : compil� pour un 8086, afin d'�tre utilisable sur un XT
  - ...
  
  Vous trouverez davantage d'information dans les fichiers de documentation
  en anglais, allemand, fran�ais et espagnol, respectivement :
                CPCEMU_E.TXT
                CPCEMU_D.TXT
                CPCEMU_F.TXT
                CPCEMU_S.TXT.


Ecrivez vos commentaires � :

        Marco Vieth
        Auf dem Uekern 4
        33165 Lichtenau
        Germany

        ou par e-mail:
          cpcemu@hotmail.com
          (ali@uni-paderborn.de)

        ou �:
        Rainer Loritz
        (rainer@loritz.net)

-------------------
