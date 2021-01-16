with Sda_Exceptions; use Sda_Exceptions;
with Lca;
--  Définition de structures de données associatives sous forme d'une
--  liste chaînée associative (LCA) avec table de hachage (TH).
generic
   type T_Cle is private;
   type T_Donnee is private;
   Capacite : Integer;
   with function Hachage (Cle : in T_Cle) return Integer;

package Th is

   type T_Th is limited private;

   procedure Initialiser (Tab : out T_Th);
   procedure Enregistrer
     (Tab : in out T_Th; Cle : in T_Cle; Donnee : in T_Donnee);
   procedure Supprimer (Tab : in out T_Th; Cle : in T_Cle);
   procedure Vider (Tab : in out T_Th);
   function Est_Vide (Tab : T_Th) return Boolean;
   function Taille (Tab : in T_Th) return Integer;
   function Cle_Presente (Tab : in T_Th; Cle : in T_Cle) return Boolean;
   function La_Donnee (Tab : in T_Th; Cle : in T_Cle) return T_Donnee;

   generic
      with procedure Traiter_Cellule (Cle : in T_Cle; Donnee : in T_Donnee);
   procedure Pour_Chaque (Tab : in T_Th);

private

   -- Instanciation du package Lca
   package P_Lca is new Lca (T_Cle, T_Donnee);
   use P_Lca;

   type T_Th is array (1 .. Capacite) of T_Lca;

end Th;
