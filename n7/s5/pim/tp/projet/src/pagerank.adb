with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Exceptions;        use Ada.Exceptions;
with Exceptions;            use Exceptions;
with Helpers;               use Helpers;
with Google;

procedure Pagerank is
   package Google_Table is new Google
      (T_Float => T_Double, Capacite_Max => 10_000);
   use Google_Table;

   Nom_Fichier  : Unbounded_String;  -- nom du fichier .net a charger
   A            : T_Double;          -- coefficient alpha
   Max_Iter     : Integer;           -- nombre maximum d'iterations
   P            : Boolean;           -- commuter naif / creux
   Pi           : T_Poids;           -- le vecteur des poids
   Pi_Trie      : T_Poids;           -- le vecteur des poids trie
   Taille       : Integer;           -- nombre de pages web
   Aide_Demande : Boolean;           -- 

begin
   --  Supprimer les lignes du terminal
   Nettoyer_Console;
   --  Lire les arguments fournis par l'utilisateur
   Lire_Args (Nom_Fichier, A, Max_Iter, P, Aide_Demande);

   if not (Aide_Demande) then -- Si l'utilisateur ne demande pas de l'aide
      --  Recuperer le nombre de pages
      Taille := Nb_Page (Nom_Fichier);
      --  Informer l'utilisateur de la taille requise pour le calcul
      Estimer_Donnees(Taille, Max_Iter);
      -- Calculer la matrice G
      Calculer_Coefs(Nom_Fichier, Taille, A);
      --  Initialiser le tableau pi des poids
      Initialiser_Poids (Pi, Taille);
      --  Rechercher la valeur finale du vecteur pi
      Calculer_Poids (Pi, Taille, Max_Iter, Nom_Fichier);
      --  Trier les elements de pi par ordre de poids croissant
      Trier_Poids (Pi_Trie, Pi, Taille);
      --  Generer les fichiers de sortie
      Creer_Fichiers (Pi, Pi_Trie, Taille, A, Max_Iter, Nom_Fichier);
   end if;

  
exception
   when Erreur_Lire_Args => -- le message d'erreur a deja ete emis
      null;

   when Erreur_Lecture_Taille =>
      Put_Line
        ("Une erreur est survenue lors de la lecture de la taille du reseau.");
      Put_Line
        ("Veuillez vérifier que la premiere ligne du fichier est bien");
      Put_Line ("un entier representant la taille du reseau.");

   when Erreur_Capacite_Max_Depassee =>
      Put_Line ("Attention la taille du reseau est trop grande.");
      Put_Line ("Veuillez augmenter la valeur de la variable CAPACITE_MAX");
      Put_Line ("dans le fichier pagerank.adb");

   when E : others =>
      Put_Line ("Une erreur non geree est survenue :");
      Put_Line (Exception_Message (E));
end Pagerank;
