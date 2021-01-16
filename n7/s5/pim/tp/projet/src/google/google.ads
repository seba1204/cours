with Exceptions;            use Exceptions;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Float_Text_IO;     use Ada.Float_Text_IO;
with Ada.Integer_Text_IO;   use Ada.Integer_Text_IO;
with Helpers;               use Helpers;
with Google_Naive;          
with Google_Creuse;          

generic
   type T_Float is digits <>;
   CAPACITE_MAX : Integer;
package Google is
   package Google_Naive_Table is new Google_Naive
      (T_Float => T_Double, Capacite_Max => 10_000);
   use Google_Naive_Table;
   
   package Google_Creuse_Table is new Google_Creuse
      (T_Float => T_Double);
   use Google_Creuse_Table;


   Type_Id : Boolean;

   procedure Definir_Type (Id : in Boolean);

   function Nb_Page (Nom_Fichier : in Unbounded_String) return Integer;

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
      

end Google;
