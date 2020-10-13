with Ada.Text_IO;          use Ada.Text_IO;
with Ada.Integer_Text_IO;  use Ada.Integer_Text_IO;

procedure Lire_Entier is

	-- Lire un entier au clavier.
	-- Param�tres :
	--    Nombre : l'entier � lire
	-- N�cessite : ---
	-- Assure : -- Nombre est l'entier lu
	procedure Lire (Nombre: out Integer) is
	    Item: Character;
	    End_Of_Line: Boolean;
	    nb: Character;
   begin
      Nombre:= 0;
		loop
         Look_Ahead(Item, End_Of_Line);
         if (not End_Of_Line) then
            Get(nb);
            Nombre := (Nombre * 10) + (Character'Pos(nb) - 48);
         end if;
		exit when End_Of_Line;
		end loop;
	end Lire;

	Un_Entier: Integer;	    -- lu au clavier
	Suivant: Character;     -- lu au clavier
begin
	-- Demander un entier
	Put ("Un entier : ");

	Lire(Un_Entier);

	-- Afficher l'entier lu
	Put ("L'entier lu est : ");
	Put (Un_Entier, 1);
	New_Line;

	-- Afficher le caract�re suivant
	Get (Suivant);
	Put ("Le caract�re suivant est : ");
	Put (Suivant);
	New_Line;

end Lire_Entier;
