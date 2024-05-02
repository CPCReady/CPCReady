100 REM CPCREC.BAS - program to receive a file from the PC
110 REM Marco Vieth, 26.7.1994
120 REM
130 CLEAR:DEFSTR a:DEFINT b-z
140 ladr=&A000:IF PEEK(ladr)=&FE THEN 180
150 PRINT"Please wait...":MEMORY ladr-1
160 sum=0:FOR i=&A000 TO &A0A6:READ t$:POKE i,VAL("&"+t$):sum=UNT(sum+PEEK(i))
170 NEXT:READ t$:IF VAL("&"+t$)<>sum THEN PRINT"Checksum ERROR !":STOP
180 CLOSEIN:CLOSEOUT
190 OUT &EF00,&FF:'inactive
200 MODE 2
210 PRINT"CPCREC v1.0 - program to receive files"
220 PRINT"from a PC using the parallel interface"
230 PRINT
240 a=SPACE$(255)
250 CALL ladr,@a:IF LEN(a)=0 THEN 250
260 IF a="TRM:" THEN PRINT"Terminal not supported.":STOP
270 PRINT"Receiving file ";a
280 OPENOUT "!"+a
290 CALL ladr,@a:IF LEN(a)>0 THEN PRINT#9,a;:GOTO 290
300 CLOSEOUT:PRINT"Ok.":PRINT:GOTO 210
310 DATA FE,01,C0,DD,6E,00,DD,66,01,E5,CD,7E,A0,E1,D0,36
320 DATA 00,C9,C5,D5,E5,11,20,4E,06,F5,ED,78,E6,40,6F,3E
330 DATA BF,06,EF,ED,79,06,F5,ED,78,4F,E6,40,AD,20,06,1B
340 DATA 7A,B3,20,F1,37,F5,3E,FF,06,EF,ED,79,F1,38,3A,1E
350 DATA 00,16,08,F3,21,10,27,06,F5,79,E6,40,4F,ED,78,E6
360 DATA 40,A9,20,08,2B,7C,B5,20,F4,37,18,1D,3E,DF,06,EF
370 DATA ED,79,ED,79,06,F5,ED,78,FB,4F,17,17,CB,1B,06,EF
380 DATA 3E,FF,ED,79,15,20,CC,A7,7B,E1,D1,C1,FB,C9,CD,12
390 DATA A0,38,23,77,B7,37,28,1E,47,23,7E,23,66,6F,04,18
400 DATA 12,11,0A,00,CD,12,A0,30,08,1B,7A,B3,20,F6,37,18
410 DATA 05,77,23,10,EC,A7,C9
420 DATA 4C94
430 END
