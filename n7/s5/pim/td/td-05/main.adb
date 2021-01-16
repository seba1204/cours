with P_Pile; 
use P_Pile;

procedure Test_Pile is 
    P: T_Pile;
begin

    -- initialise une pile
    Initialiser(P);

    -- empile successivement les caractères ’o’, ’k’, puis ’ ?’,
    empiler(P,‘o’);
    empiler(‘k’);
    empiler(‘?’);

    -- vérifie que le sommet est ’ ?’
    pragma assert { sommet(FP)=’?’};

    -- dépile 3 fois
    for i in range 1  .. 3 loop
        depiler(P);
    end loop;

    -- vérifie que la pile est vide
    pragma assert { Est_Vide(P) };
end Test_Pile;
