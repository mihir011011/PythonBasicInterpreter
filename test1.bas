10 LET X = 1
20 LET Y = 10
30 LET Z = 0
35 LET Z = Z + 1
40 PRINT Z
50 IF Z < Y GOTO 35
55 LET Y = 0
60 LET Z = Z - 1
70 PRINT Z
80 IF Z > Y GOTO 60
90 GOTO 110
100 PRINT Z
105 PRINT Z
110 LET A = 500
120 LET B = A / 2
125 LET B = B * 3
130 LET C = A - B
140 PRINT A
150 PRINT B
160 PRINT C
170 IF A <> X GOTO 181
180 PRINT X
181 IF A >= 500 GOTO 195
190 STOP
195 PRINT A
200 IF X < 1 GOTO 999
205 PRINT X
210 IF X <= A GOTO 190
599 PRINT X
999 STOP