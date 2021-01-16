package body Google is

   ------------------
   -- Definir_Type --
   ------------------

   procedure Definir_Type (Id : in Boolean) is
   begin
      Type_Id := Id; -- True => Naive, False => Creuse
   end Definir_Type;

   -------------
   -- Nb_Page --
   -------------

   function Nb_Page (Nom_Fichier : in Unbounded_String) return Integer is
    Taille      : Integer;
    Fichier_Net : Ada.Text_IO.File_Type;
   begin
      begin
         Open (Fichier_Net, In_File, To_String (Nom_Fichier));
         Get (Fichier_Net, Taille);
         if Taille > CAPACITE_MAX then
            raise ERREUR_Capacite_Max_Depassee;
         end if;
         Close (Fichier_Net);
         return Taille;
      exception
         when others =>
            Close (Fichier_Net);
            raise ERREUR_Lecture_Taille;
      end;
   end Nb_Page;

   --------------------
   -- Calculer_Coefs --
   --------------------

   procedure Calculer_Coefs
     (Nom_Fichier : in Unbounded_String; Taille : in Integer; A : in T_Float)
   is
   begin
      if Type_Id then
         Google_Naive_Table.Calculer_Coefs(Nom_Fichier, Taille, A);
      else
         Google_creuse_Table.Calculer_Coefs(Nom_Fichier, Taille, A);
      end if;
   end Calculer_Coefs;

   -----------------------
   -- Initialiser_Poids --
   -----------------------

   procedure Initialiser_Poids (Pi : out T_Poids; Taille : in Integer) is
   begin
      if Type_Id then
         Google_Naive_Table.Initialiser_Poids (Pi, Taille);
      else
         Google_creuse_Table.Initialiser_Poids (Pi, Taille);
      end if;
   end Initialiser_Poids;

   --------------------
   -- Calculer_Poids --
   --------------------

   procedure Calculer_Poids
     (Pi          : in out T_Poids; Taille : in Integer; Max_Iter : in Integer;
      Nom_Fichier : in     Unbounded_String)
   is
   begin
      if Type_Id then
         Google_Naive_Table.Calculer_Poids (Pi, Taille, Max_Iter, Nom_Fichier);
      else
         Google_creuse_Table.Calculer_Poids (Pi, Taille, Max_Iter, Nom_Fichier);
      end if;
   end Calculer_Poids;

   -----------------
   -- Trier_Poids --
   -----------------

   procedure Trier_Poids
     (Pi_Trie : out T_Poids; Pi : in T_Poids; Taille : in Integer)
   is
   begin
      if Type_Id then
         Google_Naive_Table.Calculer_Coefs(Nom_Fichier, Taille, A);
      else
         Google_creuse_Table.Calculer_Coefs(Nom_Fichier, Taille, A);
      end if;
   end Trier_Poids;

   --------------------
   -- Creer_Fichiers --
   --------------------

   procedure Creer_Fichiers
     (Pi : in T_Poids; Pi_Trie : in T_Poids; Taille : in Integer;
      a : in T_Float; Max_Iter : in Integer; Nom_Fichier : in Unbounded_String)
   is
   begin
      if Type_Id then
         Google_Naive_Table.Trier_Poids (Pi_Trie, Pi, Taille);
      else
         Google_creuse_Table.Trier_Poids (Pi_Trie, Pi, Taille);
      end if;
   end Creer_Fichiers;

end Google;
