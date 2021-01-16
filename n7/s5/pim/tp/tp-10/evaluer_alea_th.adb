with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
with Ada.Command_Line;    use Ada.Command_Line;
with Sda_Exceptions;      use Sda_Exceptions;
with Alea;
with Th;

--  Évaluer la qualité du générateur aléatoire et les SDA.
procedure Evaluer_Alea_Th is

   -- Afficher l'usage.
   procedure Afficher_Usage is
   begin
      New_Line;
      Put_Line ("Usage : " & Command_Name & " Borne Taille");
      New_Line;
      Put_Line ("   Borne  : les nombres sont tirés dans l'intervalle 1..Borne");
      Put_Line ("   Taille : la taille de l'échantillon");
      New_Line;
   end Afficher_Usage;

   --  Afficher le Nom et la Valeur d'une variable. La Valeur est affichée sur la Largeur_Valeur
   --  précisée.
   procedure Afficher_Variable (Nom : String; Valeur : in Integer; Largeur_Valeur : in Integer := 1)
   is
   begin
      Put (Nom);
      Put (" : ");
      Put (Valeur, Largeur_Valeur);
      New_Line;
   end Afficher_Variable;

   --  Évaluer la qualité du générateur de nombre aléatoire Alea sur un intervalle
   --  donné en calculant les fréquences absolues minimales et maximales des entiers obtenus
   --  lors de plusieurs tirages aléatoires.
   --
   -- Paramètres :
   --        Borne: in Entier      -- le nombre aléatoire est dans 1..Borne
   --        Taille: in Entier -- nombre de tirages (taille de l'échantillon)
   --        Min, Max: out Entier -- fréquence minimale et maximale
   --
   -- Nécessite :
   --    Borne > 1
   --    Taille > 1
   --
   --  Assure : -- poscondition peu intéressante !
   --    0 <= Min Et Min <= Taille
   --    0 <= Max Et Max <= Taille
   --    Min + Max <= Taille
   --    Min <= Moyenne Et Moyenne <= Max
   --
   --  Remarque : On ne peut ni formaliser les 'vraies' postconditions, ni écrire de programme de
   --  test car on ne maîtrise par le générateur aléatoire. Pour écrire un programme
   --  de test, on pourrait remplacer le générateur par un générateur qui fournit
   --  une séquence connue d'entiers et pour laquelle on pourrait déterminer les données
   --  statistiques demandées. Ici, pour tester on peut afficher les nombres aléatoires et
   --  refaire les calculs par ailleurs pour vérifier que le résultat produit est le bon.
   procedure Calculer_Statistiques
     (Borne  : in Integer;  -- Borne supérieur de l'intervalle de recherche
      Taille : in Integer;  -- Taille de l'échantillon
      Min,
      Max : out Integer  -- min et max des fréquences de l'échantillon
   ) with
      pre  => Borne > 1 and Taille > 1,
      post => 0 <= Min and Min <= Taille and 0 <= Max and Max <= Taille and Min + Max <= Taille
   is
      package Mon_Alea is new Alea (1, Borne);
      use Mon_Alea;

      Longueur : constant Integer := 1000;

      function Hachage (Cle : in Integer) return Integer is
      begin
         return Cle mod Longueur + 1;
      end Hachage;

      -- On instancie le module Th
      package Table_Hachage is new Th
      (Integer, Integer, Longueur, Hachage);
      use Table_Hachage;

      
      Mini, Maxi : Integer;

      procedure Compare_Mini (Cle : in Integer; Donnee : in Integer) is
      begin
         if Donnee < Mini then
            Mini := Donnee;
         end if;
      end Compare_Mini;

      procedure Compute_Mini is new Table_Hachage.Pour_Chaque (Compare_Mini);

      Tab : Table_Hachage.T_Th;
      Rd_Nb : Integer := 0;
      Nombre_Apparition : Integer := 0;
   begin
      Initialiser(Tab);
      Maxi := 0;
      Mini := Taille;

      for i in 1..Taille loop
         Get_Random_Number(Rd_Nb);
         if (Cle_Presente(Tab, Rd_Nb)) then
            Nombre_Apparition := La_Donnee(Tab, Rd_Nb) + 1;
         else
            Nombre_Apparition := 1;
         end if;
         if Nombre_Apparition > Maxi then
            Maxi := Nombre_Apparition;
         end if;
         Enregistrer(Tab, Rd_Nb, Nombre_Apparition);
      end loop;
      Compute_Mini(Tab);
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

      Calculer_Statistiques (Borne, Taille, Min, Max);

      --  Afficher les fréquence Min et Max
      Afficher_Variable ("Min", Min);
      Afficher_Variable ("Max", Max);
   end if;

exception
   when CONSTRAINT_ERROR => Put_Line("Les arguments doivent être des entiers");
   when others => Put_Line("Erreur");

end Evaluer_Alea_Th;
