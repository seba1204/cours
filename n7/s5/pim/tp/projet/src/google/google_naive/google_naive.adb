package body Google_Naive is


   procedure Init (N : in Unbounded_String; A : in T_Float; M : in Integer; T : in Ineger) is
   begin
      Nom_Fichier_Net := N;
      A               := A;
      Max_Iter        := M;
      Taille          := T;
   end Init;

   --------------------
   -- Calculer_Coefs --
   --------------------
   procedure Calculer_Coefs is
      type T_Tampon is array (1 .. Capacite_Max) of Integer;
      I, J : Integer;
      Tampon        : T_Tampon;
      Taille_Bis    : Integer;
      Fichier_Net   : Ada.Text_IO.File_Type;
      Referenceur   : Integer := 0;
      Destinataire  : Integer := 0;
      Ligne_Nulle   : Boolean;
      Fichier_Temp  : Ada.Text_IO.File_Type;
      Dernier_Index : Integer := 1;
      Ajout_G       : Float;
   begin
      Open (Fichier_Net, In_File, To_String (Nom_Fichier));

      Get (Fichier_Net, Taille_Bis);

      if Taille_Bis /= Taille then
         Close (Fichier_Net);
         raise ERREUR_Lecture_Taille
           with "La taille du fichier " & To_String (Nom_Fichier) &
           "a change pendant les calculs (Taille initiale : " & Integer'Image (Taille) &
           ", Taille actuelle : " & Integer'Image (Taille) & ").";
      end if;

      if Taille < Capacite_Max then
         -- reseau de petite taille : on charge G en mémoire RAM
         -- -----1. 
         -- on lit le fichier ligne par ligne en rajoutant au fur et à mesure dans G les coef
         -- et on enregistre dans tampon la quantité de liens par ligne

         -- initialisaion à 0
         for I in 1..Taille loop
            Tamon(I) := 0;
            for J in 1..Taille loop
               G(I,J) := T_Float(0);
            end loop; 
         end loop;

         -- lecture du fichier .net
         while not End_Of_File (Fichier_Net) loop
            Get (Fichier_Net, Referenceur);
            Get (Fichier_Net, Destinataire);
            Tampon (Referenceur + 1) := Tampon (Referenceur + 1) + 1;
            G(Referenceur + 1, Destinataire + 1) := T_Float(1);
         end loop;

         -- -----2. 
         -- On boule sur tampon et on enregistre dans G le bon coef

         declare
            Un : T_Float := T_Float(1);
            B : T_Float := Un / T_Float(Taille);
         begin            
            for I in 1..Taille loop
               for J in 1..Taille loop
                  if Tampon(I) = 0 then
                     G(I,J) := B;
                  else 
                     G(I,J) := A * Un / T_Float(Tampon(I)) + (Un - A) * B;
                  end if;
               end loop; 
            end loop;
         end;

      elsif Taille < Capacite_Max * Capacite_Max then
         -- reseau de moyenne taille : on charge les colonnes de G en mémoire RAM

      else 
         -- reseau de taille énorme : jsp quoi faire...
         
      end if;

      -- initialisation de Tampon
      for i in 1 .. Taille loop
         Tampon (i) := +"";
      end loop;

      -- lecture du fichier .net
      while not End_Of_File (Fichier_Net) loop
         Get (Fichier_Net, Referenceur);
         Get (Fichier_Net, Destinataire);
         if Tampon (Referenceur + 1) = +"" then
            Tampon (Referenceur + 1) := +Integer'Image (Destinataire + 1);
         else
            Tampon (Referenceur + 1) :=
              To_Unbounded_String
                (To_String (Tampon (Referenceur + 1)) & ";" &
                 Integer'Image (Destinataire + 1));
         end if;
      end loop;

      -- copie de tampon dans Fichier_Temp
      Create
        (Fichier_Temp, Out_File,
         Chemin (Nom_Fichier) & Nom (Nom_Fichier) & ".temp");

      Ajout_G := (1.0 - Float (A)) / Float (Taille);
      for i in 1 .. Taille loop
         declare
            Taille_Ligne : Integer;
            Index        : Integer := 1;
            Compteur     : Integer := 1;
            Ligne        : String (1 .. To_String (Tampon (i))'Last);
         begin
            Ligne := To_String (Tampon (i));

            -- Parser la ligne Tampon
            if Ligne /= "" then
               Index    := 0;
               Compteur := 1;

               -- Le nombre d'éléments dans la ligne
               Taille_Ligne := Compter (+Ligne, ';') + 1;

               -- TODO: TRIER la ligne dans l'ordre croissant

               for k in 1 .. Taille_Ligne loop
                  -- Lecture de l'index
                  Dernier_Index := Index;
                  Index         := 0;
                  while Compteur <= Ligne'Last and then Ligne (Compteur) /= ';'
                  loop
                     if Ligne (Compteur) /= ' ' then
                        Index :=
                          Index * 10 + Integer'Value ((1 => Ligne (Compteur)));
                     end if;
                     Compteur := Compteur + 1;
                  end loop;
                  Compteur := Compteur + 1;

                  -- Creation ou completion de la ligne
                  for j in Dernier_Index + 1 .. Index - 1 loop
                     if j /= 1 then
                        Put (Fichier_Temp, " ");
                     end if;
                     Put (Fichier_Temp, Ajout_G, Fore => 1, Aft => 10);
                  end loop;

                  -- Ajout d'espace, sauf si début de ligne
                  if Index /= 1 then
                     Put (Fichier_Temp, " ");
                  end if;

                  -- Ajout de la valeur calculee de G
                  Put
                    (Fichier_Temp, Float (A) / Float (Taille_Ligne) + Ajout_G,
                     Fore => 1, Aft => 10);
                  -- TODO: Gerer le T_Float
               end loop;

               -- Completion de la ligne par des zeros
               for j in Index + 1 .. Taille loop
                  if j /= 1 then
                     Put (Fichier_Temp, " ");
                  end if;
                  Put (Fichier_Temp, Ajout_G, Fore => 1, Aft => 10);
               end loop;

            else
               for i in 1 .. Taille loop
                  if i > 1 then
                     Put (Fichier_Temp, " ");
                  end if;
                  Put
                    (Fichier_Temp, 1.0 / Float (Taille), Fore => 1, Aft => 10);
               end loop;
            end if;
            Put_Line (Fichier_Temp, "");
         end;
      end loop;

      Close (Fichier_Net);
      Close (Fichier_Temp);
   end Calculer_Coefs;

   -----------------------
   -- Initialiser_Poids --
   -----------------------

   procedure Initialiser_Poids is
   begin
      for i in 1 .. Taille loop
         Pi (i).Index := i - 1;
         Pi (i).Poids := 1.0 / T_Float (Taille);
      end loop;
   end Initialiser_Poids;

   --------------------
   -- Calculer_Poids --
   --------------------

   procedure Calculer_Poids is
      type T_Colonne is array (1 .. Taille) of T_Float;
      Somme            : T_Float;
      Colonne          : T_Colonne;
      Fichier_Temp     : Ada.Text_IO.File_Type;
      Temp             : Float;
      Nom_Fichier_Temp : Unbounded_String;
      Nouveau_Pi       : T_Poids;
   begin
      Nom_Fichier_Temp :=
        To_Unbounded_String
          (Chemin (Nom_Fichier) & Nom (Nom_Fichier) & ".temp");

      for k in 1 .. Max_Iter loop

         for i in 1 .. Taille loop
            -- charger la colonne i du fichier .temp en mémoire
            -- déterminer le dernier indice non nul
            Open (Fichier_Temp, In_File, To_String (Nom_Fichier_Temp));
            for j in 1 .. Taille loop
               for l in 1 .. i - 1 loop
                  Get (Fichier_Temp, Temp);
               end loop;
               Get (Fichier_Temp, Temp);
               Colonne (j) := T_Float (Temp);
               if j < Taille then
                  Set_Line (Fichier_Temp, To => Ada.Text_IO.Count (j + 1));
               end if;
            end loop;
            Close (Fichier_Temp);

            Somme := 0.0;
            for j in 1 .. Taille loop
               -- Calcul matriciel
               Somme := Somme + Pi (j).Poids * Colonne (j);
            end loop;
            Nouveau_Pi (i).Poids := Somme;
            Somme                := 0.0;
         end loop;
         for i in 1 .. Taille loop
            Pi (i).Poids := Nouveau_Pi (i).Poids;
         end loop;
      end loop;
   end Calculer_Poids;

   -----------------
   -- Trier_Poids --
   -----------------

   procedure Trier_Poids is
      Courant_Poids : T_Float;
      Courant_Index : Integer;
      j             : Integer;
   begin
      -- on realise un tri par insertion
      for i in 1 .. Taille loop -- copier Pi dans Pi_Trie
         Pi_Trie (i).Poids := Pi (i).Poids;
         Pi_Trie (i).Index :=
           Pi (i)
             .Index; -- on peut tester une affectation directe Pi_Trie := Pi mais je crains que les adresses des elements soient les memes
      end loop;

      for i in 1 .. Taille loop
         Courant_Poids := Pi_Trie (i).Poids;
         Courant_Index := Pi_Trie (i).Index;
         j             := i;

         while j > 1 and then Pi_Trie (j - 1).Poids < Courant_Poids loop
            Pi_Trie (j) := Pi_Trie (j - 1);
            j           := j - 1;
         end loop;

         Pi_Trie (j).Poids := Courant_Poids;
         Pi_Trie (j).Index := Courant_Index;
      end loop;

   end Trier_Poids;

   --------------------
   -- Creer_Fichiers --
   --------------------

   procedure Creer_Fichiers is
      Fichier_Ord : Ada.Text_IO.File_Type;
      Fichier_P   : Ada.Text_IO.File_Type;
      F           : Unbounded_String;
   begin
      F := Nom_Fichier; -- Pour raccourcir les lignes suivantes
      Create (Fichier_Ord, Out_File, Chemin (F) & Nom (F) & ".ord");
      Create (Fichier_P, Out_File, Chemin (F) & Nom (F) & ".p");

      -- Ecriture de l'entete du fichiers de poids
      Put (Fichier_P, Taille, 0);
      Put (Fichier_P, " ");
      Put (Fichier_P, Float (A), Fore => 1, Aft => 10);
      Put (Fichier_P, " ");
      Put (Fichier_P, Max_Iter, 0);
      New_Line (Fichier_P);

      for i in 1 .. Taille loop
         -- Ecriture des indices de poids ordonnés
         Put (Fichier_Ord, Pi_Trie (i).Index, 1);
         New_Line (Fichier_Ord);

         -- Ecriture des poids dans l'ordre des indices croissants
         Put (Fichier_P, Float (Pi (i).Poids), Fore => 1, Aft => 10);
         New_Line (Fichier_P);
      end loop;

      Close (Fichier_Ord);
      Close (Fichier_P);

   end Creer_Fichiers;

end Google_Naive;
