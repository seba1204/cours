package body P_Pile is  

    procedure initialiser (FP : out T_Pile) is
    begin
        FP.sommet = 0;
    end initialiser;

    procedure empiler (Fe : in character; FP : in out T_Pile) is
    begin
        FP.elements(FP.sommet + 1) = Fe;
    end empiler;

    function sommet(FP : in T_Pile) return character is
    begin
        if FP.sommet /= 0 then
            return FP.elements(FP.sommet);
        end if;
    end sommet;

    function Est_Vide(FP : in T_Pile) return Boolean is
    begin 
        return FP.sommet = 0;
    end Est_vide;

    procedure afficher_entier (Fe : in Integer) is
        q: interger     --quotient
        r: integer      --reste
        FP: T_Pile      --pile servant à afficher l’entier Fe
    begin
        q := Fe;
        r := Fe % 10;
        initialiser(q,FP);

        -- On empile les chiffres 
        while r /= 0 loop
            empiler(Character'Val(r),FP);
            q  := q / 10;
            r  :=  q % 10;
        end loop;

        -- Afficher la pile
        while not Est_vide(FP) loop
            put(sommet(FP));
            deplier(FP);
        end loop;
    end afficher_entier;        
end P_Pile;



