with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

with Th;

procedure Th_Sujet is
   Longueur : constant Integer := 11;

   function Hachage (Cle : in Unbounded_String) return Integer is
   begin
      return Length (Cle) mod Longueur + 1;
   end Hachage;

   -- On instancie le module Th
   package Table_Hachage is new Th
     (Unbounded_String, Integer, Longueur, Hachage);
   use Table_Hachage;

   procedure Afficher_Cellule (Cle : in Unbounded_String; Donnee : in Integer)
   is
   begin
      Put ("[");
      Put (To_String (Cle));
      Put (": ");
      Put (Integer'Image (Donnee));
      Put ("] -> ");
   end Afficher_Cellule;

   procedure Afficher_Tableau is new Table_Hachage.Pour_Chaque
     (Afficher_Cellule);

   Tab : Table_Hachage.T_Th;
begin
   Initialiser (Tab);
   Enregistrer (Tab, To_Unbounded_String ("un"), 1);
   Enregistrer (Tab, To_Unbounded_String ("deux"), 2);
   Enregistrer (Tab, To_Unbounded_String ("trois"), 3);
   Enregistrer (Tab, To_Unbounded_String ("quatre"), 4);
   Enregistrer (Tab, To_Unbounded_String ("cinq"), 5);
   Enregistrer (Tab, To_Unbounded_String ("quatre-vingt-dix-neuf"), 99);
   Enregistrer (Tab, To_Unbounded_String ("vingt-et-un"), 21);
   Afficher_Tableau (Tab);
end Th_Sujet;
