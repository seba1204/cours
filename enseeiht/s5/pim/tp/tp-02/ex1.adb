-- Auteurs : PONT Sébastien
-- Equipe  : L4
-- Mini-projet 1 : Le jeu du devin

with Ada.Text_Io;          use Ada.Text_Io;
with Ada.Integer_Text_Io;  use Ada.Integer_Text_Io;

	-- R0 : Faire deviner un nombre à l utilisateur.
	procedure Devin_Game is
		Secret_Number : Integer; -- Nombre secret à deviner
		User_Number : Integer; -- Nombre proposé par l utilisateur
		Count : Integer:= 0; -- Nombre d'essais de l utilisateur
		Is_Number_Valid : Boolean := False; -- True quand 1 < Secret_Number < 9
		Is_Number_Right  : Boolean := False; -- True quand l utilisateur a deviné le nombre
	begin
   -- R1 : Faire deviner un nombre à l utilisateur


		-- R2 : Demander le nombre
   loop
           Put("J'ai choisi ");
		    Get(Secret_Number);
		    -- R3 : Vérifier le nombre
		    if 1 <= Secret_Number and Secret_Number <= 999 then
		        Is_Number_Valid:= True;
		    else
		        Put_Line("Le nombre à deviner doit être compris entre 1 et 999.");
		    end if;
		exit when Is_Number_Valid;
		end loop;

		-- R2 : Faire deviner le nombre
		loop
		    Put("Proposez un nombre : ");
           Get(User_Number);
           Count := Count + 1;
		    -- R3 : Jauger le nombre proposé
		    if User_Number > Secret_Number then
		        Put_Line("Le nombre proposé est trop grand.");
		    elsif User_Number < Secret_Number then
		        Put_Line("Le nombre proposé est trop petit.");
		    else
               Is_Number_Right:= True;
           end if;
		exit when Is_Number_Right;
		end loop;

		-- R2 : Afficher le message de fin
		Put_Line("Trouvé !");
        Put("Bravo !  Vous avez trouvé en ");
        Put (Count, 1);
        Put(" essai(s).");

	end Devin_Game;
