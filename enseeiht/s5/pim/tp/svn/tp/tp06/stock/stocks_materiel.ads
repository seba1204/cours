
-- Auteur: PONT Sébastien
-- Gérer un stock de matériel informatique.

package Stocks_Materiel is


   CAPACITE : constant Integer := 10; -- nombre maximum de matériels dans un stock

   type T_Nature is (UNITE_CENTRALE, DISQUE, ECRAN, CLAVIER, IMPRIMANTE);
   type T_Etat is (MARCHE, HS);
   type T_Stock is limited private;
   type T_Materiel is limited private;
   type T_Tableau is limited private;
   
   -- Exceptions
   
   Stock_Plein : EXCEPTION;



    -- Créer un stock vide.
    --
    -- paramètres
    --     Stock : le stock à  créer
    --
    -- Assure
    --     Nb_Materiels (Stock) = 0
    --
    procedure Creer (Stock : out T_Stock) with
        Post => Nb_Materiels (Stock) = 0;


    -- Obtenir le nombre de matériels dans le stock Stock.
    --
    -- Paramètres
    --    Stock : le stock dont ont veut obtenir la taille
    --
    -- Nécessite
    --     Vrai
    --
    -- Assure
    --     Résultat >= 0 Et Résultat <= CAPACITE
    --
    function Nb_Materiels (Stock: in T_Stock) return Integer with
        Post => Nb_Materiels'Result >= 0 and Nb_Materiels'Result <= CAPACITE;

    -- Obtenir le nombre de materiels qui sont hors d etat de fonctionnement.
    --
    -- Paramètres
    --    Stock : le stock dans lequel on cherche le matériel HS.
    --
    -- Nécessite
    --     Vrai
    --
    -- Assure
    --     Résultat >= 0 Et Résultat <= CAPACITE
    --
    function Nb_Materiels_HS (Stock: in T_Stock) return Integer with
     Post => Nb_Materiels_HS'Result >= 0 and Nb_Materiels_HS'Result <= CAPACITE;
   
   
   -- Mettre à jour l’état d’un matériel enregistrer dans le stock à partir de 
   -- son numéro de série.   
   --   
   -- Parametres
   --    Stock : le stock dont ont veut obtenir la taille
   --    Numero_Serie : le numéro de série de l'élément à meetre a jour
   --
   -- Necessite
   --     Vrai
   --
   -- Assure
   --     Matériel mise à jour
   --
   procedure Maj_Etat (
                       Stock: in out T_Stock;
                       Numero_Serie : in Integer;
                       Etat : in T_Etat
                      ) with
     Post => Stock.Tableau(Numero_Serie).Etat = Etat;
   
   
   -- Enregistrer un nouveau métériel dans le stock.  Il est en
   -- fonctionnement.  Le stock ne doit pas être plein.
   -- 
   -- Paramètres
   --    Stock : le stock à  compléter
   --    Numero_Serie : le numéro de série du nouveau matériel
   --    Nature       : la nature du nouveau matériel
   --    Annee_Achat  : l'année d'achat du nouveau matériel
   -- 
   -- Nécessite
   --    Nb_Materiels (Stock) < CAPACITE
   -- 
   -- Assure
   --    Nouveau matériel ajouté
   --    Nb_Materiels (Stock) = Nb_Materiels (Stock)'Avant + 1
   procedure Enregistrer (
                          Stock        : in out T_Stock;
                          Numero_Serie : in     Integer;
                          Nature       : in     T_Nature;
                          Annee_Achat  : in     Integer
                         ) with
     Pre => Nb_Materiels (Stock) < CAPACITE,
     Post => Nb_Materiels (Stock) = Nb_Materiels (Stock)'Old + 1;
 
 

 
private
    type T_Materiel is record
         Numero_Serie : Integer;
         Nature : T_Nature;
         Annee_Achat : Integer;
         Etat : T_Etat;

         -- invariants de type :
         -- Annee >= 0
         -- 
   end record;

   type T_Tableau is array(1..CAPACITE) of T_Materiel;

   type T_Stock is record
      Tableau : T_Tableau;
      Longueur : Integer;
      Nb_HS : Integer;
   end record;
   

end Stocks_Materiel;
