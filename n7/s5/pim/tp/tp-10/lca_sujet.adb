with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Lca;

-- Exemple d'utilisation des vecteurs creux.
procedure LCA_Sujet is

   -- On instancie le module LCA
   package Dictionnaire is new Lca
     (T_Cle => Unbounded_String, T_Donnee => Integer);
   use Dictionnaire;

   procedure Afficher_T (Cle : in Unbounded_String; Donnee : in Integer) is
   begin
      Put (To_String (Cle));
      Put (": ");
      Put_Line (Integer'Image (Donnee));
   end Afficher_T;

   procedure Afficher is new Dictionnaire.Pour_Chaque (Traiter => Afficher_T);

   Nombre_Dic : T_Lca;

begin
   Put_Line ("=========Début des tests=========");
   Put_Line ("Initialisation la SDA...");
   Initialiser (Nombre_Dic);
   Put_Line ("ok !");
   Put_Line ("Enregistrement de cinq couples ...");
   Enregistrer (Nombre_Dic, To_Unbounded_String ("un"), 1);
   Enregistrer (Nombre_Dic, To_Unbounded_String ("deux"), 2);
   Enregistrer (Nombre_Dic, To_Unbounded_String ("trois"), 3);
   Enregistrer (Nombre_Dic, To_Unbounded_String ("quatre"), 4);
   Enregistrer (Nombre_Dic, To_Unbounded_String ("cinq"), 5);
   Put_Line ("ok !");
   Put_Line ("Suppression du 1er couple ...");
   Supprimer (Nombre_Dic, To_Unbounded_String ("un"));
   Put_Line ("ok !");
   Put_Line ("Affichage du dictionnaire...");
   Afficher (Nombre_Dic);
   Put_Line ("ok !");
   Put_Line ("Enregistrement d'un nouveau couple ...");
   Enregistrer (Nombre_Dic, To_Unbounded_String ("un"), 1);
   Put_Line ("ok !");
   Put_Line ("Affichage du dictionnaire...");
   Afficher (Nombre_Dic);
   Put_Line ("ok !");
   Put_Line ("Calcul de la taille du dictionnaire...");
   Put_Line (Integer'Image (Taille (Nombre_Dic)));
   Put_Line ("ok !");
   Put_Line ("Effacement du dictionnaire...");
   Vider (Nombre_Dic);
   Put_Line ("ok !");
   Put_Line ("=========Fin des tests=========");
end LCA_Sujet;
