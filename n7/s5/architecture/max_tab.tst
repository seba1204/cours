// Test du module max_tab(rst, clk, cal, ad_1[7..0], ad_2[7..0] : 
// max[31..0], ad_max[7..0], INITAD, INITMAX, MAJMAX, FINI)
// Attention : il faut que le module testé ait exactement les mêmes signaux
// d'entrée et de sortie, en respectant la casse.

// Quel est le nombre de cycles d’horloge nécessaire pour
// calculer le max d’un tableau de N éléments ?
// il faut N+2 cycles : initialisation + boucle de 1 à N + désactivation 
// de cal


set rst 1
set rst 0
set cal 0
set clk 0

// Initialisation
check INITAD 1
check INITMAX 0
check MAJMAX 0
check FINI 0
check ad_max[7..0] 00000000
check max[31..0] 00000000000000000000000000000000

// cal=0 : rien ne doit evoluer
set ad_1[7..0] 00000000
set ad_2[7..0] 00000101

set clk 1

check INITAD 1
check INITMAX 0
check MAJMAX 0
check FINI 0
check ad_max[7..0] 00000000
check max[31..0] 00000000000000000000000000000000

// cal=1 : Verif INITAD -> INITMAX
// ad_1 modifié pour bien tester l'initialisation
set ad_1[7..0] 00000001
set clk 0
set cal 1
set clk 1

check INITAD 0
check INITMAX 1
check MAJMAX 0
check FINI 0
check ad_max[7..0] 00000000
check max[31..0] 00000000000000000000000000000000

// Verif INITMAX -> MAJMAX
set clk 0
set clk 1

check INITAD 0
check INITMAX 0
check MAJMAX 1
check FINI 0
check ad_max[7..0] 00000001
check max[31..0] 00000000000000000000000001110011

// On boucle sur le tableau
set clk 0
set clk 1

check INITAD 0
check INITMAX 0
check MAJMAX 1
check FINI 0
check ad_max[7..0] 00000001
check max[31..0] 00000000000000000000000001110011

// On boucle sur le tableau
set clk 0
set clk 1

check INITAD 0
check INITMAX 0
check MAJMAX 1
check FINI 0
check ad_max[7..0] 00000001
check max[31..0] 00000000000000000000000001110011

// On boucle sur le tableau
set clk 0
set clk 1

check INITAD 0
check INITMAX 0
check MAJMAX 1
check FINI 0
check ad_max[7..0] 00000001
check max[31..0] 00000000000000000000000001110011

// Dernier tour
set clk 0
set clk 1

check INITAD 0
check INITMAX 0
check MAJMAX 0
check FINI 1
check ad_max[7..0] 00000101
check max[31..0] 00000000000000000000000001110100

// Verif FINI -> INITAD si cal=0
set cal 0
set clk 0
set clk 1

check INITAD 1
check INITMAX 0
check MAJMAX 0
check FINI 0