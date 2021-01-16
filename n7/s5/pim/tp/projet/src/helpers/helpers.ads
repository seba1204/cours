with Exceptions;            use Exceptions;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Command_Line;      use Ada.Command_Line;
with Ada.Text_IO;           use Ada.Text_IO;

package Helpers is

   type T_Double is digits 3;

   function "+" (Item : in String) return Unbounded_String;
   function "-" (Item : in String) return Integer;
   function "&" (Left, Right : in Unbounded_String) return Unbounded_String;
   -- function "&" (Left: in Unbounded_String; Right: in String) return
   -- Unbounded_String; function "&" (Left: in Unbounded_String; Right:
   -- in Integer) return Unbounded_String; function "&" (Left: in
   -- Unbounded_String; Right: in Float) return Unbounded_String; function "&"
   -- (Left: in String; Right: in Unbounded_String ) return Unbounded_String;
   -- function "&" (Left: in Integer; Right: in Unbounded_String )
   -- return Unbounded_String; function "&" (Left: in Float; Right:
   -- in Unbounded_String ) return Unbounded_String;
   function Compter
     (Chaine : in Unbounded_String; Schema : in Character) return Integer;
   function Chemin (Nom_Fichier : in Unbounded_String) return String;
   function Nom (Nom_Fichier : in Unbounded_String) return String;
   procedure Afficher_Aide;
   procedure Nettoyer_Console;
   procedure Lire_Args
     (Nom_Fichier : out Unbounded_String; A : out T_Double;
      Max_Iter    : out Integer; P : out Boolean; Aide : out Boolean);
   procedure Estimer_Donnees (Taille : in Integer; Max_Iter : in Integer);

private

end Helpers;
