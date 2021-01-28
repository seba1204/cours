/**
 *  \author Xavier Crégut <nom@n7.fr>
 *  \file file.c
 *
 *  Objectif :
 *	Implantation des opérations de la file
*/

#include <malloc.h>
#include <assert.h>

#include "file.h"

void initialiser(File *f)
{
    f->tete = NULL;
    f->queue = NULL;

    assert(est_vide(*f));
}

void detruire(File *f)
{
    Cellule *Cellule_actuelle;
    Cellule *Cellule_precedente;
    Cellule_actuelle = f->tete;
    while (Cellule_actuelle->suivante != NULL)
    {
        Cellule_precedente = Cellule_actuelle;
        Cellule_actuelle = Cellule_actuelle->suivante;
        free(Cellule_precedente);
        Cellule_precedente->suivante = NULL;
        Cellule_precedente = NULL;
    }

    free(Cellule_actuelle);
    Cellule_actuelle = NULL;
}

char tete(File f)
{
    assert(!est_vide(f));

    return f.tete->valeur;
}

bool est_vide(File f)
{
    return (f.tete == NULL && f.queue == NULL);
}

/**
 * Obtenir une nouvelle cellule allouée dynamiquement
 * initialisée avec la valeur et la cellule suivante précisé en paramétre.
 */
static Cellule *cellule(char valeur, Cellule *suivante)
{
    Cellule *Nouvelle_Cellule = malloc(sizeof(Cellule));
    if (Nouvelle_Cellule)
    {
        Nouvelle_Cellule->valeur = valeur;
        Nouvelle_Cellule->suivante = suivante;
    }
    return Nouvelle_Cellule;
}

void inserer(File *f, char v)
{
    assert(f != NULL);
    Cellule *Queue = f->queue;
    Queue->suivante = cellule(v, NULL);
    f->queue = Queue->suivante;
}

void extraire(File *f, char *v)
{
    assert(f != NULL);
    assert(!est_vide(*f));
    Cellule *Tete = f->tete;
    f->tete = Tete->suivante;
    *v = Tete->valeur;
}

int longueur(File f)
{
    int compteur = 0;
    Cellule *Cellule_actuelle;
    Cellule_actuelle = f.tete;
    while (Cellule_actuelle != NULL)
    {
        Cellule_actuelle = Cellule_actuelle->suivante;
        compteur++;
    }
    return compteur;
}
