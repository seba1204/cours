-- Auteurs : Philippe Négrel-Jerzy
-- Equipe  : K-2 Nicolas / Négrel-Jerzy
-- Mini-projet 1 : Le jeu du devin

with Ada.Text_Io;          use Ada.Text_Io;
with Ada.Integer_Text_Io;  use Ada.Integer_Text_Io;

-- TODO: à compléter...
procedure Jeu_Devin is

   Min : constant Integer := 1;
   Max : constant Integer := 999;
   -- les nombres à trouver sont entre Min et Max

   -- l'ordinateur choisit un nombre et le fait deviner à l'utilisateur
   procedure Utilisateur_Devine_Nombre is
      jeu_continue : Boolean;
      nombre_essai : Integer;
      n : Integer;
      n_propose : Integer;

   begin
      jeu_continue := true;
      nombre_essai := 0;
      -- R2 : Faire choisir le nombre
      loop
         put("J'ai choisi ");get(n);
         --New_Line;
         exit when n>Min and n<Max;
      end loop;
      -- R2 : Jouer au jeu

      while jeu_continue loop
         put("Proposez un nombre : ");get(n_propose);
         --New_Line;
         -- R3 : Vérifier le nombre proposé
         if n_propose = n then
            put_line("Trouvé !");
            New_Line;
            jeu_continue := false;
         elsif n_propose > n then
            put_line("Le nombre proposé est trop grand.");
         else
            put_line("Le nombre proposé est trop petit.");
         end if;
         nombre_essai := nombre_essai + 1;
      end loop;

      -- R2 : l'ordinateur affiche le nombre d'essai

      put("Bravo !  Vous avez trouvé en ");put(nombre_essai,0);put(" essai(s).");
      New_Line;


   end Utilisateur_Devine_Nombre;



   -- Deviner le nombre choisi par l'utilisateur
   procedure Ordi_Devine_Nombre is
      reponse : character := 'n'; -- user answer to first question
      MIN_LOC : integer := Min;
      MAX_LOC : integer := Max;
      test : integer := 500;
      arret : boolean := False;
      essais : integer := 0;
      indice : character := ' ';

   begin
      -- Initialiser le jeu
      While reponse /= 'o' loop
         -- Variant : reponse

         Put("Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ? ");
         Get(reponse);
         If reponse /= 'o' then
            Put_Line("J'attends...");
         end if;
      end loop;

      -- Jouer avec l'utilisateur
      While not arret loop
         -- Variant : arret

         -- Tester
         essais := essais+1;

         Put("Je propose ");
         Put(test, 0);
         New_Line;
         Put("Votre indice (t/p/g) ? ");
         Get(indice);

         Case indice is
         when 'g' =>
            if abs(MAX_LOC - MIN_LOC) > 3 then
               -- Reduire le nombre teste
               MAX_LOC := Integer'((MAX_LOC + MIN_LOC)/2);
               test := Integer'((MAX_LOC + MIN_LOC)/2);
            else
               arret := True;
               Put_Line("Vous trichez. J'arrête cette partie.");
            end if;
         when 'p' =>
            if abs(MAX_LOC - MIN_LOC) > 3 then
               -- Augmenter le nombre teste
               MIN_LOC := Integer'((MAX_LOC + MIN_LOC)/2);
               test := Integer'((MAX_LOC + MIN_LOC)/2);
            else
               arret := True;
               Put_Line("Vous trichez. J'arrête cette partie.");
            end if;
         when 't' =>
            arret := True;

            -- Ecrire message fin
            Put("J'ai trouvé ");
            Put(test ,0);
            Put(" en ");
            Put(essais, 0);
            Put(" essai(s).");
            New_Line;
         when others =>
            null;
         end Case;
      end loop;
      New_Line;

   end Ordi_Devine_Nombre;


   choix : Integer := 400; -- un chiffre qui n'est pas une possibilité
begin
   loop
      --Afficher les choix disponibles
      Put_Line("1- L'ordinateur choisit un nombre et vous le devinez");
      Put_Line("2- Vous choisissez un nombre et l'ordinateur le devine");
      Put_Line("0- Quitter");

      --Demander son choix à l'utilisateur
      Put("Votre choix : ");
      Get(choix);
      New_Line;

      exit when choix = 0;

      -- Exécuter l'algorithme correspondant
      case choix is
         when 1 =>
            Utilisateur_Devine_Nombre;
         when 2 =>
            Ordi_Devine_Nombre;
         when others =>
            null;
      end case;

   end loop;
end Jeu_Devin;
