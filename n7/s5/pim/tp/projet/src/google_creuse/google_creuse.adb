package body Google_Creuse is

   -------------
   -- Nb_Page --
   -------------

   function Nb_Page (Nom_Ficher : in Unbounded_String) return Integer is
   begin
      pragma Compile_Time_Warning (Standard.True, "Nb_Page unimplemented");
      return raise Program_Error with "Unimplemented function Nb_Page";
   end Nb_Page;

   -----------------------
   -- Initialiser_Coefs --
   -----------------------

   procedure Initialiser_Coefs (G : out T_Google) is
   begin
      pragma Compile_Time_Warning
        (Standard.True, "Initialiser_Coefs unimplemented");
      raise Program_Error with "Unimplemented procedure Initialiser_Coefs";
   end Initialiser_Coefs;

   --------------------
   -- Calculer_Coefs --
   --------------------

   procedure Calculer_Coefs
     (G      : in out T_Google; Nom_Ficher : in Unbounded_String;
      Taille : in     Integer)
   is
   begin
      pragma Compile_Time_Warning
        (Standard.True, "Calculer_Coefs unimplemented");
      raise Program_Error with "Unimplemented procedure Calculer_Coefs";
   end Calculer_Coefs;

   -----------------------
   -- Initialiser_Poids --
   -----------------------

   procedure Initialiser_Poids (Pi : out T_Poids; Taille : in Integer) is
   begin
      pragma Compile_Time_Warning
        (Standard.True, "Initialiser_Poids unimplemented");
      raise Program_Error with "Unimplemented procedure Initialiser_Poids";
   end Initialiser_Poids;

   --------------------
   -- Calculer_Poids --
   --------------------

   procedure Calculer_Poids
     (Pi       :    out T_Poids; G : in T_Google; Taille : in Integer;
      Max_Iter : in     Integer)
   is
   begin
      pragma Compile_Time_Warning
        (Standard.True, "Calculer_Poids unimplemented");
      raise Program_Error with "Unimplemented procedure Calculer_Poids";
   end Calculer_Poids;

   -----------------
   -- Trier_Poids --
   -----------------

   function Trier_Poids (Pi : in T_Poids; Taille : in Integer) return T_Poids
   is
   begin
      pragma Compile_Time_Warning (Standard.True, "Trier_Poids unimplemented");
      return raise Program_Error with "Unimplemented function Trier_Poids";
   end Trier_Poids;

   --------------------
   -- Creer_Fichiers --
   --------------------

   procedure Creer_Fichiers
     (Pi : in T_Poids; Copi : in T_Poids; Taille : in Integer;
      a  : in T_Element; Max_Iter : in Integer)
   is
   begin
      pragma Compile_Time_Warning
        (Standard.True, "Creer_Fichiers unimplemented");
      raise Program_Error with "Unimplemented procedure Creer_Fichiers";
   end Creer_Fichiers;

end Google_Creuse;
