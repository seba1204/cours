with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
with Ada.Unchecked_Deallocation;

package body Lca is

   procedure Free is new Ada.Unchecked_Deallocation
     (Object => T_Cellule, Name => T_Lca);

   procedure Initialiser (Sda : out T_Lca) is
   begin
      Sda := null;
   end Initialiser;

   function Est_Vide (Sda : T_Lca) return Boolean is
   begin
      return Sda = null;
   end Est_Vide;

   function Taille (Sda : in T_Lca) return Integer is
      Compteur     : Integer;
      Sda_En_Cours : T_Lca;
   begin
      Compteur     := 0;
      Sda_En_Cours := Sda;

      while Sda_En_Cours /= null loop
         Compteur     := Compteur + 1;
         Sda_En_Cours := Sda_En_Cours.all.Suivant;
      end loop;

      return Compteur;
   end Taille;

   procedure Enregistrer
     (Sda : in out T_Lca; Cle : in T_Cle; Donnee : in T_Donnee)
   is
      Sda_En_Cours : T_Lca;
   begin
      Sda_En_Cours := Sda;

      while Sda_En_Cours /= null
        and then
        (Sda_En_Cours.all.Suivant /= null and Sda_En_Cours.all.Cle /= Cle)
      loop
         Sda_En_Cours := Sda_En_Cours.all.Suivant;
      end loop;
      if Sda = null then
         Sda            := new T_Cellule;
         Sda.all.Cle    := Cle;
         Sda.all.Donnee := Donnee;
      elsif Sda_En_Cours.all.Cle = Cle then
         Sda_En_Cours.all.Donnee := Donnee;
      elsif Sda_En_Cours.all.Suivant = null then
         Sda_En_Cours.all.Suivant            := new T_Cellule;
         Sda_En_Cours.all.Suivant.all.Cle    := Cle;
         Sda_En_Cours.all.Suivant.all.Donnee := Donnee;
      end if;

   end Enregistrer;
   function Cle_Presente (Sda : in T_Lca; Cle : in T_Cle) return Boolean is
      Sda_En_Cours : T_Lca;
   begin
      Sda_En_Cours := Sda;
      while Sda_En_Cours /= null loop
         if Sda_En_Cours.all.Cle = Cle then
            return True;
         end if;
         Sda_En_Cours := Sda_En_Cours.all.Suivant;
      end loop;
      return False;
   end Cle_Presente;

   function La_Donnee (Sda : in T_Lca; Cle : in T_Cle) return T_Donnee is
      Sda_En_Cours : T_Lca;
      Found        : Boolean := False;
      --  note : j'ai nommé la variable en Anglais car je voudrais dire trouvé
      --  mais les accentes pour les noms de variables sont interdits
      --  et puis dans la condition, ça fait quasiment une phrase :
      --  while not found loop
   begin
      Sda_En_Cours := Sda;
      while Sda_En_Cours /= null and not Found loop
         if Sda_En_Cours.all.Cle = Cle then
            Found := True;
         else
            Sda_En_Cours := Sda_En_Cours.all.Suivant;
         end if;
      end loop;

      if Found then
         return Sda_En_Cours.all.Donnee;
      else
         raise Cle_Absente_Exception;
      end if;
   end La_Donnee;

   procedure Supprimer (Sda : in out T_Lca; Cle : in T_Cle) is
      Sda_En_Cours  : T_Lca := null;
      Sda_Precedent : T_Lca := null;
      Next : T_Lca := null;
   begin
      Sda_En_Cours := Sda;
      while Sda_En_Cours /= null and then Sda_En_Cours.all.Cle /= Cle loop
         Sda_Precedent := Sda_En_Cours;
         Sda_En_Cours  := Sda_En_Cours.all.Suivant;
      end loop;

      if Sda_En_Cours = null then
         raise Cle_Absente_Exception;
      else
         --  Sda etait initialement nulle
         if Sda_Precedent = null then
            Sda_En_Cours := Sda.all.Suivant;
            Free (Sda);
            Sda := Sda_En_Cours;
         else
            Next := Sda_En_Cours.all.Suivant;
            Free (Sda_Precedent.all.Suivant);
            Sda_Precedent.all.Suivant := Next;
         end if;
      end if;

   end Supprimer;

   procedure Vider (Sda : in out T_Lca) is
   begin
      if Sda /= null then
         Vider (Sda.all.Suivant);
         Free (Sda);
      end if;
   end Vider;

   procedure Pour_Chaque (Sda : in T_Lca) is
      Sda_En_Cours : T_Lca;
   begin
      Sda_En_Cours := Sda;
      while Sda_En_Cours /= null loop
         begin
            Traiter (Sda_En_Cours.all.Cle, Sda_En_Cours.all.Donnee);
         exception
            when others =>
               Put ("Erreur !");
               New_Line;
         end;
         Sda_En_Cours := Sda_En_Cours.all.Suivant;
      end loop;
   end Pour_Chaque;

end Lca;
