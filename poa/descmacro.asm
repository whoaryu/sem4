DATA SEGMENT
    STRING1 DB 99H, 12H, 56H, 45H, 36H
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
    START:MOV AX, DATA
    MOV DS,AX
    
    MOV CH, 04H
    
    CHECK MACRO PTR
    MOV AL, [PTR]
    MOV BL, [PTR+1]
    CMP AL, BL
    JNC DOWN
    MOV DL, [PTR+1]
    XCHG [PTR], DL
    MOV [PTR+1],DL
    
    DOWN:
    
    ENDM 
    
    UP2: MOV CL, 04H
    LEA SI, STRING1
    
    UP1: CHECK SI
    INC SI
    DEC CL
    JNZ UP1
    DEC CH
    JNZ UP2
    
    CODE ENDS
END START
