with Ada.Text_IO; use Ada.Text_IO;

package body Th is

   -----------------
   -- Initialiser --
   -----------------

   procedure Initialiser (Tab : out T_Th) is
   begin
      for i in 1 .. Capacite loop
         P_Lca.Initialiser (Tab (i));
      end loop;
   end Initialiser;

   -----------------
   -- Enregistrer --
   -----------------

   procedure Enregistrer
     (Tab : in out T_Th; Cle : in T_Cle; Donnee : in T_Donnee)
   is
   begin
      P_Lca.Enregistrer (Tab (Hachage (Cle)), Cle, Donnee);
   end Enregistrer;

   ---------------
   -- Supprimer --
   ---------------

   procedure Supprimer (Tab : in out T_Th; Cle : in T_Cle) is
   begin
      P_Lca.Supprimer (Tab (Hachage (Cle)), Cle);
   end Supprimer;

   -----------
   -- Vider --
   -----------

   procedure Vider (Tab : in out T_Th) is
   begin
      for i in 1 .. Capacite loop
         P_Lca.Vider (Tab (i));
      end loop;
   end Vider;

   --------------
   -- Est_Vide --
   --------------

   function Est_Vide (Tab : T_Th) return Boolean is
      Bool : Boolean := True;
   begin
      for i in 1 .. Capacite loop
         Bool := Bool and P_Lca.Est_Vide (Tab (i));
      end loop;

      return Bool;

   end Est_Vide;

   ------------
   -- Taille --
   ------------

   function Taille (Tab : in T_Th) return Integer is
      T : Integer := 0;
   begin
      for i in 1 .. Capacite loop
         T := T + P_Lca.Taille (Tab (i));
      end loop;
      return T;
   end Taille;

   ------------------
   -- Cle_Presente --
   ------------------

   function Cle_Presente (Tab : in T_Th; Cle : in T_Cle) return Boolean is
   begin
      return P_Lca.Cle_Presente (Tab (Hachage (Cle)), Cle);
   end Cle_Presente;

   ---------------
   -- La_Donnee --
   ---------------

   function La_Donnee (Tab : in T_Th; Cle : in T_Cle) return T_Donnee is
   begin
      return P_Lca.La_Donnee (Tab (Hachage (Cle)), Cle);
   end La_Donnee;

   -----------------
   -- Pour_Chaque --
   -----------------

   procedure Pour_Chaque (Tab : in T_Th) is
      procedure Traiter_Sda is new P_Lca.Pour_Chaque (Traiter_Cellule);
   begin
      for i in 1 .. Capacite loop
         Traiter_Sda (Tab (i));
      end loop;
   end Pour_Chaque;

end Th;
