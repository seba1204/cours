with Sda_Exceptions; use Sda_Exceptions;

--  Définition de structures de données associatives sous forme d'une liste
--  chaînée associative (LCA).
generic
   type T_Cle is private;
   type T_Donnee is private;

package Lca is

   type T_Lca is limited private;

   --  Initialiser une Sda. La Sda est vide.
   procedure Initialiser (Sda : out T_Lca) with
      Post => Est_Vide (Sda);

      --  Est-ce qu'une Sda est vide ?
   function Est_Vide (Sda : T_Lca) return Boolean;

   --  Obtenir le nombre d'éléments d'une Sda.
   function Taille (Sda : in T_Lca) return Integer with
      Post => Taille'Result >= 0 and (Taille'Result = 0) = Est_Vide (Sda);

      --  Enregistrer une Donnée associée a une Clé dans une Sda. Si la
      --  clé est déja présente dans la Sda, sa donnée est changée.
   procedure Enregistrer
     (Sda : in out T_Lca; Cle : in T_Cle; Donnee : in T_Donnee) with
      Post => Cle_Presente
        (Sda, Cle) and then
      (La_Donnee (Sda, Cle) =
       Donnee)                    -- donnée insérée
      --  and then (if not (Cle_Presente (Sda, Cle)'Old) then Taille (Sda)
      --  = Taille (Sda)'Old) and then (if Cle_Presente (Sda, Cle)'Old then
      --  Taille (Sda) = Taille (Sda)'Old + 1)
      ;

      --  Savoir si une Clé est présente dans une Sda.
   function Cle_Presente (Sda : in T_Lca; Cle : in T_Cle) return Boolean;

   --  Obtenir la donnée associée a une Cle dans la Sda. Exception :
   --  Cle_Absente_Exception si Clé n'est pas utilisée dans l'Sda
   function La_Donnee (Sda : in T_Lca; Cle : in T_Cle) return T_Donnee;

   --  Supprimer la Donnée associée a une Clé dans une Sda. Exception :
   --  Cle_Absente_Exception si Clé n'est pas utilisée dans la Sda
   procedure Supprimer (Sda : in out T_Lca; Cle : in T_Cle) with
      Post => Taille
        (Sda) = Taille (Sda)'Old -
        1           -- un élément de moins
      and
      not Cle_Presente (Sda, Cle);         -- la clé a été supprimée

      --  Supprimer tous les éléments d'une Sda.
   procedure Vider (Sda : in out T_Lca) with
      Post => Est_Vide (Sda);

      --  Appliquer un traitement (Traiter) pour chaque couple d'une Sda.
   generic
      with procedure Traiter (Cle : in T_Cle; Donnee : in T_Donnee);
   procedure Pour_Chaque (Sda : in T_Lca);

private

   type T_Cellule;
   type T_Lca is access T_Cellule;
   type T_Cellule is record
      Cle     : T_Cle;
      Donnee  : T_Donnee;
      Suivant : T_Lca;
   end record;

end Lca;
