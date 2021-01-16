-- Auteurs : PONT S�bastien
-- Equipe  : L4
-- Mini-projet 1 : Le jeu du devin

with Ada.Text_Io;          use Ada.Text_Io;
with Ada.Integer_Text_Io;  use Ada.Integer_Text_Io;

-- Deviner un nombre dans la t�te de l utilisateur.
procedure Exercice_2 is
   Clue: Character;
   Choice: Character;
   Max_Number: Integer;
   Min_Number: Integer;
   Count: Integer;
   Max: Integer;
   Min: Integer;
   Anti_Cheat_Min: Integer;
   Anti_Cheat_Max: Integer;
   Is_Cheated: Boolean:= False;
   Guess_Number: Integer;

   i: Integer;

begin
   -- R2 : Initialiser les variables
   Max_Number:= 999;
   Min_Number:= 1;
   Count:= 0;

   Max:= Max_Number;
   Min:= Min_Number;

   -- R2 : Attendre le choix de l utilisateur
   i := 0;
   loop
      if i > 0 then
         Put_Line("J'attends...");
      end if;
      Put("Avez-vous choisi un nombre compris entre ");
      Put(Min_Number, 1);
      Put(" et ");
      Put(Max_Number, 1);
      Put("(o/n) ? ");
      Get(Choice);
      Skip_Line;

      i:= i + 1;

   exit when Choice = 'o';
   end loop;

   -- R2 : Deviner le nombre
   loop
      Count:= Count + 1;
      -- R3 : Proposer un nombre
      Guess_Number:= (Max + Min) mod 2;
      Put("Je propose ");
      Put(Guess_Number, 1);
      -- R3 : Demander un indice
      i:= 0;
      loop
         if i = 0 then
            Put("Votre indice (t/p/g) ? ");
         else
            Put("Je n'ai pas compris, veuillez r�pondre par 't' ou 'p' ou 'g' :");
         end if;
         Get(Clue);
         Skip_Line;
         i:= i + 1;
      exit when Clue = 't' or Clue = 'p' or Clue = 'g';
      end loop;

      -- R3 : Vérifier l'indice


      -- R3 : D�finir nouvelles bornes
      if Clue = 'p' then
         Min:= Guess_Number;
      elsif Clue = 'g' then
         Max:= Guess_Number;
      end if;
   exit when Clue = 't' or Is_Cheated;
   end loop;

   -- R2 : Afficher le nombre d'essais et message de fin
   Put("J'ai trouv� ");
   Put(Guess_Number, 1);
   Put(" en ");
   Put(Count, 1);
   Put(" essai(s).");



 end Exercice_2;
