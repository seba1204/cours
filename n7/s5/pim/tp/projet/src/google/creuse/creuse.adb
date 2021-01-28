package body Creuse is

   procedure Free_Cellule is new Ada.Unchecked_Deallocation (Cellule,Ptr_Cellule);

   procedure Free_Ligne is new Ada.Unchecked_Deallocation (Ligne,Ptr_Ligne);
   -----------------
   -- Initialiser --
   -----------------

   procedure Initialiser (Self : in out Table_Creuse) is
   begin
      Taille := Self.Table'Length;
      for I in 1..Taille loop
         Self.Table(I) := null;
      end loop;
   end Initialiser;

   -------------
   -- Inserer --
   -------------

   procedure Inserer (Self : in out Table_Creuse; Ligne_Index : in Integer; Cellule_Index : in Integer; Valeur : in T_Donnee) is
      I : Integer;

      Ligne_Precedente : Ptr_Ligne := null;
      Ligne_Actuelle : Ptr_Ligne := null;
      Ligne_Suivante : Ptr_Ligne := null;

      Cellule_Precedente : Ptr_Cellule := null;
      Cellule_Actuelle : Ptr_Cellule := null;
      Cellule_Suivante : Ptr_Cellule := null;
   begin
      I := Hachage(Ligne_Index);
      
      Ligne_Actuelle := Self.Table(I);

      while Ligne_Actuelle /= null and then (Ligne_Actuelle.all.Index < Ligne_Index) loop
         Ligne_Precedente := Ligne_Actuelle;
         Ligne_Actuelle := Ligne_Actuelle.all.Suivant;
      end loop;

      if Ligne_Actuelle /= null and then Ligne_Actuelle.all.Index = Ligne_Index then
         Cellule_Actuelle := Ligne_Actuelle.all.Cellule;
      end if;

      while Cellule_Actuelle /= null and then (Cellule_Actuelle.all.Index < Cellule_Index) loop
         Cellule_Precedente := Cellule_Actuelle;
         Cellule_Actuelle := Cellule_Actuelle.all.Suivant;
      end loop;


      -- Si elle existe, on enregistre la cellule suivante
      if Cellule_Actuelle /= null then
         if Cellule_Actuelle.all.Index > Cellule_Index then
            Cellule_Suivante := Cellule_Actuelle;
         -- si la cellule existe déjà, on la remplace
         elsif Cellule_Suivante.all.Suivant /= null then
            Cellule_Suivante := Cellule_Suivante.all.Suivant;
         end if;
      end if;


      Cellule_Actuelle := new Cellule'(Cellule_Index, Valeur, Cellule_Suivante);

      -- Enregistrer la nouvelle cellule

      -- si la ligne était vide
      if Cellule_Precedente = null then

         -- Si elle existe, on enregistre la ligne suivante
         if Ligne_Actuelle /= null then
            Ligne_Suivante := Ligne_Actuelle;
         end if;

         Ligne_Actuelle := new Ligne'(Ligne_Index, Cellule_Actuelle, Ligne_Suivante);

         if Ligne_Precedente /= null then
            Ligne_Precedente.all.Suivant := Ligne_Actuelle;
         else
            Self.Table(I) := Ligne_Actuelle;
         end if;
      else
         Cellule_Precedente.all.Suivant := Cellule_Actuelle;
      end if;

   end Inserer;

   

   --------------------------
   -- Pour_Chaque_Cellule --
   --------------------------

   procedure Pour_Chaque_Cellule (Self : in out Table_Creuse; P : access procedure (C : in out Ptr_Cellule ;I : in Integer; J : in Integer)) is
      Ligne_Actuelle : Ptr_Ligne;
      Cellule_Actuelle : Ptr_Cellule;
   begin
      for I in 1..Taille loop
         Ligne_Actuelle := Self.Table(i);
         while Ligne_Actuelle /= null loop
            Cellule_Actuelle := Ligne_Actuelle.all.Cellule;
            while Cellule_Actuelle /= null loop
               P(Cellule_Actuelle, Ligne_Actuelle.all.Index, Cellule_Actuelle.all.Index);
               Cellule_Actuelle := Cellule_Actuelle.all.Suivant;
            end loop;
            Ligne_Actuelle := Ligne_Actuelle.all.Suivant;
         end loop;
      end loop;
   end Pour_Chaque_Cellule;



   -----------------
   -- Lire_Valeur --
   -----------------

   function Lire_Valeur (Self : in out Table_Creuse; I : in Integer; J: in Integer) return Retour_Lire_Valeur is
      Ligne_Actuelle : Ptr_Ligne := null;
      Cellule_Actuelle : Ptr_Cellule := null;
      Retour : Retour_Lire_Valeur;
      Indice : Integer := Hachage(I);
   begin
      -- On ne boucle pas à chaque fois sur toute la matrice
      -- On enregistre où on s'arrete

      Ligne_Actuelle := Self.Table(Indice);

      while Ligne_Actuelle /= null and then Ligne_Actuelle.all.Index < I loop
         Ligne_Actuelle := Ligne_Actuelle.all.Suivant;
      end loop;

      if Ligne_Actuelle /= null and then Ligne_Actuelle.all.Index = I then
         Cellule_Actuelle := Ligne_Actuelle.all.Cellule;
         while Cellule_Actuelle /= null and then Cellule_Actuelle.all.Index < J loop
            Cellule_Actuelle := Cellule_Actuelle.all.Suivant;
         end loop;
         if Cellule_Actuelle /= null and then Cellule_Actuelle.all.Index = J then
            Retour.Valeur := Cellule_Actuelle.all.Donnee;
         else
            Retour.Cellule_Nulle := True;
         end if;
      else
         Retour.Ligne_Nulle := True;
      end if;
      return Retour;
   end Lire_Valeur;

   -----------
   -- Vider --
   -----------

   procedure Vider (Self : in out Table_Creuse) is
      Ligne_Actuelle : Ptr_Ligne;

      procedure Vider_Cellule (C : in out Ptr_Cellule;I : in Integer; J : in Integer) is 
      begin
         Free_Cellule(C);
      end Vider_Cellule;

   begin
      Pour_Chaque_Cellule(Self, Vider_Cellule'Access);

      for I in 1..Taille loop
         Ligne_Actuelle := Self.Table(i);
         Free_Ligne(Ligne_Actuelle);
      end loop;

   end Vider;

   -------------
   -- Hachage --
   -------------

   function Hachage (Index : in Integer) return Integer is 
   begin
      return Index mod Taille + 1;
   end Hachage;

end Creuse;
