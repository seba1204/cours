-- with Ada.Text_IO;          use Ada.Text_IO;
-- with Ada.Integer_Text_IO;  use Ada.Integer_Text_IO;
with Stocks_Materiel;      use Stocks_Materiel;

-- Auteur: 
-- Gerer un stock de materiel informatique.
--
procedure Scenario_Stock is

    Mon_Stock : T_Stock;
begin
   -- Creer un stock vide
   Creer (Mon_Stock);
   pragma Assert (Nb_Materiels (Mon_Stock) = 0);
   
   -- Enregistrer quelques materiels
   Enregistrer (Mon_Stock, 1012, UNITE_CENTRALE, 2016);
   pragma Assert (Nb_Materiels (Mon_Stock) = 1);
   
   Enregistrer (Mon_Stock, 2143, ECRAN, 2016);
   pragma Assert (Nb_Materiels (Mon_Stock) = 2);
   
   Enregistrer (Mon_Stock, 3001, IMPRIMANTE, 2017);
   pragma Assert (Nb_Materiels (Mon_Stock) = 3);
   
   Enregistrer (Mon_Stock, 3012, UNITE_CENTRALE, 2017);
   pragma Assert (Nb_Materiels (Mon_Stock) = 4);
   
   -- Rendre certains matériels HS
   Maj_Etat (Mon_Stock, 1012, HS);
   Maj_Etat (Mon_Stock, 3001, HS);
   pragma Assert (Nb_Materiels_HS (Mon_Stock) = 2);
   
end Scenario_Stock;
