CPCEMU v2.5, Emulateur de CPC pour des calculateurs moderns
-----------------------------------------------------------

Qu'est-ce que CPCEMU ?
  CPCEMU émule un Amstrad CPC sur votre calculateur. Il vous faut au moins
  un AT 386 avec carte graphique VGA.  Les ROMs des CPCs comme distribué
  dans le Royaume-Uni sont incluses. Va vous chercher les ROMs françaises
  dans l'Internet, s'il vous plait.


Démarrage rapide :
DOS:
  Copiez l'archive CPCEMU15.ZIP vers un sous-répertoire de votre disque dur,
  et décompressez-la avec "PKUNZIP CPCEMU15.ZIP".
  Ensuite, utilisez INSTALL.BAT.
  Après cela, lancez CPC6128.BAT pour avoir une première idée.
Linux:
  Copiez l'archive cpcemu-linux-*-2.x.tar.gz vers un sous-répertoire de
  votre disque dur, et décompressez-la avec
  'tar xvzf cpcemu-linux-*-2.x.tar.gz'. Ensuite, changez le répertoire
  avec 'cd cpcemu-2.x'. Lancez './cpc6128' pour avoir une première idée.
  (remplacent * par arm, arm64, x86 ou x86_64)
Windows:
  Copiez le programme d'installation cpcemu-win32-x86-2.x.exe vers un sous-
  répertoire de votre disque dur et lancez le programme. Choisissez un
  répertoire pour l'installation. Lancez 'CPCemu/CPC6128' dans le menu de
  démarrage pour avoir une première idée.
MacOS, Android, iOS:
  Copiez le programme vers votre appareil et lancez-le.
  

  Vous pouvez essayer la nouvelle aide en ligne en appuyant sur 'F1'. Avec
  'F7', 'T', '2' vous pouvez choisir le clavier française si vous avez
  installé les ROMs françaises dans le sous-répertoire 'ROM'.
  Lorsque vous vous posez des questions, lisez simplement la documentation
  (complètement nouvelle et en français) CPCEMU_F.TXT. 
  Pas de panique, elle est plus courte qu'elle le semble au premier abord :
  la partie concernant l'utilisateur "normal" prend fin au chapitre 6.


Quoi de neuf dans les versions 2.0-2.5?
----------------------------------------
  - Complète émulation d'un M4 Board (http://www.spinpoint.org)
  - Clavier original mais virtuel en 4 langues différentes
  - Emulation exceptionelle du CRTC
  - Extension de la RAM (type Vortex 512 Ko ou type Jarek 4 Mo)
  - Souris
  - Mise à niveau de la version la plus récente de SDL (2.0.22)
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
  - auto-démarrage des programmes Basic à partir des images de disquettes
  - descriptions 4DOS dans les menus de sélection de fichiers
  - l'aide en ligne comprend à présent les rubriques contenant des espaces
  - les noms de chemin dans les configurations sont sauvegardés relativement
  - taux de données fixé avec CPCTRANS v2.3g
  - palette de couleurs définie par l'utilisateur pour SNA2GIF v1.2
  - CPCPARA v1.2 : on peut désactiver l'envoi rapide (par exemple pour Vortex)
  - base de données de POKEs étendue
  - quelques modifications mineures

Quoi de neuf dans la version 1.4 ?
----------------------------------

  - soutien de la carte sonore GUS, par Ulrich Doewich
  - système d'aide en ligne, en anglais, allemand, français et espagnol
  - documentation complète en français
  - deux joysticks acceptés
  - modes graphiques VESA pour des résolutions supérieures
  - amélioré le menu des réglages et le fichier de configuration
  - chargement et sauvegarde des configurations depuis le menu des réglages
  - amélioré les routines FDC pour les formats non standard
  - format de disquettes "Extended"
  - couleurs et touches configurables par l'utilisateur
  - amélioré CPCTRANS (v2.3)
  - nouveau SNA2GIF (v1.1) : extrait les écrans depuis les snapshots
  
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

  - temps réel, équivalent à celui du CPC : dans ce mode, CPCEMU essaie
    d'être aussi rapide qu'un vrai CPC.
  - les ROMs sont "(c) by Amstrad and Locomotive Software"
  - documentation française
  - susyème de menu admettant la souris
  - base de données de POKEs pour tricher facilement aux jeux
  - reformater les images de disquettes avec CPCEMU
  - insertion d'images de disquettes avec l'attribut "lecture seule"
  - meny Debug : ajouté l'option "find" (recherche)
  - "fast Z80" : ne plante pas l'ordinateur lorsqu'on utilise les
    instructions du Z80 avec un accès "mot" à l'adresse 0xFFFF
  - adaptateur parallèle : nouveaux PCPARA, et CPCPARA jusqu'à 19 000 bauds
  - CPCTRANS : compilé pour un 8086, afin d'être utilisable sur un XT
  - ...
  
  Vous trouverez davantage d'information dans les fichiers de documentation
  en anglais, allemand, français et espagnol, respectivement :
                CPCEMU_E.TXT
                CPCEMU_D.TXT
                CPCEMU_F.TXT
                CPCEMU_S.TXT.


Ecrivez vos commentaires à :

        Marco Vieth
        Auf dem Uekern 4
        33165 Lichtenau
        Germany

        ou par e-mail:
          cpcemu@hotmail.com
          (ali@uni-paderborn.de)

        ou à:
        Rainer Loritz
        (rainer@loritz.net)

-------------------
