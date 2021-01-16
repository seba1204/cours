
-- Auteurs : PONT Sébastien
-- Equipe  : L4
-- Mini-projet 1 : Le jeu du devin

with Ada.Text_Io;          use Ada.Text_Io;
with Ada.Integer_Text_Io;  use Ada.Integer_Text_Io;


-- Jouer aux jeux devin avec l'utilisateur
procedure Jeu_Devin is

	Mini : Integer;
	Maxi : Integer;

	procedure Utilisateur_Devine is
		Secret_Number:      Integer;          -- Nombre secret à deviner
		Nombre_Utilisateur: Integer;          -- Nombre proposé par l utilisateur
		Compteur:           Integer:= 0;      -- Nombre d'essais de l utilisateur
		Nombre_Valide:      Boolean:= False;  -- True quand 1 < Secret_Number < 999
		Nombre_Juste:       Boolean:= False;  -- True quand l'utilisateur a deviné le nombre
	begin
		-- R1 : Faire deviner un nombre à l utilisateur ---------------------------------------

		-- R2 : Demander le nombre ------------------------------------------------------------

		loop
			Put("J'ai choisi ");
			Get(Secret_Number);

			-- R3 : Vérifier le nombre ---------------------------------------------------
			if Mini <= Secret_Number and Secret_Number <= Maxi then
				Nombre_Valide:= True;
			else
				Put("Le nombre à deviner doit être compris entre ");
				Put(Mini, 1);
				Put(" et ");
				Put(Maxi, 1);
				Put(".");
				New_Line;
			end if;
		exit when Nombre_Valide;
		end loop;

		-- R2 : Faire deviner le nombre ----------------------------------------------------
		loop
			Put("Proposez un nombre : ");
			Get(Nombre_Utilisateur);
			Compteur:= Compteur + 1;

			-- R3 : Jauger le nombre proposé ---------------------------------------------
			if Nombre_Utilisateur > Secret_Number then
				Put_Line("Le nombre proposé est trop grand.");
			elsif Nombre_Utilisateur < Secret_Number then
				Put_Line("Le nombre proposé est trop petit.");
			else
				Nombre_Juste:= True;
			end if;
		exit when Nombre_Juste;
		end loop;

		-- R2 : Afficher le message de fin --------------------------------------------
		Put_Line("Trouvé !");
		Put("Bravo !  Vous avez trouvé en ");
		Put (Compteur, 1);
		Put(" essai(s).");

	end Utilisateur_Devine;

	procedure Ordinateur_Devine is
		Indice:         Character;    -- Indice de l'utilisateur
		Choice:         Character;    -- choix utilisateur oui / non
		Compteur:       Integer;      -- Compteur de nombre de coups
		Triche:         Boolean;      -- True si l'utilisateur triche
		Nombre_Devine:  Integer;      -- Nombre proposé par ordinateur
		Juste:          Boolean;      -- False au deuxième tour de boucle

	begin
		-- R1 : Faire deviner un nombre à l'ordinateur -------------------------------------
		-- R2 : Initialiser les variables --------------------------------------------------
		Compteur:= 0;
		Triche:= False;
		Juste:= True;
		Indice:= ' ';

		-- R2 : Attendre le choix de l utilisateur -----------------------------------------
		loop
			if not Juste then
				Put_Line("J'attends...");
			end if;

			Put("Avez-vous choisi un nombre compris entre ");
			Put(Mini, 1);
			Put(" et ");
			Put(Maxi, 1);
			Put(" (o/n) ? ");
			Get(Choice);
			Skip_Line;

			Juste:=False;        -- Pour afficher "J'attends..." au prochain tour

		exit when Choice = 'o';
		end loop;

		-- R2 : Deviner le nombre ----------------------------------------------------------
		loop
			Compteur:= Compteur + 1;

			-- R3 : Proposer un nombre ---------------------------------------------------
			Nombre_Devine:= (Maxi + Mini) / 2;
			Put("Je propose ");
			Put(Nombre_Devine, 1);
			New_Line;

			-- R3 : Demander un indice ---------------------------------------------------
			Juste:= True;
			loop
				if not Juste then
					Put("Je ne comprends pas : ");
					Put(Indice);
					New_Line;
				end if;

				Put("Votre indice (t/p/g) ? ");

				Get(Indice);
				Skip_Line;
				Juste:= False;
			exit when Indice = 't' or Indice = 'p' or Indice = 'g';
			end loop;

			-- R3 : Vérifier l'indice ----------------------------------------------------
			if Indice = 'p' then
				if abs(Maxi - Nombre_Devine) < 1 then
					Triche:= True;
				end if;
			elsif Indice = 'g' then
				if abs(Mini - Nombre_Devine) < 1 then
					Triche:= True;
				end if;
			end if;

			-- R3 : Définir nouvelles bornes ---------------------------------------------
			if Indice = 'p' then
				Mini:= Nombre_Devine + 1;
			elsif Indice = 'g' then
				Maxi:= Nombre_Devine - 1;
			end if;
		exit when Indice = 't' or Triche;
		end loop;

		-- R2 : Afficher le nombre d'essais et message de fin ------------------------------
		if Triche then
			Put("Vous trichez. J'arrête cette partie.");
		else
			Put("J'ai trouvé ");
			Put(Nombre_Devine, 1);
			Put(" en ");
			Put(Compteur, 1);
			Put(" essai(s).");
		end if;
	end Ordinateur_Devine;


	-- Déclaration des variables
	Choix_Pincipal: Character;
	Juste: Boolean := True; -- False au deuxième tour de boucle
begin
	-- R1 : Afficher un menu UI convivial pour le choix des jeux --------------------------

	-- R2 : Demander mini et maxi
	loop
		if not Juste then
			Put_Line("Veuillez rentrer un minimum positif strictement plus petit que le maximum.");
		end if;
		Put ("Min = ");
		Get (Mini);
		Put ("Max = ");
		Get (Maxi);

		Juste:= False;
	exit when Mini < Maxi;
	end loop;

	Juste:= True;

	loop
		if not Juste then
			Put("Choix incorrect.  Recommencez !");
		end if;

		 --R2 : Afficher les choix ----------------------------------------------------------
		New_Line;
		Put_Line("1- L'ordinateur choisit un nombre et vous le devinez");
		Put_Line("2- Vous choisissez un nombre et l'ordinateur le devine");
		Put_Line("0- Quitter");

		--R2 : Demander son choix ----------------------------------------------------------
		Put("Votre choix : ");
		Get(Choix_Pincipal);
		Skip_line;
		New_Line;

		-- R2 : Traiter le choix -----------------------------------------------------------
        case  Character'Pos(Choix_Pincipal) is
			when 49 =>
				Utilisateur_Devine;
				Juste:= True;
			when 50 =>
				Ordinateur_Devine;
				Juste:= True;
			when others =>
				Juste:= False;
		end case;

	exit when Character'Pos(Choix_Pincipal) = 48;
	end loop;
end Jeu_Devin;
