with Ada.Text_IO;       use Ada.Text_IO;
with Ada.Float_Text_IO; use Ada.Float_Text_IO;
with Vecteurs_Creux;    use Vecteurs_Creux;

-- Exemple d'utilisation des vecteurs creux.
procedure Exemple_Vecteurs_Creux is

	V : T_Vecteur_Creux;
	Epsilon: constant Float := 1.0e-5;
begin
	Put_Line ("---- Début du scénario ----");




	
	Put_Line("Etape 1 - On initialise V :");
	Initialiser(V);
	Afficher(V);

	Put_Line("Etape 2 - On vérifie que V est vide :");
	if Est_Nul(V) then
		Put_Line("V est bien vide");
	else
		Put_Line("Ha... je m'attendais pas à ça...");
	end if;

	Put_Line("Etape 3 - On détruit V : ");
	Detruire(V);
	Afficher(V);

	
	Put_Line("Etape 4.1 - On affiche la 18ème composante de V de manière itérative : ");
	Initialiser(V);
	Put(Composante_Iteratif(V, 18));
	Put_Line("");

	Put_Line("Etape 4.2 - On affiche la 18ème composante de V de manière récursive : ");
	Put(Composante_Recursif(V, 18));
	Put_Line("");


	Put_Line("Etape 5 - On modifie des éléments de la liste : ");
	Put_Line("Etape 5.1 - V[2] = 4.5 ");
	Modifier(V, 2, 4.5);
	Afficher(V);
	Put_Line("Etape 5.2 - V[5] = 18.6 ");
	Modifier(V, 5, 18.6);
	Afficher(V);
	Put_Line("Etape 5.3 - V[3] = 4.8 ");
	Modifier(V, 3, 4.8);
	Afficher(V);


	Put_Line ("---- Fin du scénario ----");
end Exemple_Vecteurs_Creux;
