with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Text_IO;           use Ada.Text_IO;
with Exceptions;            use Exceptions;
with Helpers;               use Helpers;

generic
   type T_Float is digits <>;
   Capacite_Max : Integer;

package Google_Naive is

   type T_Page is record
      Poids : T_Float;
      Index : Integer;
   end record;
   type T_Poids is array (1..Capacite_Max) of T_Page;
   type T_Google is array (1..Capacite_Max, 1..Capacite_Max) of T_Float;

   Nom_Fichier_Net : Unbounded_String;
   A               : T_Float;
   Max_Iter        : Integer;
   Taille          : Integer;
   G               : T_Google;
   Pi              : T_Poids;
   Pi_Trie         : T_Poids;

   procedure Init
     (N : in Unbounded_String; A : in T_Float; M : in Integer; T : in Ineger);
   procedure Calculer_Coefs;
   procedure Initialiser_Poids;
   procedure Calculer_Poids;
   procedure Trier_Poids;
   procedure Creer_Fichiers;


end Google_Naive;
