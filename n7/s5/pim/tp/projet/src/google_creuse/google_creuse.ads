with Exceptions;            use Exceptions;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

generic 
   -- type reel de precision quelconque
   type T_Element is digits <>;
   
package Google_Creuse is
   type T_Google is limited private;
   type T_Poids is limited private;

   function Nb_Page (Nom_Ficher : in Unbounded_String) return Integer;

   procedure Initialiser_Coefs (G : out T_Google);
   
   procedure Calculer_Coefs (G : in out T_Google ; Nom_Ficher : in Unbounded_String; Taille : in Integer);

   procedure Initialiser_Poids (Pi : out T_Poids ; Taille : in Integer);
   
   procedure Calculer_Poids (Pi : out T_Poids; G : in T_Google ; Taille : in Integer; Max_Iter : in Integer);
   
   function Trier_Poids (Pi : in T_Poids; Taille : in Integer) return T_Poids;

   procedure Creer_Fichiers (Pi : in T_Poids; Copi : in T_Poids; Taille : in Integer; a : in T_Element; Max_Iter : in Integer);

private
   type T_Cellule;
   type T_Google is access T_Cellule;
   type T_Cellule is record
      Cle     : Integer;
      Donnee  : T_Element;
      Suivant : T_Google;
   end record;
   type T_Page is record
      Index : Integer;
      Poids : T_Element;
   end record;
   type T_Poids is array(1..CAPACITE_MAX) of T_Page;
end Google_Creuse;
