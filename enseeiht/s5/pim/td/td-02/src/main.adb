with Ada.Text_IO;          use Ada.Text_IO;
with Ada.Integer_Text_IO;  use Ada.Integer_Text_IO;

--R0 Afficher le pgcd de deux entiers strictement positifs
procedure pgcd is
    a : Integer  ; -- Les deux nombres dont
    b : Integer  ; -- on veut calculer le pgcd
    na : Integer ; --Variables auxiliares
    nb : Integer ; --car a et b ne doivent pas etre modifiées
    pgcd : Integer ;--Le pgcd de a et b
    
begin
    --R1 Comment "afficher le pgcd de deux entiers positifs ?"
    --R2 Comment "Demander deux entiers " ?
    loop
        Put("A et B ?");
        Get(a);
        Get(b);
    exit when a>0 and b>0;
    end loop;

   --{ (a > 0) Et (b > 0) }
    
    
        --R2 Comment "Determiner le pgcd de a et b" ?
    na := a;
    nb := b;
            --R3 Comment determiner deux entiers differents?
    while na /= nb loop 
            --R3 Comment soustraire au plus grand le plus petit
        if na >nb then
            na := na - nb;
        else
            nb := nb - na;
        end if;
    end loop;
    pgcd := na;
        
    --R1 Comment afficher le pgcd ?
    Put(" pgcd = ");
    Put(pgcd);
    
end pgcd;
