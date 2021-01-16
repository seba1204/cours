with Ada.Text_IO;          use Ada.Text_IO;
with Ada.Integer_Text_IO;  use Ada.Integer_Text_IO;

-- Afficher la somme des valeurs d'un série dont les valeurs sont lues au clavier.
-- Pour marquer la fin de la série, la dernière valeur est doublée.
procedure tp is

	Somme: Integer:= 0;	    	-- Somme des valeurs de la série
   Car: Integer:= 0;
   OldCar: Integer;
begin
	-- Déterminer la somme des valeurs d'une série lue un clavier
   loop
      OldCar := Car;
      Get(Car);
      Skip_Line;
      Somme := Somme + Car;
      exit when OldCar = Car;
      Somme := Somme - Car;
   end loop;
	-- Afficher la longueur
	Put ("Somme : ");
	Put (Somme, 1);
	New_Line;

end tp;
