-- Auteurs : PONT S�bastien
-- Equipe  : L4
-- Mini-projet 1 : Le jeu du devin

with Ada.Text_Io;          use Ada.Text_Io;
with Ada.Integer_Text_Io;  use Ada.Integer_Text_Io;

-- Jouer aux jeux devin avec l'utilisateur
procedure Jeu_Devin is

	Mini : constant Integer := 1;
	Maxi : constant Integer := 999;

	-- Faire deviner un nombre à l utilisateur.
	procedure User_Guess is	-- TODO: Donner un nom significatif !
        Secret_Number : Integer; -- Nombre secret � deviner
		User_Number : Integer; -- Nombre propos� par l utilisateur
		Count : Integer:= 0; -- Nombre d'essais de l utilisateur
		Is_Number_Valid : Boolean := False; -- True quand 1 < Secret_Number < 9
		Is_Number_Right  : Boolean := False; -- True quand l utilisateur a devin� le nombre
	begin
        -- R1 : Faire deviner un nombre � l utilisateur
		-- R2 : Demander le nombre
        loop
            Put("J'ai choisi ");
		    Get(Secret_Number);
		    -- R3 : V�rifier le nombre
		    if 1 <= Secret_Number and Secret_Number <= 999 then
		        Is_Number_Valid:= True;
		    else
		        Put_Line("Le nombre � deviner doit �tre compris entre 1 et 999.");
		    end if;
		exit when Is_Number_Valid;
		end loop;

		-- R2 : Faire deviner le nombre
		loop
            Put("Proposez un nombre : ");
            Get(User_Number);
            Count := Count + 1;
		    -- R3 : Jauger le nombre propos�
		    if User_Number > Secret_Number then
		        Put_Line("Le nombre propos� est trop grand.");
		    elsif User_Number < Secret_Number then
		        Put_Line("Le nombre propos� est trop petit.");
		    else
               Is_Number_Right:= True;
           end if;
		exit when Is_Number_Right;
		end loop;

		-- R2 : Afficher le message de fin
		Put_Line("Trouv� !");
        Put("Bravo !  Vous avez trouv� en ");
        Put (Count, 1);
        Put(" essai(s).");
	end User_Guess;



	-- Deviner un nombre dans la t�te de l utilisateur.
	procedure Computer_Guess is
        Clue: Character;
        Choice: Character;
        Max_Number: Integer;
        Min_Number: Integer;
        Counti: Integer;
        Maxi: Integer;
        Mini: Integer;
        Is_Cheated: Boolean:= False;
        Guess_Number: Integer;

        i: Integer;
	begin
        -- R2 : Initialiser les variables
        Max_Number:= 999;
        Min_Number:= 1;
        Counti:= 0;

        Maxi:= Max_Number;
        Mini:= Min_Number;

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
            Put(" (o/n) ? ");
            Get(Choice);
            Skip_Line;

            i:= i + 1;

        exit when Choice = 'o';
        end loop;

        -- R2 : Deviner le nombre
        loop
            Counti:= Counti + 1;
            -- R3 : Proposer un nombre
            Guess_Number:= Integer(Float'Unbiased_Rounding(Float(Maxi + Mini) / 2.0));
            Put("Je propose ");
            Put(Guess_Number, 1);
            Put_Line("");
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

            -- R3 : V�rifier l'indice
            if abs(Mini - Guess_Number) < 3 or abs(Maxi - Guess_Number) < 3 then
                Is_Cheated:= True;
            end if;

            -- R3 : D�finir nouvelles bornes
            if Clue = 'p' then
                Mini:= Guess_Number;
            elsif Clue = 'g' then
                Maxi:= Guess_Number;
            end if;
        exit when Clue = 't' or Is_Cheated;
        end loop;

        -- R2 : Afficher le nombre d'essais et message de fin
        if Is_Cheated then
            Put("Vous trichez.");
            Put("J'arr�te cette partie.");
        else
            Put("J'ai trouv� ");
            Put(Guess_Number, 1);
            Put(" en ");
            Put(Counti, 1);
            Put(" essai(s).");
        end if;
	end Computer_Guess;


	Main_Choice: Integer;
begin
	 loop
      --Afficher les choix
      Put_Line("1- L'ordinateur choisit un nombre et vous le devinez");
      Put_Line("2- Vous choisissez un nombre et l'ordinateur le devine");
      Put_Line("0- Quitter");

      --Demander son choix
      Put("Votre choix : ");
      Get(Main_Choice);
      New_Line;


      -- Traiter le choix
      case Main_Choice is
         when 1 => User_Guess;
         when 2 => Computer_Guess;
         when others =>
            null;
      end case;

   exit when Main_Choice = 0;
   end loop;
end Jeu_Devin;
