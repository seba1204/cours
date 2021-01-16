#!/bin/bash
for borne in `seq 1 5`;
do
  for taille in `seq $borne 7` ;
  do
    ( time ./obj/evaluer_alea_lca $((10**$borne)) $((10**$taille)) ) >> bornes_lca.txt 2>> time_lca.txt    
    ( time ../obj/evaluer_alea_th $((10**$borne)) $((10**$taille)) ) >> bornes_th.txt 2>> time_th.txt
  done
done