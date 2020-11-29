with Ada.Unchecked_Deallocation;

package body LCA is

	procedure Free is
		new Ada.Unchecked_Deallocation (Object => T_Cellule, Name => T_LCA);


	procedure Initialiser(Sda: out T_LCA) is
	begin
		Sda := null;
	end Initialiser;


	function Est_Vide (Sda : T_LCA) return Boolean is
	begin
		return Sda = null;
	end;


	function Taille (Sda : in T_LCA) return Integer is
		compteur : Integer;
		Sda_En_Cours : T_LCA;
	begin
		compteur := 0;
		Sda_En_Cours := Sda;
		
		while Sda_En_Cours /= null loop
			compteur := compteur + 1;
			Sda_En_Cours := Sda_En_Cours.all.Suivant;
		end loop;

		return compteur;
	end Taille;

	-- Enregistrer une Donnée à la fin de la SDA chainée
	-- Si la clé est déjà présente dans la Sda, sa donnée est changée.
	procedure Enregistrer (Sda : in out T_LCA ; Cle : in T_Cle ; Donnee : in T_Donnee) is
		Sda_En_Cours : T_LCA;
	begin
		Sda_En_Cours := Sda;
		
		while Sda_En_Cours /= null and then (Sda_En_Cours.all.Suivant /= null and Sda_En_Cours.all.Cle /= Cle) loop
			Sda_En_Cours := Sda_En_Cours.all.Suivant;
		end loop;

		-- on est sorti de la boucle soit :
		-- 	1. parce que Sda en entrée était nul (donc on n'est jamais rentré dans la boucle)
		--	2. parce que Sda_En_Cours.all.Suivant = null donc on est en fin de chaîne
		--	3. parce que Sda_En_Cours.all.Cle = Cle, il faut donc modifier la donnée associée à cette clé
		-- rq : on peut avoir les conditions 2. et 3. en même temps
		if Sda = null then
			Sda := new T_Cellule;
			Sda.all.Cle := Cle;
			Sda.all.Donnee := Donnee;
		elsif Sda_En_Cours.all.Cle = Cle then
			Sda_En_Cours.all.Donnee := Donnee;
		elsif Sda_En_Cours.all.Suivant = null then
			Sda_En_Cours.all.Suivant := new T_Cellule;
			Sda_En_Cours.all.Suivant.all.Cle := Cle;
			Sda_En_Cours.all.Suivant.all.Donnee := Donnee;
		end if;
		
	end Enregistrer;


	function Cle_Presente (Sda : in T_LCA ; Cle : in T_Cle) return Boolean is
		Sda_En_Cours : T_LCA;
    begin
		Sda_En_Cours := Sda;
		while Sda_En_Cours /= null loop
			if Sda_En_Cours.all.Cle = Cle then
				return True;
			end if;
			Sda_En_Cours := Sda_En_Cours.all.Suivant;
		end loop;
		return False;
	end;


	function La_Donnee (Sda : in T_LCA ; Cle : in T_Cle) return T_Donnee is
		Sda_En_Cours : T_LCA;
	begin
		Sda_En_Cours := Sda;
		while Sda_En_Cours /= null loop
			if Sda_En_Cours.all.Cle = Cle then
				return Sda_En_Cours.all.Donnee;
			end if;
			Sda_En_Cours := Sda_En_Cours.all.Suivant;
		end loop;
		-- si on est ici, c'est qu'on n'est pas sorti grâce au return, donc la clé
		-- n'existe pas
		raise Cle_Absente_Exception;
	end La_Donnee;


	procedure Supprimer (Sda : in out T_LCA ; Cle : in T_Cle) is
		Sda_En_Cours : T_LCA;
		Sda_Precedent : T_LCA;
	begin
		Sda_En_Cours := Sda;
		while Sda_En_Cours /= null and then Sda_En_Cours.all.Cle /= Cle loop
	  		Sda_Precedent := Sda_En_Cours;
			Sda_En_Cours := Sda_En_Cours.all.Suivant;
		end loop;

		-- Si on est sorti de la boulce car Sda_En_Cours est null, c'est qu'on est en fin de chaîne
		-- et donc qu'on n'a pas trouvé la clé dans la liste
		if Sda_En_Cours = null then
			raise Cle_Absente_Exception;
		else 
			-- Normalement ici on a Sda_En_Cours.all.Suivant.all.Cle = Cle
   			-- Donc on va changer le 'Suivant' du en cours par le Suivant du Suivant (s'il n'est pas null)
			if Sda_Precedent = null then
				Sda := Sda.all.Suivant;
			else
				Sda_Precedent.all.Suivant := Sda_En_Cours.all.Suivant;
			end if;
		end if;

	end Supprimer;


	procedure Vider (Sda : in out T_LCA) is
	begin
		if Sda /= Null then
			Vider(Sda.all.Suivant);
			Free(Sda);
		end if;
	end Vider;


	procedure Pour_Chaque (Sda : in T_LCA) is
		Sda_En_Cours : T_LCA;
    begin
		Sda_En_Cours := Sda;
		while Sda_En_Cours /= null loop
			begin
				Traiter(Sda_En_Cours.all.Cle, Sda_En_Cours.all.Donnee);
			exception
				when others => null;
			end;
			Sda_En_Cours := Sda_En_Cours.all.Suivant;
		end loop;
	end Pour_Chaque;


end LCA;