
with Ada.Unchecked_Deallocation;

generic
   type T_Donnee is private;

package Creuse is


   type Cellule;
   type Ligne;

   type Ptr_Cellule is access Cellule;
   type Ptr_Ligne is access Ligne;

   type Cellule is record 
      Index: Integer;
      Donnee: T_Donnee;
      Suivant: Ptr_Cellule;
   end record;
   type Ligne is record 
      Index: Integer;
      Cellule: Ptr_Cellule;
      Suivant: Ptr_Ligne;
   end record;

   type Table_Hachage is array (Positive range <>) of Ptr_Ligne;

   type Table_Creuse(Size: Integer) is tagged record
      Table : Table_Hachage(1..Size);
   end record;

   type Retour_Lire_Valeur is record
      Ligne_Nulle : Boolean := False;
      Cellule_Nulle : Boolean := False;
      Valeur : T_Donnee;
   end record;


   procedure Initialiser (Self : in out Table_Creuse);
   procedure Inserer (Self : in out Table_Creuse; Ligne_Index : in Integer; Cellule_Index : in Integer; Valeur : in T_Donnee);
   procedure Pour_Chaque_Cellule (Self : in out Table_Creuse; P : access procedure (C : in out Ptr_Cellule ;I : in Integer; J : in Integer));
   function Lire_Valeur (Self : in out Table_Creuse; I : in Integer; J: in Integer) return Retour_Lire_Valeur;
   procedure Vider (Self : in out Table_Creuse);

private

   Taille : Integer;
   function Hachage(Index : in Integer) return Integer;



end Creuse;
