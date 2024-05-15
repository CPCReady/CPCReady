100 REM ROMGET (v2.0)
110 REM 3.9.1994
120 REM
130 MODE 1: CLEAR: DEFINT a-z
140 PRINT"ROMGET v2.0":PRINT"Run on a CPC to save the ROMs as files.": PRINT
150 PRINT"Insert disk with >= 50K free space": PRINT"and press a key ..."
160 CALL &BB18
170 adr=&A000: sh=adr+2: dh=adr+5: k=adr+15
180 h!=HIMEM: MEMORY &1FFF
190 FOR i=adr TO adr+&12: READ a$: POKE i,VAL("&"+a$): NEXT
200 POKE sh,0: POKE dh,&20: POKE k,&FC: CALL adr
210 POKE sh,&C0: POKE dh,&60: CALL adr
220 PRINT"Saving lower&upper-ROM (CPCXXXX.ROM) ..."
230 SAVE"!CPCXXXX.ROM",b,&2000,&8000
240 POKE k,7: CALL adr
250 IF PEEK(&6000)<>1 THEN PRINT"No AMSDOS-ROM found.": GOTO 280
260 PRINT"Saving AMSDOS-ROM (CPCADOS.ROM) ..."
270 SAVE"!CPCADOS.ROM",b,&6000,&4000
280 PRINT"Trying to find some other ROMs ..."
290 FOR i=1 TO 251:PRINT HEX$(i);
300 IF i=7 THEN 360
310 POKE k,i:CALL adr
320 IF PEEK(&6000)=&80 THEN 360
330 PRINT" ROM found -- ";
340 PRINT"Saving MYROM";HEX$(i,2);".ROM ..."
350 SAVE"!MYROM"+HEX$(i,2)+".ROM",b,&6000,&4000:PRINT
360 PRINT CHR$(13);:NEXT
370 PRINT:PRINT"bye."
380 MEMORY h!: END
390 DATA 21,00,C0,11,00,20,01,00,40,DF,0D,A0,C9,10,A0,00,ED,B0,C9
400 '
410 '****  end of program  ***
420 '
430 'ROMGET - written to save the CPC-ROM in a file, which can be used
440 'by CPCEMU (transfer Z80CPC.ROM, Z80DISK.ROM to a PC).
450 '
460 'If you input this program, you can leave all REM- and PRINT - lines.
470 'Some annotations:
480 ' line 200 : copy low-rom &0000-&3fff to ram &2000-&5fff
490 ' line 210 : copy high-rom &c000-&ffff to ram &6000-&9fff
500 ' line 240 : copy amsdos-rom &c000-&ffff to ram &6000-&9fff
510 '
520 'The assembler-module in data-line 300 :
530 '
540 ';ROMGET2 (v1.2)
550 ';17.1.1993 (26.,27.6.1989)
560 ';
570 ';Program to copy the CPC-ROMs to RAM, so you can save them in a file.
580 ';Run this on a CPC
590 ';
600 ';usage:
610 '; adr = &a000
620 '; poke adr+&02 , source-address (hi-byte)
630 '; poke adr+&05 , destionation-address (hi-byte)
640 '; poke adr+&0F , rom/ram-configuration
650 '; call adr       'to copy &4000-byte-bank
660 ';
670 '; (rom/ram-config -  0..251 = ROM-number, 252=lower,upper rom enabled, ...)
680 'ORG #A000
690 'LD HL,#C000               ;source-address (ROM or RAM)
700 'LD DE,#2000               ;destination-address (RAM)
710 'LD BC,#4000               ;length of bank
720 'RST #18
730 'DEFW RSTTAB
740 'RET
750 '
760 'RSTTAB DEFW BLOCK         ;jump to prg
770 'DEFB 0                    ;rom/ram-configuration
780 '
790 'BLOCK LDIR                ;copy the bank
800 'RET
810 '
820 'END
830 ';
