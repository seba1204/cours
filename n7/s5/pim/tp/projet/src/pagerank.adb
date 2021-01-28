with Ada.Exceptions; use Ada.Exceptions;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Helpers; use Helpers;
with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Float_Text_IO;     use Ada.Float_Text_IO;
with Ada.Integer_Text_IO;   use Ada.Integer_Text_IO;
with Ada.Directories;  use Ada.Directories; -- pour lire la taille d'un fichier
with Ada.Real_Time; use  Ada.Real_Time; -- pour le temps d'exécution
with P_Google;

function Pagerank return Integer is
   ---------------- CONSTANTES ----------------
   Nb_Digit     : constant Integer := 3;
   --------------------------------------------
   
   type Reel is digits Nb_Digit;

   package Matrice_Google is new P_Google (Reel);
   use Matrice_Google;

   type Table is array(Positive range <>) of Reel;
   type R_Poids is record 
      Poids : Reel := Reel(0);
      Index : Integer := 0;
   end record;
   type Poids is array(Positive range <>) of R_Poids;
   -- Variables :

   A : Args; -- Arguments golbaux
   C : Integer := 0; -- Compteur d'octets lus
   Taille_Fichier : Integer; -- Taille en octets
   Fichier_1, Fichier_2 : Ada.Text_IO.File_Type;
   Referenceur, Destinataire : Integer;

   -- Calcul poids
   sum : Reel;

   -- Temps
   duree : Duration;
begin

   -- Lecture des arguments
   A := Lire_Arugments;

   -- Si on a affiche l'aide, on ne fait rien d'autre
   if A.Aide_Demande then
      return 0;
   end if;

   -- C'est ici que tout se passe
   declare
      F : constant String := To_String(A.Nom_Fichier);
      Taille : constant Integer := A.Taille_Reseau;
      G : Google'Class := Initialiser(A);
      P : Poids(1..Taille);
      T : Table(1..Taille);
      Poids_Tampon : R_Poids;
      Zero : constant Reel := Reel(0);
      Un : constant Reel := Reel(1);
      temps : Time;
   begin

      Log("Mode " & G.Mode);

      Log("Initalisation des coefficients de G...");
      G.Initialiser;

      Log("Initalisation des poids...");
      for I in 1..Taille loop
         P(I).Poids      := Un / Reel(Taille);
         P(I).Index      := I - 1;
      end loop;

      Log("Lecture du fichier reseau...");
      begin
         Open(Fichier_1, In_File, F);
         Get(Fichier_1, Referenceur);
         C := C + Octets(Referenceur);
         Taille_Fichier := Integer (Size (F));
         while not End_Of_File (Fichier_1) loop
            Get (Fichier_1, Referenceur);
            Get (Fichier_1, Destinataire);
            C := C + Octets(Referenceur) + Octets(Destinataire) + 2;
            G.Inserer(Referenceur, Destinataire, Un);
            G.Tamponner(Referenceur + 1);
            Log_P(C, Taille_Fichier);
         end loop;
      exception
         when others => null;         
      end;
      Close (Fichier_1);

      
      Log("Calcul des coefficients de G...");
      G.Calculer_Coef;

      Log("Calcul poids: " & Integer'Image(A.Max_Iter) & " iterations");
      temps := Clock;
      for K in 1..A.Max_Iter loop
         Log_P(K, A.Max_Iter);

         for I in 1..Taille loop
            sum := Zero;
            for J in 1.. Taille loop
               sum := sum + P(J).Poids * G.Multiplicateur_De_Poids(J, I);
            end loop;
            T(I) := sum;
         end loop;

         -- Copie du tampon
         for I in 1..Taille loop
            P(I).Poids := T(I);
         end loop;
      end loop;
      duree := To_Duration(Clock - temps);
      Log("Tri des poids par insertion...");
      for I in 1 .. Taille loop
         Log_P(I, Taille);
         Poids_Tampon := P(I);
         C             := I;

         while C > 1 and then P(C - 1).Poids < Poids_Tampon.Poids loop
            P(C) := P(C - 1);
            C    := C - 1;
         end loop;
         P (C) := Poids_Tampon;
      end loop;
      
      Log("Export des fichiers...");
      Create (Fichier_1, Out_File, Chemin (F) & Nom (F) & ".ord");
      Create (Fichier_2, Out_File, Chemin (F) & Nom (F) & ".p");

      -- Ecriture de l'entete du fichiers de poids
      Put (Fichier_2, Taille, 0);
      Put (Fichier_2, " ");
      Put (Fichier_2, A.A, Fore => 1, Aft => 10);
      Put (Fichier_2, " ");
      Put (Fichier_2, A.Max_Iter, 0);
      New_Line (Fichier_2);

      for I in 1 .. Taille loop
         Log_P(I, Taille);
         -- Ecriture des indices de poids ordonnés
         Put (Fichier_1, P(I).Index, 1);
         New_Line (Fichier_1);

         -- Ecriture des poids dans l'ordre des indices croissants
         Put (Fichier_2, Float (P(I).Poids), Fore => 1, Aft => 10);
         New_Line (Fichier_2);
      end loop;

      Close (Fichier_1);
      Close (Fichier_2);

      Log_Matlab(Integer(duree * 1000));
   end;
   Log("Temps d'execution :" & Humaniser(Duree));
   -- Fin
   return 0;

   exception
      when E : others =>
         Ada.Text_IO.Put_Line (Exception_Message (E));
         return 1;
end Pagerank;
