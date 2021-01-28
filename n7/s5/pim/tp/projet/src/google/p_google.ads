with Exceptions;            use Exceptions;
with Ada.Directories;  use Ada.Directories;
with Ada.Exceptions; use Ada.Exceptions;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Float_Text_IO;     use Ada.Float_Text_IO;
with Ada.Integer_Text_IO;   use Ada.Integer_Text_IO;
with Helpers;               use Helpers;
with Naive;
with Creuse;

generic
   type Reel is digits <>;

package P_Google is

   package G_Creuse is new Creuse(Reel);
   use G_Creuse;

   package G_Naive is new Naive(Reel);
   use G_Naive;


   A : Args;
   
   type Tampon is array(Positive range <>) of Reel;

   type Google is tagged null record;
   function Mode (Self: in out Google) return String;
   procedure Initialiser (Self: in out Google);
   procedure Inserer (Self: in out Google; I : in Integer; J: in Integer;Valeur : in Reel);
   procedure Tamponner (Self: in out Google; I: in Integer);
   procedure Calculer_Coef (Self: in out Google);
   function Multiplicateur_De_Poids (Self: in out Google; I : in Integer; J: in Integer) return Reel;

   -- TODO: mettre tampon dans google

   type Google_Naive(Taille: Positive) is new Google with record
      G : Table_Naive(1..Taille, 1..Taille); -- du package Naive
      T : Tampon(1..Taille);
   end record;
   function Mode (Self: in out Google_Naive) return String;
   procedure Initialiser (Self: in out Google_Naive);
   procedure Inserer (Self: in out Google_Naive; I : in Integer; J: in Integer;Valeur : in Reel);
   procedure Tamponner (Self: in out Google_Naive; I: in Integer);
   procedure Calculer_Coef (Self: in out Google_Naive);
   function Multiplicateur_De_Poids (Self: in out Google_Naive; I : in Integer; J: in Integer) return Reel;
   
   type Google_Creuse(Taille_Reseau: Positive; Taille_Hachage: Positive) is new Google with record
      G : Table_Creuse(Taille_Hachage);
      T : Tampon(1..Taille_Reseau);
   end record;
   function Mode (Self: in out Google_Creuse) return String;
   procedure Initialiser (Self: in out Google_Creuse);
   procedure Inserer (Self: in out Google_Creuse; I : in Integer; J: in Integer;Valeur : in Reel);
   procedure Tamponner (Self: in out Google_Creuse; I: in Integer);
   procedure Calculer_Coef (Self: in out Google_Creuse);
   function Multiplicateur_De_Poids (Self: in out Google_Creuse; I : in Integer; J: in Integer) return Reel;


   function Initialiser (Ar : in Args) return Google'Class;

private
   Un : constant Reel := Reel(1);
   Zero : constant Reel := Reel(0);

end P_Google;
