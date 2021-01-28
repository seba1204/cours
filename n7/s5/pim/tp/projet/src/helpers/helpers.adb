package body Helpers is

   function "-" (Item : in String) return Integer is
   begin
      return Integer'Value(Item);
   end "-";

   function "+" (Item : in String) return Unbounded_String renames To_Unbounded_String;

   function T (Item : in Unbounded_String) return String is
   begin
      return To_String(Item);
   end T;

   function Est_Nom_Fichier_Net(Argument : in String) return Boolean is
      Longueur : Integer;  -- Longueur de l'argument
   begin
      begin
         Longueur := Argument'Length;
         if Longueur > 3 then
            return (Argument(Longueur - 3..Longueur)) = ".net";
         else 
            return False;
         end if;
      exception
         when others => return False;
      end;
   end Est_Nom_Fichier_Net;

   --------------------
   -- Lire_Arugments --
   --------------------

   function Lire_Arugments return Args is
      A : Args;
      Compteur : Integer := 1;
      Net_File : Ada.Text_IO.File_Type;
      DEM : String := " Pour plus d'aide sur les arguments, tapez './pagerank -h'.";

      procedure Est_Naif is begin
         A.Est_Naif := False;
         Compteur := Compteur + 1;
      end Est_Naif;

      procedure Max_Iter is begin
         Compteur := Compteur + 1;
         if -Argument(Compteur) > 0 then
            A.Max_Iter := -Argument (Compteur);
            Compteur := Compteur + 1;
         else
            raise Erreur_Mauvais_Parametre_Iteration;
         end if;
      end Max_Iter;

      procedure Alpha is begin
         Compteur := Compteur + 1;
         if Float'Value(Argument (Compteur)) > 0.0 then
            A.A := Float'Value(Argument (Compteur));
            Compteur := Compteur + 1;
         else
            raise Erreur_Mauvais_Parametre_Alpha;
         end if;
      end Alpha;

      procedure Aide_Demande is begin
         A.Aide_Demande := True;
         Compteur := Compteur + 1;
      end Aide_Demande;

      procedure Est_Verbeux is begin
         Verbeux := True;
         Compteur := Compteur + 1;
      end Est_Verbeux;
      
      procedure Taille_Hachage is begin
         Compteur := Compteur + 1;
         if -Argument (Compteur) > 0 then
            A.Taille_Hachage := -Argument (Compteur);
            Compteur := Compteur + 1;
         else
            raise Erreur_Mauvais_Parametre_Taille_Hachage;
         end if;
      end Taille_Hachage;

      procedure Nom_Fichier is begin
         if Est_Nom_Fichier_Net(Argument(Compteur)) then
            A.Nom_Fichier := +Argument (Compteur);
            Compteur := Compteur + 1;
         else
            raise Erreur_Lire_Args;
         end if;
      end Nom_Fichier;

      
      procedure Active_Matlab is begin
         Matlab := True;
         Compteur := Compteur + 1;
      end Active_Matlab;

      function AF (Input : in String) return Character is
         Longueur : Integer;  -- Longueur de l'argument
      begin
         begin
            Longueur := Input'Length;
            if Longueur = 2 then
               return Character(Input(Input'First + 1));
            else 
               return 'x';
            end if;
         exception
            when others => return 'x';
         end;
      end AF;
   begin
      begin
         Nettoyer_Console;
         if Argument_Count < 1 then
            raise Erreur_Argument_Manquant;

         else
            -- Boucle sur les arguments
            while Compteur <= Argument_Count loop
               case AF(Argument (Compteur)) is
                  when 'P' | 'p' => Est_Naif;
                  when 'I' | 'i' => Max_Iter;
                  when 'A' | 'a' => Alpha;
                  when 'H' | 'h' => Aide_Demande;
                  when 'V' | 'v' => Est_Verbeux;
                  when 'D' | 'd' => Taille_Hachage;
                  when 'M' | 'm' => Active_Matlab;
                  when others => Nom_Fichier;
               end case;
            end loop;

            if A.Aide_Demande then
               Afficher_Aide;
            elsif To_String(A.Nom_Fichier)'Length < 3 then
               raise ERREUR_Mauvais_Parametre_Fichier;
            else
               begin
                  Open(Net_File, In_File, To_String(A.Nom_Fichier));
                  Get(Net_File, A.Taille_Reseau);
                  Close(Net_File);
               exception
                  when others =>
                     raise ERREUR_Fichier_Manquant;
               end;
            end if;
         end if;
         return A;
      exception
         when Erreur_Argument_Manquant =>
            raise Erreur_Lire_Args with "Veuillez renseigner le nom du fichier .net." & DEM;

         when Erreur_Mauvais_Parametre_Iteration =>
            raise Erreur_Lire_Args with "Mauvais parametre d'iteration." & DEM;

         when Erreur_Mauvais_Parametre_Alpha =>
            raise Erreur_Lire_Args with "Mauvais parametre alpha." & DEM;
            
         when Erreur_Mauvais_Parametre_Taille_Memoire =>
            raise Erreur_Lire_Args with "Mauvais parametre taille memoire." & DEM;
            
         when Erreur_Mauvais_Parametre_Taille_Hachage =>
            raise Erreur_Lire_Args with "Mauvais parametre taille de tableau de hachage." & DEM;

         when ERREUR_Mauvais_Parametre_Fichier =>
            raise Erreur_Lire_Args with "Fichier .net manquant, veuillez indiquez un le nom du fichier (extension comprise)" & DEM;

         when ERREUR_Fichier_Manquant =>
            raise Erreur_Lire_Args with "Fichier .net introuvable ou illisible. Verifiez le chemin d'acces" & DEM;

         when others =>
            raise Erreur_Lire_Args with "Un probleme a ete rencontre lors du traitrement des arguments, l'operation n'a pas abouti" & DEM;
      end;
   end Lire_Arugments;

   procedure Log(Message : in String) is 
   begin
      if Verbeux and not(Matlab) then
         Put_Line(Message);
      end if;
   end Log;

   LP : Integer := 0;

   procedure Log_P(Progression : in Integer; Max : in Integer) is 
      P : Integer;
   begin
      if Verbeux and not(Matlab) then
         P := Progression * 100 / Max;
         if (Progression = 1) then
            LP := 0;
         end if;
         if P /= LP then
            for I in 1..(P-LP) loop
               -- Put("█");
               Put("-");
            end loop;
            if P + P - LP > 100 then
               New_Line;
            end if;
            LP := P;
         end if;
      end if;
   end Log_P;

   procedure Log_Matlab(Duree : in Integer) is 
   begin
      if Verbeux and Matlab then
         Put(Integer'Image(Duree));
      end if;
   end Log_Matlab;

  function Chemin (Nom_Fichier : in String) return String is
      Compteur : Integer;
   begin
      begin
         Compteur := Nom_Fichier'Length;
         while Compteur > 0 and then (Nom_Fichier(Compteur) /= '/' and Nom_Fichier(Compteur) /= '\') loop
            Compteur := Compteur - 1;
         end loop;
         if Compteur > 1 then
            return Nom_Fichier(Nom_Fichier'First..Compteur);
         else
            return "./";
         end if;
      exception
         when others => 
            Put_Line("Une erreur est survenue dans la lecture du chemin du nom du fichier .net.");
            Put_Line("Les fichiers de sortis seront alors crees dans le dossier ou se trouve pagerank.");
            return "./";
      end;
   end Chemin;

   function Nom (Nom_Fichier : in String) return String is
      Debut : Integer;
      Fin : Integer;
   begin
      begin
         Debut := Nom_Fichier'Length;
         Fin := Nom_Fichier'Length;
         while Debut > 0 and then (Nom_Fichier(Debut) /= '/' and Nom_Fichier(Debut) /= '\') loop
            Debut := Debut - 1;
         end loop;
         
         while Fin > 0 and then Nom_Fichier(Fin) /= '.' loop
            Fin := Fin - 1;
         end loop;
         Fin := Fin - 1;
         if Debut < Fin and Debut >= 1 then
            return Nom_Fichier(Debut..Fin);
         else
            return "sorti";
         end if;
      exception
         when others => 
            Put_Line("Une erreur est survenue dans la lecture du chemin du fichier .net.");
            Put_Line("Les fichiers de sortis seront alors creesavec le nom 'sorti'.");
            return "sorti";
      end;
   end Nom;

   function Octets (R : in Integer) return Integer is
      A : Integer := R;
      D : Integer := 0;
   begin
      if R = 0 then
         return 1;
      end if;
      while(A > 0) loop
         A := A / 10;
         D := D + 1;
      end loop;
      D := D;
      return D;
   end Octets;

   
   function Humaniser (Duree : in Duration) return String is
   Millisecondes : Integer;
   Secondes : Integer;
   Minutes : Integer;
   begin
      Millisecondes := Integer(duree * 1000);
      if Millisecondes > 1000 then
         Secondes := Millisecondes / 1000;
         Millisecondes := Millisecondes mod 1000;
         if Secondes > 60 then
            Secondes := Secondes / 60;
            Minutes := Secondes mod 60;
            return (Integer'Image(Minutes) & " m " & Integer'Image(Secondes)  & " s.");
         end if;
         return (Integer'Image(Secondes) & " s " & Integer'Image(Millisecondes)  & " ms.");
      end if;
      return (Integer'Image(Millisecondes) & " ms.");
   end Humaniser;


   procedure Nettoyer_Console is
      Preambule : constant Character := Character'Val (8#33#); -- '\033'
      Caractere_Vidange: constant String    := "[2J";
      Caractere_Plein : constant String    := "[;H";
      Sequence: constant String := Preambule & Caractere_Vidange & Preambule & Caractere_Plein;
   begin
      Put (Sequence);
   end Nettoyer_Console;


   procedure Afficher_Aide is
   begin
      Put_Line("Bienvenue dans l'aide de pagerank.");
      Put_Line("La commande peut prendre 7 arguments differents.");
      Put_Line("Un argument est une lettre precedee d'un tiret et eventuellement");
      Put_Line("suivie d'un parametre.");
      Put_Line("Les arguments sont insensibles a la casse.");
      Put_Line("L'ordre des arguments n'a pas d'importance.");      
      Put_Line("Les fichiers de sortie sont crees dans le meme dossier que le fichier d'entree .net.");
      New_Line;
      Put_Line("    -P : [Optionnel] Permet de choisir l'implementation creuse");
      Put_Line("         de Google. Si cet argument n'est pas present, c'est");
      Put_Line("         l'implementation naive qui est choisie.");
      New_Line;
      Put_Line("    -I : [Optionnel] Doit etre suivi d'un nombre entier.");
      Put_Line("         Le nombre doit etre un entier positif.");
      Put_Line("         Permet de parametrer le nombre d'iterations faites");
      Put_Line("         pour calculer les poids. Valeur par defaut : 150");
      New_Line;
      Put_Line("    -A : [Optionnel] Doit etre suivi d'un reel (ex : 0.85).");
      Put_Line("         Le parametre doit etre un reel compris entre 0 et 1.");
      Put_Line("         Permet d'indiquer le parametre alpha du calcul de");
      Put_Line("         la matrice Google.");
      New_Line;
      Put_Line("    -V : [Optionnel] Active le mode verbeux.");
      Put_Line("         Si active, toutes les etapes de calcul seront decrites");
      New_Line;
      Put_Line("    -D : [Optionnel] Doit etre suivi d'un nombre entier.");
      Put_Line("         Parametre definissant la taille du tableau de hachage pour");
      Put_Line("         l'implementation creuse.");
      Put_Line("         Valeur par defaut : 100");
      New_Line;
      Put_Line("    -M : [Optionnel] Active le mode Matlab");
      Put_Line("         Aucun log n'est affiche, sauf a la fin du programme pour afficher");
      Put_Line("         le temps d'execution.");
      New_Line;
      Put_Line("    -H : [Optionnel] Affiche cet aide.");
      New_Line;
      Put_Line("    <nom_fichier.net> : [Obligatoire]");
      Put_Line("         La ligne de commande doit se terminer par le nom du fichier");
      Put_Line("         .net qui contient les liens entre les pages web.");
   end Afficher_Aide;
end Helpers;
