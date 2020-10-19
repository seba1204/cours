with Ada.Text_IO;             use Ada.Text_IO;
with Ada.Integer_Text_IO;     use Ada.Integer_Text_IO;

procedure Robot_Type_1 is
    Type T_Position is Record
        X: Integer;
        Y: Integer;
    End Record;

    Type T_Etat is (LIBRE, OCCUPE);

    Type T_Direction is (NORD, EST, SUD, OUEST);

	Type T_Robot is Record
	    Position: T_Position;
	    Direction: T_Direction;
	End Record;

	Borne_Max_X : CONSTANT Integer := 10;
	Borne_Max_Y : CONSTANT Integer := 10;

	Type T_Environnement is array (1..Borne_Max_x, 1..Borne_Max_Y) Of T_Etat;

    function Est_Libre(Robot: in T_Robot; Env: in out T_Environnement) return Boolean is
        X : Integer;
        Y : Integer;
    begin
      X := Robot.Position.X;
      Y := Robot.Position.Y;
      return Env(X, Y) = LIBRE;
      end Est_Libre;

--| Le programme principal |------------------------------------------------
	R1 : T_Robot;
	R2 : T_Robot;

	E1 : T_Environnement;

	Position : T_Position;

begin

	-- Initialiser R1 pour que son abscisse soit 4, son ordonnée 2 et sa direction ouest
    Position.X := 4;
    Position.Y := 2;
    R1.Position := Position;
	-- Initialiser R2 avec R1
    R2 := R1;

	-- Modifier l'abscisse de R1 pour qu'elle devienne 3
    R1.Position.X := 3;

	-- Afficher l'abscisse de R1. La valeur affichée sera 3
	Put ("Abscisse de R1 : ");
	Put (R1.Position.X, 1);
	New_Line;

	-- Afficher l'abscisse de R2. La valeur affichée sera 4
	Put ("Abscisse de R2 : ");
	Put (R2.Position.X, 1);
	New_Line;

	-- Modifier l'environnement pour que la case de coordonnées (4,2) soit libre.
	E1(4,2) := LIBRE;


	-- Afficher "OK" si le robot R1 est sur une case libre, "ERREUR" sinon
	if Est_Libre(R1, E1) then
		Put_Line ("OK");
	else
		Put_Line ("ERREUR");
	end if;

end Robot_Type_1;
