package body P_Google is

   function Initialiser (Ar : in Args) return Google'Class is
   begin
      A := Ar;
      if A.Est_Naif then
         declare
            G : Google_Naive (A.Taille_Reseau);
         begin
            return G;
         end;
      else
         declare
            G : Google_Creuse (A.Taille_Reseau, A.Taille_Hachage);
         begin
            return G;
         end;
      end if;
   end Initialiser;

   
   function Mode (Self : in out Google) return String is
   begin
      -- return Google'External_Tag;
      return "Google";
   end Mode;
   procedure Initialiser (Self: in out Google) is 
   begin
      null;
   end Initialiser;
   procedure Inserer (Self: in out Google; I : in Integer; J: in Integer;Valeur : in Reel) is 
   begin
      null;
   end Inserer;
   procedure Tamponner (Self: in out Google; I: in Integer) is 
   begin
      null;
   end Tamponner;
   procedure Calculer_Coef (Self: in out Google) is 
   begin
      null;
   end Calculer_Coef;
   function Multiplicateur_De_Poids (Self: in out Google; I : in Integer; J: in Integer) return Reel is 
   begin
      return 0.0;
   end Multiplicateur_De_Poids;

 
   -- =========================================================================
   -- =                         GOOGLE NAIVE                                  =
   -- =========================================================================

   -- =========================================================================
   function Mode (Self : in out Google_Naive) return String is
   begin
      -- return Google_Naive'External_Tag;
      return "Google Naive";
   end Mode;

   procedure Initialiser (Self : in out Google_Naive) is
      Taille: constant Integer := A.Taille_Reseau;
   begin
      for I in 1..Taille loop
         Self.T(I) := Zero;
         for J in 1..Taille loop
            Self.G(I,J) := Zero;
         end loop; 
      end loop;
   end Initialiser;

   -- =========================================================================
   procedure Inserer (Self : in out Google_Naive; I : in Integer; J: in Integer; Valeur : in Reel) is      
   begin
      Self.G(I+1,J+1) := Valeur;
   end Inserer;

   -- =========================================================================
   procedure Tamponner (Self : in out Google_Naive; I : in Integer) is      
   begin
      Self.T(I) := Self.T(I) + Un;
   end Tamponner;

   -- =========================================================================
   procedure Calculer_Coef (Self : in out Google_Naive) is
      Taille: constant Integer := A.Taille_Reseau;
      AC : constant Reel := Reel(A.A);
      BC : constant Reel := Un / Reel(Taille);
   begin
     for I in 1..Taille loop
         Log_P(I, Taille);
         for J in 1..Taille loop
            if Self.T(I) = Zero then
               Self.G(I,J) := BC;
            else
               if Self.G(I,J) = Zero then
                  Self.G(I,J) := (Un - AC) * BC;
               else
                  Self.G(I,J) := AC * Un / Reel(Self.T(I)) + (Un - AC) * BC;
               end if;
            end if;
         end loop; 
      end loop;
   end Calculer_Coef;


   -- =========================================================================
   function Multiplicateur_De_Poids (Self: in out Google_Naive; I : in Integer; J: in Integer) return Reel is
   begin
      return Self.G(I, J);
   end Multiplicateur_De_Poids;



   -- =========================================================================
   -- =                         GOOGLE CREUSE                                 =
   -- =========================================================================
   function Mode (Self : in out Google_Creuse) return String is
   begin
      -- return Google_Creuse'External_Tag;
      return "Google Creuse";
   end Mode;

   -- =========================================================================
   procedure Initialiser (Self : in out Google_Creuse) is
      Taille: constant Integer := A.Taille_Reseau;
   begin
      -- G
      Self.G.Initialiser;

      -- Tampon
      for I in 1..Taille loop
         Self.T(I) := Zero;
      end loop;
   end Initialiser;

   -- =========================================================================
   procedure Inserer (Self : in out Google_Creuse; I : in Integer; J: in Integer; Valeur : in Reel) is      
   begin
      Self.G.Inserer(I,J, Valeur);
   end Inserer;

   -- =========================================================================
   procedure Tamponner (Self : in out Google_Creuse; I : in Integer) is      
   begin
      Self.T(I) := Self.T(I) + Un;
   end Tamponner;

   -- =========================================================================
   procedure Calculer_Coef (Self : in out Google_Creuse) is
      procedure AF(C : in out Ptr_Cellule ;I : in Integer; J : in Integer) is
      begin
         C.all.Donnee := Reel(A.A) / Self.T(I+1) + (Un - Reel(A.A)) / Reel(A.Taille_Reseau);
      end AF;
   begin
      Self.G.Pour_Chaque_Cellule(AF'Access);
   end Calculer_Coef;

   Derniere_Ligne : Ptr_Ligne := null;
   Derniere_Cellule : Ptr_Ligne := null;

   -- =========================================================================
   function Multiplicateur_De_Poids (Self : in out Google_Creuse; I : in Integer; J: in Integer) return Reel is
      Zero_Cellule, Zero_Ligne : Reel;
      Ligne_Actuelle : Ptr_Ligne := null;
      Cellule_Actuelle : Ptr_Cellule := null;
      Retour : Retour_Lire_Valeur;
   begin
      Zero_Cellule := (Un-Reel(A.A)) / Reel(A.Taille_Reseau);
      Zero_Ligne := Un / Reel(A.Taille_Reseau);

      Retour := Self.G.Lire_Valeur(I-1,J-1);

      if Retour.Ligne_Nulle then
         return Zero_Ligne;
      else
         if Retour.Cellule_Nulle then
            return Zero_Cellule;
         else
            return Retour.Valeur;
         end if;
      end if;
   end Multiplicateur_De_Poids;



end P_Google;
