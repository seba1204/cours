with Ada.Text_IO;           use Ada.Text_IO;

-- Piloter un drone au moyen d'un menu textuel.
procedure Drone is
    Choix: Character := 'a';
    Altitude: Integer := 0;
    HasStarted: Boolean := False;

begin

   --Boucle principale

   loop
      New_Line;
      Put("Altitude : " & Integer'Image (Altitude));
      New_Line;
      Put("Que faire ?");
      New_Line;
      Put("    d -- Démarrer");
      New_Line;
      Put("    m -- Monter");
      New_Line;
      Put("    s -- Descendre");
      New_Line;
      Put("    q -- Quitter");
      New_Line;
      Put("Votre choix : ");
      Get(Choix);
      Skip_Line;
      case Choix is
      when 'd' => HasStarted := True;
      when 'q' => null;
      when 'm' | 's' =>
         if HasStarted then
            case Choix is
               when 'm' => Altitude := Altitude + 1;
               when 's'  =>
                  if Altitude > 0 then
                     Altitude := Altitude - 1;
                  else
                     Put_Line("Le drône est déjà posé.");
                  end if;
               when others => null;
            end case;
         else
            Put("Le drone n'est pas démarré.");
         end if;
      when others => Put_Line("Je n'ai pas compris !");
      end case;

      exit when Choix = 'q' or Altitude >= 5;
      end loop;

   if HasStarted and Altitude < 5 then
      Put("Au revoir...");
   elsif Altitude = 5 then
        Put_Line("Le drone est hors de portée... et donc perdu !");
   else
        Put_Line("Vous n'avez pas réussi à le mettre en route ?");
   end if;


   -- Message d'au revoir


end Drone;
