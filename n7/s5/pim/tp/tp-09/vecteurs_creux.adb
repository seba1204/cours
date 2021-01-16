with Ada.Text_IO;                 use Ada.Text_IO;
with Ada.Integer_Text_IO;         use Ada.Integer_Text_IO;
with Ada.Float_Text_IO;           use Ada.Float_Text_IO;
with Ada.Unchecked_Deallocation;

package body Vecteurs_Creux is


	procedure Free is
		new Ada.Unchecked_Deallocation (T_Cellule, T_Vecteur_Creux);


	procedure Initialiser (V : out T_Vecteur_Creux) is
	begin
		V := null;
	end Initialiser;


	procedure Detruire (V: in out T_Vecteur_Creux) is
	begin
		if V /= Null then
			Detruire (V.all.Suivant);
			Free (V);
		end if;
	end Detruire;


	function Est_Nul (V : in T_Vecteur_Creux) return Boolean is
	begin
		return V  = Null;
	end Est_Nul;


	function Composante_Recursif (V : in T_Vecteur_Creux ; Indice : in Integer) return Float is
	begin
		if V /= null then
			if V.all.Indice = Indice then
				return V.all.Valeur;
			else
				return Composante_Recursif(V.all.Suivant, Indice);
			end if;
		else
			return 0.0;
		end if;
	end Composante_Recursif;


	function Composante_Iteratif (V : in T_Vecteur_Creux ; Indice : in Integer) return Float is
		next : T_Vecteur_Creux;
	begin
		next := V;
		if V /= null then
			while next.all.Indice /= Indice or next.all.Suivant /= null loop
				next := next.all.Suivant;
			end loop;
			return next.all.Valeur;
		else
			return 0.0;
		end if;
	end Composante_Iteratif;


	procedure Modifier (V : in out T_Vecteur_Creux ;
				       Indice : in Integer ;
					   Valeur : in Float ) is

		next : T_Vecteur_Creux;
	begin
		next := V;
		while (next /= null) and then ((next.all.Indice /= Indice) or (next.all.Suivant /= null)) loop
			next := next.all.Suivant;
		end loop;
		if  (next /= null) and then (next.all.Suivant /= null) then
			next.all.Valeur := Valeur;
		else
			if next /= null then
				next.all.Suivant := null;
				next.all.Suivant := new T_Cellule;
				next.all.Suivant.all.Indice := Indice;
				next.all.Suivant.all.Valeur := Valeur;
			else
				next := new T_Cellule;
				next.all.Indice := Indice;
				next.all.Valeur := Valeur;
			end if;
		end if;
	end Modifier;


	function Sont_Egaux_Recursif (V1, V2 : in T_Vecteur_Creux) return Boolean is
	begin
		return False;	-- TODO: à changer
	end Sont_Egaux_Recursif;


	function Sont_Egaux_Iteratif (V1, V2 : in T_Vecteur_Creux) return Boolean is
	begin
		return False;	-- TODO: à changer
	end Sont_Egaux_Iteratif;


	procedure Additionner (V1 : in out T_Vecteur_Creux; V2 : in T_Vecteur_Creux) is
	begin
		Null;	-- TODO: à changer
	end Additionner;


	function Norme2 (V : in T_Vecteur_Creux) return Float is
	begin
		return 0.0;	-- TODO: à changer
	end Norme2;


	Function Produit_Scalaire (V1, V2: in T_Vecteur_Creux) return Float is
	begin
		return 0.0;	-- TODO: à changer
	end Produit_Scalaire;


	procedure Afficher (V : T_Vecteur_Creux) is
	begin
		if V = Null then
			Put_Line ("--E");
		else
			-- Afficher la composante V.all
			Put ("-->[ ");
			Put (V.all.Indice, 0);
			Put (" | ");
			Put (V.all.Valeur, Fore => 0, Aft => 1, Exp => 0);
			Put (" ]");

			-- Afficher les autres composantes
			Afficher (V.all.Suivant);
		end if;
	end Afficher;


	function Nombre_Composantes_Non_Nulles (V: in T_Vecteur_Creux) return Integer is
	begin
		if V = Null then
			return 0;
		else
			return 1 + Nombre_Composantes_Non_Nulles (V.all.Suivant);
		end if;
	end Nombre_Composantes_Non_Nulles;


end Vecteurs_Creux;
