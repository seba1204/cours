-- with Ada.Text_IO;          use Ada.Text_IO;
-- with Ada.Integer_Text_IO;  use Ada.Integer_Text_IO;

-- Auteur: 
-- Gérer un stock de matériel informatique.
--
package body Stocks_Materiel is

   
   procedure Creer (Stock : out T_Stock) is
   begin
      Stock.Longueur := 0;
   end Creer;   


   function Nb_Materiels (Stock: in T_Stock) return Integer is
   begin
      return Stock.Longueur;
   end;


   function Nb_Materiels_HS (Stock: in T_Stock) return Integer is
   begin
      return Stock.Nb_Materiels_HS;
   end;

   procedure Maj_Etat (
                       Stock: out T_Stock;
                       Numero_Serie : in Integer;
                       Etat : Boolean;
                      ) is
   begin
      Stock.Tableau(Numero_Serie).Etat := Etat;
   end;

   procedure Enregistrer (                          
                          Stock        : in out T_Stock;                          
                          Numero_Serie : in     Integer;                          
                          Nature       : in     T_Nature;                          
                          Annee_Achat  : in     Integer                            
                                                   ) is
      Nouveau_Materiel : T_Materiel;
   begin
      if Nb_Materiels(Stock) + 1 >= CAPACITE then
         raise Stock_Plein;
      else         
         Nouveau_Materiel.Numero_Serie := Numero_Serie;
         Nouveau_Materiel.Nature := Nature;
         Nouveau_Materiel.Annee_Achat := Annee_Achat;
         Nouveau_Materiel.Etat := MARCHE;
         Stock.Tableau(Nb_Materiels(Stock)  + 1) := Nouveau_Materiel;
         Stock.Longueur := Stock.Longueur + 1;
      end if;
    end;


end Stocks_Materiel;
