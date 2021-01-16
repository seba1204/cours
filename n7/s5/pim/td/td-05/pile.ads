package P_Pile is
    Type T_Pile is private

    procedure initialiser (FP : out T_Pile);
        -- R0 : initialiser une pile vide
        -- params :
        --      - FP : T_Pile : Pile à initialiser 
        -- post
        --      - sommet = 0

    procedure empiler (Fe : in character; FP : in out T_Pile);
        -- R0 : Empiler un nouvel élément au sommet de la pile
        -- params
        --      - Fe : Character    : élément à ajouter
        --      - Fp : T_Pile       : Pile recevant l'élément
        -- pre
        --      - sommet'Avant /= 0
        -- post 
        --      - sommet'Avant = sommet - 1

    procedure depiler (FP : in out T_Pile);
        -- R0 Dépiler le sommet de la pile
        -- params
        --      - FP : T_Pile : Pile dont on veut supprimer le sommet
        -- pre 
        --      - sommet /= 0
        -- post
        --      - sommet'Avant = sommet + 1

    function sommet (FP : in T_Pile) return character;
        -- R0 Renvoie le sommet de la pile
        -- params
        --      - FP : T_Pile :  Pile dont on veut accéder au sommet
        -- Type de retour : Character
        --      - sommet /= 0
        -- post : 
        --      - resultat = elements(sommet)


    function est_Vide (FP : in T_Pile) return Boolean;
        -- R0 verifie si la pile est vide
    
        -- params 
        --     - FP : T_pile : pile a tester
        -- Type de retour: Boolean
        -- post
        --      - (sommet=0 and resultat= True) or (sommet/=0 and resultat=False)

    
    procedure afficher_entier (Fe : in Integer);
        -- R0 : Afficher un entier à l'aide de pile
        -- params
        --      - Fe : Integer; Entier à afficher
        -- test
        --      Entree : Fe := 123 Resultat 123

    private
        capacite : constant integer := 20;
        Type T_elements is array (1..capacite) of character
        Type T_pile is record
            elements : T_elements;
            sommet : Integer;   -- {0 <= sommet and sommet <= capacite}
        end record
    
end P_Pile;