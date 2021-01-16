with Exceptions;            use Exceptions;
with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Helpers;               use Helpers;

generic
   type T_Float is digits <>;

package Google_Creuse is
   type T_Page is private;
   type T_Poids is private;

   Nom_Fichier_Net : Unbounded_String;
   A               : T_Float;
   Max_Iter        : Integer;
   Taille          : Integer;
   Pi              : T_Poids;
   Pi_Trie         : T_Poids;
   procedure Init
     (N : in Unbounded_String; A : in T_Float; M : in Integer; T : in Ineger);
   procedure Calculer_Coefs;
   procedure Initialiser_Poids;
   procedure Calculer_Poids;
   procedure Trier_Poids;
   procedure Creer_Fichiers;

   private

end Google_Creuse;
