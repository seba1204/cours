package P_Liste is
    -- TODO: déclarer exepetion Liste_Vide
    procedure Init(Fl : out T_Liste) with
        Post => Fl = null;

    procedure ajouter (Fl : in out T_Liste; Fe : in Integer) with
        Post => Fe est en tête de Fl TODO:

    function Tete (FL : in T_Liste) return Integer with
        -- Pre => Fl /= null,
        Post => Resultat = entier en tête de Fl;TODO:

    function Taille (Fl : in T_Liste) return Integer with
        Post => Resultat = nb cellules de Fl;TODO:

    function Is_In (Fl : in T_Libre ; Fe : in Integer) return Boolean with
        Post => Resultat = Fe \in Fl;TODO:

    procedure Supprimer (Fl : in out T_Liste ; Fe : in Integer) with 
        Pre => Is_In(Fl, Fe),
        Post => Fl est retirée de FL;TODO:
    
    procedure Inserer (Fl : in T_Liste ; Fe, Ff : in  Integer) with
        Pre => Ff \in Fl,TODO:
        Post => Fe est inséré après Ff dans Fl;TODO:

private 
    type T_Cellule;
    type T_Liste is access T_Cellule;
    type T_Cellule is record
        Element : Integer
        Suivante : T_Liste
    end record
end P_Liste
