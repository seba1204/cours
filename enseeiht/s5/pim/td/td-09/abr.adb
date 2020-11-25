with SDA_Exceptions;         use SDA_Exceptions;
with Ada.Unchecked_Deallocation;

package body ABR is

	procedure Free is
		new Ada.Unchecked_Deallocation (Object => T_Noeud, Name => T_ABR);


	procedure Initialiser(Sda: out T_ABR) is
	begin
		Sda := null;
	end Initialiser;


	function Est_Vide (Sda : T_ABR) return Boolean is
	begin
		return Sda = null;
	end Est_Vide;


	function Taille (Sda : in T_ABR) return Integer is
	begin
		if Sda = null then
			return 0;
		elsif  Sda.all.Sous_Arbre_Gauche = null and Sda.all.Sous_Arbre_Droit = null then
			return 1;
		else
			return Taille(Sda.all.Sous_Arbre_Droit) + Taille(Sda.all.Sous_Arbre_Gauche);
		end if;
	end Taille;

	procedure Enregistrer (Sda : in out T_ABR ; Cle : in T_Cle ; Donnee : in T_Donnee) is
		Sda_Actuel : T_ABR;
	begin
		Sda_Actuel := Sda;
		while Sda_Actuel /= null and then Sda_Actuel.all.Cle = Cle loop
			if Sda_Actuel.all.Cle < Cle then
				Sda_Actuel := Sda.all.Sous_Arbre_Droit;
			elsif Sda_Actuel.all.Cle /= Cle then
				Sda_Actuel := Sda.all.Sous_Arbre_Gauche;
			end if;
		end loop;
		if Sda_Actuel = null then
			Sda_Actuel := new T_Noeud;
			Sda_Actuel.all.Cle := Cle;
			Sda_Actuel.all.Donnee := Donnee;
		elsif Sda_Actuel.all.Cle = Cle then
			Sda_Actuel.all.Donnee := Donnee;
		end if;
	end Enregistrer;


	function La_Donnee (Sda : in T_ABR ; Cle : in T_Cle) return T_Donnee is
		Sda_Actuel : T_ABR;
	begin
		Sda_Actuel := Sda;
		while Sda_Actuel /= null and then Sda.all.Cle /= Cle loop
			if Sda_Actuel.all.Cle < Cle then
				Sda_Actuel := Sda.all.Sous_Arbre_Droit;
			elsif Sda_Actuel.all.Cle /= Cle then
				Sda_Actuel := Sda.all.Sous_Arbre_Gauche;
			end if;
		end loop;
		if Sda_Actuel = null then
			raise Cle_Absente_Exception;
		else
			return Sda_Actuel.all.Donnee;
		end if;
	end La_Donnee;


	procedure Supprimer (Sda : in out T_ABR ; Cle : in T_Cle) is
	begin
		null;	-- TODO: à changer
	end Supprimer;

	procedure decrocher_min (Sda : in out T_ABR ; Cle : in T_Cle) is
	begin
	
	end decrocher_min;

	procedure Vider (Sda : in out T_ABR) is
	begin
		null;	-- TODO: à changer
	end Vider;


	procedure Pour_Chaque (Sda : in T_ABR) is
	begin
		null;	-- TODO: à changer
	end Pour_Chaque;


end ABR;
