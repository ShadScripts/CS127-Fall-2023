#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#This program prints in simplified machine language!

loop:
    bgt $s0,50,exit
    addi $t0,$t0,5
    j loop

exit: