with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
with Ada.Command_Line;    use Ada.Command_Line;
with Sda_Exceptions;      use Sda_Exceptions;
with Alea;
with Lca;

--  Evaluer la qualité du générateur aléatoire et les SDA.
procedure Evaluer_Alea_Lca is
   procedure Afficher_Usage is
   begin
      New_Line;
      Put_Line ("Usage : " & Command_Name & " Borne Taille");
      New_Line;
      Put_Line ("   Borne  : les nombres sont tirés dans l'intervalle 1..Borne");
      Put_Line ("   Taille : la taille de l'échantillon");
      New_Line;
   end Afficher_Usage;
   
   procedure Afficher_Variable (Nom : String; Valeur : in Integer; Largeur_Valeur : in Integer := 1)
   is
   begin
      Put (Nom);
      Put (" : ");
      Put (Valeur, Largeur_Valeur);
      New_Line;
   end Afficher_Variable;

   procedure Calculer_Statistiques
     (Borne  : in Integer;  -- Borne supérieur de l'intervalle de recherche
      Taille : in Integer;  -- Taille de l'échantillon
      Min,
      Max : out Integer  -- min et max des fréquences de l'échantillon
   ) with
      Pre  => Borne > 1 and Taille > 1,
      Post => 0 <= Min and Min <= Taille and 0 <= Max and Max <= Taille and Min + Max <= Taille
   is
      package Mon_Alea is new Alea (1, Borne);
      use Mon_Alea;

      -- On instancie le module LCA
      package Nombres is new Lca
      (T_Cle => Integer, T_Donnee => Integer);
      use Nombres;
      
      Mini, Maxi : Integer;

      procedure Compare_Mini (Cle : in Integer; Donnee : in Integer) is
      begin
         if Donnee < Mini then
            Mini := Donnee;
         end if;
      end Compare_Mini;

      procedure Compute_Mini is new Nombres.Pour_Chaque (Compare_Mini);


      Liste_Nombres : T_Lca;
      Rd_Nb : Integer := 0;
      Nombre_Apparition : Integer := 0;
   begin

      Initialiser(Liste_Nombres);
      Maxi := 0;
      Mini := Taille;
      
      -- On tire au hasard un nouveau nombre
      -- Si ce nombre apprait déjà dans les clés de la Liste_Nombres
      -- Alors on incrémente sa fréquence, sinon on initialise sa fréquence à 1

      for i in 1..Taille loop
         Get_Random_Number(Rd_Nb);
         if (Cle_Presente(Liste_Nombres, Rd_Nb)) then
            Nombre_Apparition := La_Donnee(Liste_Nombres, Rd_Nb) + 1;
         else
            Nombre_Apparition := 1;
         end if;
         if Nombre_Apparition > Maxi then
            Maxi := Nombre_Apparition;
         end if;
         Enregistrer(Liste_Nombres, Rd_Nb, Nombre_Apparition);
      end loop;
      Compute_Mini(Liste_Nombres);
      Min := Mini;
      Max := Maxi;
   end Calculer_Statistiques;

   

   Min, Max : Integer; -- fréquence minimale et maximale d'un échantillon
   Borne    : Integer;    -- les nombres aléatoire sont tirés dans 1..Borne
   Taille   : Integer;   -- nombre de tirages aléatoires
begin
   if Argument_Count /= 2 then
      Afficher_Usage;
   else
      --  Récupérer les arguments de la ligne de commande
      Borne  := Integer'Value (Argument (1));
      Taille := Integer'Value (Argument (2));

      --  Afficher les valeur de Borne et Taille
      Afficher_Variable ("Borne ", Borne);
      Afficher_Variable ("Taille", Taille);

      Put_Line("Calcul des statistiques en cours...");

      Calculer_Statistiques (Borne, Taille, Min, Max);

      --  Afficher les fréquence Min et Max
      Afficher_Variable ("Min", Min);
      Afficher_Variable ("Max", Max);
      Afficher_Variable ("Dif", Max - Min);
   end if;

exception
   when CONSTRAINT_ERROR => Put_Line("Les arguments doivent être des entiers");
   when others => Put_Line("Erreur");
end Evaluer_Alea_Lca;
