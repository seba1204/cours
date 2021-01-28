% exemples = ["worm", "exemple_sujet",  "brainlinks",  "Linux26"];

debut = 0;
fin = 10000;
pas = 100;

sous_dossier = "fichiers";

m = fix((fin - debut) / pas);
exemples = [];
while length(exemples) < m
    exemples = string(char(randi([97 122],m,10)));
    exemples = unique(exemples);
end
% génération des fichiers
for i = 1:m
    j = i * pas + debut;
    fid = fopen('./' + sous_dossier + '/' + exemples(i) + '.net','w');
    donnees = generer_ligne(0, j-1);
    fprintf(fid,'%d\n', j);
    fprintf(fid,'%d %d \n',donnees);
    fid = fclose(fid);
end

temps_Creux = zeros(m, 1);
temps_Naif = zeros(m, 1);

for i = 1:m
    disp('Calcul de ' + exemples(i) + '...');
    [~,sortie] = system('pagerank -V -M -P ./' + sous_dossier + '/' + exemples(i) + '.net');
    temps_Creux(i) = str2double(regexp(sortie, '(\d*).$', 'Match'));
    [~,sortie] = system('pagerank -V -M ./' + sous_dossier + '/' + exemples(i) + '.net');
    temps_Naif(i) = str2double(regexp(sortie, '(\d*).$', 'Match'));
end

plot(debut+pas:pas:fin, temps_Creux,'DisplayName','G Creuse');
hold on;
plot(debut+pas:pas:fin, temps_Naif,'DisplayName','G Naive');
legend;
hold off;


function [ligne] = generer_ligne(mini, maxi)
    nb_liens = max([int32(0.5 * maxi) 1]);
    referenceur = randi([mini maxi], 1, nb_liens);
    valid_vals = setdiff(mini:maxi, referenceur);
    destinataire = valid_vals( randi(length(valid_vals), 1, nb_liens) );
    ligne = [referenceur destinataire];
end
