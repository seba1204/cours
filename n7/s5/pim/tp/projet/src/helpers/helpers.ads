with Exceptions;            use Exceptions;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Command_Line;      use Ada.Command_Line;
with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Float_Text_IO;     use Ada.Float_Text_IO;
with Ada.Integer_Text_IO;   use Ada.Integer_Text_IO;
with Ada.Real_Time; use  Ada.Real_Time; -- pour le temps d'exécution

package Helpers is
   Verbeux : Boolean := False;
   Matlab : Boolean := False;
   type Args is record 
      Nom_Fichier    : Unbounded_String;
      A              : Float    := 0.85;
      Max_Iter       : Integer  := 150;
      Est_Naif       : Boolean  := True;
      Aide_Demande   : Boolean  := False;
      Taille_Hachage : Positive := 100;
      Taille_Reseau  : Positive;
   end record;
   function "-" (Item : in String) return Integer;
   function "+" (Item : in String) return Unbounded_String;
   function Lire_Arugments return Args;
   function Est_Nom_Fichier_Net(Argument : in String) return Boolean;
   procedure Log(Message : in String);
   procedure Log_P(Progression : in Integer; Max : in Integer);
   procedure Log_Matlab(Duree : in Integer);

   function Chemin (Nom_Fichier : in String) return String;
   function Nom (Nom_Fichier : in String) return String;
   function Octets (R : in Integer) return Integer;
   function Humaniser (Duree : in Duration) return String;

   private
      procedure Nettoyer_Console;
      procedure Afficher_Aide;

end Helpers;