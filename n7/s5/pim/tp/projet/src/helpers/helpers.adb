package body Helpers is

   function "+" (Item : in String) return Unbounded_String renames To_Unbounded_String;
   function "&" (Left, Right : in Unbounded_String) return Unbounded_String is
      Temp_Unbounded_String : Unbounded_String;
   begin
      Temp_Unbounded_String := Left;
      Append(Temp_Unbounded_String, Right);
      return Temp_Unbounded_String;
   end "&";
   
   -- function "&" (Left: in Unbounded_String; Right: in String) return Unbounded_String is 
   -- begin
   --    return Left & To_Unbounded_String(Right);
   -- end "&";
   -- function "&" (Left: in Unbounded_String; Right: in Integer) return Unbounded_String is 
   -- begin
   --    return Left & To_Unbounded_String(Integer'Image(Right));
   -- end "&";
   -- function "&" (Left: in Unbounded_String; Right: in Float) return Unbounded_String is 
   -- begin
   --    return Left & To_Unbounded_String(Float'Image(Right));
   -- end "&";
   -- function "&" (Left: in String; Right: in Unbounded_String ) return Unbounded_String is 
   -- begin
   --    return To_Unbounded_String(Left) & Right;
   -- end "&";
   -- function "&" (Left: in Integer; Right: in Unbounded_String ) return Unbounded_String is 
   -- begin
   --    return To_Unbounded_String(Integer'Image(Left)) & Right;
   -- end "&";
   -- function "&" (Left: in Float; Right: in Unbounded_String ) return Unbounded_String is 
   -- begin
   --    return To_Unbounded_String(Float'Image(Left)) & Right;
   -- end "&";
   function "-" (Item : in String) return Integer is
   begin
      return Integer'Value(Item);
   end "-";
   function T (Item : in Unbounded_String) return String is
   begin
      return To_String(Item);
   end T;
   function Compter (Chaine : in Unbounded_String; Schema : in Character) return Integer is
      Compteur : Integer;
   begin
      for i in 1..T(Chaine)'Last loop
         if To_String(Chaine)(i) = Schema then
            Compteur := Compteur + 1;
         end if;
      end loop;
      return Compteur;
   end Compter;
   

   
   ----------------------
   -- Nettoyer_Console --
   ----------------------
   -- Code pris sur internet
   -- Auteur : annexi-strayline
   -- Source : Reddit
   procedure Nettoyer_Console is
      Preambule : constant Character := Character'Val (8#33#); -- '\033'
      Caractere_Vidange: constant String    := "[2J";
      Caractere_Plein : constant String    := "[;H";
      Sequence: constant String := Preambule & Caractere_Vidange & Preambule & Caractere_Plein;
   begin
      Put (Sequence);
   end Nettoyer_Console;


   -------------------
   -- Afficher_Aide --
   -------------------

   procedure Afficher_Aide is
   begin
      Put_Line("Bienvenue dans l'aide de pagerank.");
      Put_Line("La commande peut prendre 4 arguments differents.");
      Put_Line("Un argument est une lettre precedee d'un tiret et eventuellement");
      Put_Line("suivie d'un parametre.");
      Put_Line("Les arguments sont insensibles à la casse.");
      Put_Line("L'ordre des arguments n'a pas d'importance.");      
      Put_Line("Les fichiers de sortie sont crees dans le meme dossier que le fichier d'entree .net.");
      New_Line;
      Put_Line("    -P : [Optionnel] Permet de choisir l'implementation creuse");
      Put_Line("         de T_Google. Si cet argument n'est pas present, c'est");
      Put_Line("         l'implementation naive qui est choisie.");
      New_Line;
      Put_Line("    -I : [Optionnel] Doit être suivi d'un nombre entier.");
      Put_Line("         Le nombre doit être un entier positif.");
      Put_Line("         Permet de parametrer le nombre d'iterations faites");
      Put_Line("         pour calculer les poids. Valeur par defaut : 150");
      New_Line;
      Put_Line("    -A : [Optionnel] Doit être suivi d'un reel (ex : 0.85).");
      Put_Line("         Le parametre doit être un reel compris entre 0 et 1.");
      Put_Line("         Permet d'indiquer le parametre alpha du calcul de");
      Put_Line("         la matrice Google.");
      New_Line;
      Put_Line("    -H : [Optionnel] Affiche cet aide.");
      New_Line;
      Put_Line("    <nom_fichier.net> : [Obligatoire]");
      Put_Line("         La ligne de commande doit se terminer par le nom du fichier");
      Put_Line("         .net qui contient les liens entre les pages web.");
   end Afficher_Aide;

   ---------------
   -- Lire_Args --
   ---------------
   function Est_Nom_Fichier(Argument : in String) return Boolean is
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
   end Est_Nom_Fichier;

   function Chemin (Nom_Fichier : in Unbounded_String) return String is
      Compteur : Integer;
   begin
      begin
         Compteur := T(Nom_Fichier)'Length;
         while Compteur > 0 and then (T(Nom_Fichier)(Compteur) /= '/' and T(Nom_Fichier)(Compteur) /= '\') loop
            Compteur := Compteur - 1;
         end loop;
         if Compteur > 1 then
            return T(Nom_Fichier)(T(Nom_Fichier)'First..Compteur);
         else
            return "./";
         end if;
      exception
         when others => 
            Put_Line("Une erreur est survenue dans la lecture du chemin du fichier .net.");
            Put_Line("Les fichiers de sortis seront alors crees dans le dossier où se trouve pagerank.");
            return "./";
      end;
   end Chemin;

   function Nom (Nom_Fichier : in Unbounded_String) return String is
      Debut : Integer;
      Fin : Integer;
   begin
      begin
         Debut := T(Nom_Fichier)'Length;
         Fin := T(Nom_Fichier)'Length;
         while Debut > 0 and then (T(Nom_Fichier)(Debut) /= '/' and T(Nom_Fichier)(Debut) /= '\') loop
            Debut := Debut - 1;
         end loop;
         
         while Fin > 0 and then T(Nom_Fichier)(Fin) /= '.' loop
            Fin := Fin - 1;
         end loop;
         Fin := Fin - 1;
         if Debut < Fin and Debut >= 1 then
            return T(Nom_Fichier)(Debut..Fin);
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

   procedure Lire_Args
     (Nom_Fichier :    out Unbounded_String; A : out T_Double;
      Max_Iter    :    out Integer; P : out Boolean; Aide : out Boolean)
   is    
      Compteur : Integer;
      Net_File : Ada.Text_IO.File_Type;
   begin
      begin
         --  Initialisation des valeurs par defaut
         P        := False;
         Max_Iter := 150;
         A        := 0.85;
         Compteur := 1;
         Aide     := False;

         if Argument_Count < 1 then
            raise Erreur_Argument_Manquant;

         else
            -- Boucle sur les arguments
            while Compteur <= Argument_Count loop
               --  TODO: Faire un case avec plusieurs lignes dans le when
               if Argument (Compteur) = "-P" or Argument (Compteur) = "-p" then
                  P        := True;
                  Compteur := Compteur + 1;

               elsif  Argument(Compteur) = "-I" or Argument(Compteur) = "-i"
               then
                  Compteur := Compteur + 1;

                  if -Argument(Compteur) > 0 then
                     Max_Iter := -Argument (Compteur);
                     Compteur := Compteur + 1;

                  else
                     raise Erreur_Mauvais_Parametre_Iteration;
                  end if;

               elsif Argument (Compteur) = "-A" or Argument (Compteur) = "-a"
               then
                  Compteur := Compteur + 1;

                  if -Argument (Compteur) > 0 then
                     A := T_Double'Value(Argument (Compteur));
                     Compteur := Compteur + 1;
                  else
                     raise Erreur_Mauvais_Parametre_Iteration;
                  end if;

               elsif Argument (Compteur) = "-H" or Argument (Compteur) = "-h"
               then
                  Aide := True;
                  Compteur := Compteur + 1;
               elsif Est_Nom_Fichier(Argument(Compteur)) then
                  Nom_Fichier := +Argument (Compteur);
                  Compteur := Compteur + 1;
               end if;
            end loop;

            if Aide then
               Afficher_Aide;
            elsif To_String(Nom_Fichier)'Length < 3 then
               raise ERREUR_Mauvais_Parametre_Fichier;
            end if;

         end if;
         
         -- test d'erreur de la part de la routine open
         begin
            open(Net_File, In_File, To_String(Nom_Fichier));
            close(Net_File);
         exception
            when others => -- techniquement la seule exception attendue est ADA.IO_EXCEPTIONS.NAME_ERROR
               raise ERREUR_Fichier_Manquant;
         end;

      exception
         when Erreur_Argument_Manquant =>
            Put_Line
              ("Veuillez renseigner le nom du fichier .net. Pour plus d'aide sur les arguments, tapez './pagerank -h'.");
            raise Erreur_Lire_Args;

         when Erreur_Mauvais_Parametre_Iteration =>
            Put_Line
              ("Mauvais parametre d'iteration. Pour plus d'aide sur les arguments, tapez './pagerank -h'.");
            raise Erreur_Lire_Args;

         when Erreur_Mauvais_Parametre_Alpha =>
            Put_Line
              ("Mauvais parametre alpha. Pour plus d'aide sur les arguments, tapez './pagerank -h'.");
            raise Erreur_Lire_Args;

         when ERREUR_Mauvais_Parametre_Fichier =>
            Put_Line
              ("Fichier .net manquant, veuillez indiquez un le nom du fichier (extension comprise). Pour plus d'aide sur les arguments, tapez './pagerank -h'.");
            raise Erreur_Lire_Args;

         when ERREUR_Fichier_Manquant =>
            Put_Line
              ("Fichier .net introuvable ou illisible. Verifiez le chemin d'acces");
            raise Erreur_Lire_Args;

         when others =>
            Put_Line
              ("Un probleme a ete rencontre lors du traitrement des arguments, l'operation n'a pas abouti");
            Put_Line
              ("Pour plus d'aide sur les arguments, tapez './pagerank -h'.");
            raise Erreur_Lire_Args;
      end;
   end Lire_Args;

   ------------------------
   --  Estimer_Donnees   --
   ------------------------
   procedure Estimer_Donnees (Taille : in Integer; Max_Iter : in Integer) is
      Iter_Taille : Float;
   begin
      Iter_Taille := (17.0*Float(Taille)*(Float(Taille) + 1.0)*Float(Taille))/2.0; -- un fichier temp utilise 17 octets par flottant enregistre
      Put_line("Attention, le calcul demandé requiert un flux de données total de " 
               & Float'Image(Float(Max_Iter)*Iter_Taille) 
               & "octets.");
      Put_line("La durée de l'opération sera déterminée par la vitesse maximale de lecture de votre disque.");
   end Estimer_Donnees;


end Helpers;
