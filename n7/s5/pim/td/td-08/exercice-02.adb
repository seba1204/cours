package body P_Liste is

    procedure Init(Fl : out T_Liste) is
    begin 
        Fl := null;
    end Init;

    procedure Ajouter_Debut (Fl : in out T_Liste; Fe : in Integer) is
        l : T_Liste;
    begin
        l := New T_Cellule
        l.all.Element := Fe;
        l.all.Suivante := Fl;
        Fl := l;
        -- FL := New T_Cellule(Fe, Fl); --> combine tout en même temps
    end Ajouter_Debut;


    function Tete (FL : in T_Liste) return Integer is
        Exception : Liste_Vide -- est levée si Fl est vide
    begin
        if Fl /= null then
            return (Fl.ll.element);
        else 
            raise Liste_Vide;
        end if;
    end Tete;

    
    function Taille (Fl : in T_Liste) return Integer is
        nb : Integer;
        l : T_Liste;
    begin
        nb := 0;
        l := Fl;
        while l /= null loop
            nb := nb + 1;
            l := l.all.Suivante;
        end loop;
        if F = null then
            return 0;
        else 
            return (nb);
        end if;

    end Tete;

    function Is_In (Fl : in T_Libre ; Fe : in Integer) return Boolean is
        l : T_Liste;
        b : Boolean;
    begin 
        l := Fl;
        Bool := False;
        while l /= null and then l.all.element /= Fe loop
            l := l.all.Suivante;
        end loop;

        return (not (l = null))
        
        -- if Fl = null then return (False)
        -- else
        --   return (Fl.all.element = Fe or Is_In(Fl.all.Suivante, Fe));
        -- end if;
    end Is_In;

    
    procedure Supprimer (Fl : in out T_Liste ; Fe : in Integer) is
        l : T_Liste;
        Old_Pointer : T_Liste;
    begin 
        if Fl.all.element = Fe then
            Fl := Fl.all.Suivante;
        else
            l:= Fl;
            while l.all.Suivante.all.Element /= Fe loop
                l := l.all.Suivante;
            end loop;
            l.all.Suivante := l.all.Suivante.all.Suivante;
        end if;


        -- if not Fl = null then
        --    if Fl.all.Element /= Fe then
        --        Ajouter_Debut(Fl.all.element, Supprimer(l.all.Suivante, Fe))
        --    end if;
        -- end if;

    end Supprimer;

    procedure Inserer (Fl : in T_Liste ; Fe, Ff : in  Integer) is
        l : T_Liste;
    begin
        l := Fl;
        while l.all element /= Ff loop
            l := l.all.Suivante;
        end loop;
        l.all.Suivante := New T_Cellule(Fe, l.all.Suivante);
    end Inserer;

end P_Liste
