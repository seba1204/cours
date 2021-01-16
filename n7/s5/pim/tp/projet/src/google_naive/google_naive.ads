with Exceptions;            use Exceptions;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Float_Text_IO;     use Ada.Float_Text_IO;
with Ada.Integer_Text_IO;   use Ada.Integer_Text_IO;
with Helpers;               use Helpers;

generic
   type T_Float is digits <>;
   CAPACITE_MAX : Integer;
package Google_Naive is
   type T_Poids is limited private;


   procedure Calculer_Coefs
     (Nom_Fichier : in Unbounded_String; Taille : in Integer; A : in T_Float);

   procedure Initialiser_Poids (Pi : out T_Poids; Taille : in Integer);

   procedure Calculer_Poids
     (Pi          : in out T_Poids; Taille : in Integer; Max_Iter : in Integer;
      Nom_Fichier : in     Unbounded_String);

   procedure Trier_Poids
     (Pi_Trie : out T_Poids; Pi : in T_Poids; Taille : in Integer);

   procedure Creer_Fichiers
     (Pi          : in T_Poids; Pi_Trie : in T_Poids; Taille : in Integer;
      a           : in T_Float; Max_Iter : in Integer;
      Nom_Fichier : in Unbounded_String);

private
   type T_Page is record
      Index : Integer;
      Poids : T_Float;
   end record;
   type T_Poids is array (1 .. CAPACITE_MAX) of T_Page;
end Google_Naive;
