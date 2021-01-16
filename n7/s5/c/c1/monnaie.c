#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <stdbool.h>
#define CAPACITE 5

// Definition du type monnaie
struct t_monnaie
{
    float valeur;
    char devise;
};

typedef struct t_monnaie t_monnaie;

/**
 * \brief Initialiser une monnaie 
 * \param[out] monnaie monnaie à créer
 * \param[in] valeur valeur monnaitaire
 * \param[in] devise de la monnaie 
 * \pre valeur > 0
 */
void initialiser(t_monnaie *monnaie, float valeur, char devise)
{
    assert(valeur > 0);
    monnaie->valeur = valeur;
    monnaie->devise = devise;
}

/**
 * \brief Ajouter une monnaie m1 à une monnaie m2
 * \param[in] m1 monnaie à ajouter
 * \param[in out] m2 monnaie qui sera ajoutée
 */
bool ajouter(t_monnaie m1, t_monnaie *m2)
{
    if (m1.devise == m2->devise)
    {
        m2->valeur += m1.valeur;
        return true;
    }
    return false;
}

/**
 * \brief Tester Initialiser 
 */
void tester_initialiser()
{
    t_monnaie monnaie;
    initialiser(&monnaie, 5, 'd');

    assert(monnaie.valeur == 5);
    assert(monnaie.devise == 'd');
}

/**
 * \brief Tester Ajouter 
 */
void tester_ajouter()
{
    t_monnaie m1;
    t_monnaie m2;

    initialiser(&m1, 5, 'd');
    initialiser(&m2, 6, 'd');
    assert(ajouter(m1, &m2) == true);
    assert(m2.valeur == 11);

    initialiser(&m1, 5, 'd');
    initialiser(&m2, 6, 'e');
    assert(ajouter(m1, &m2) == false);
    assert(m2.valeur == 6);
}

int main(void)
{
    tester_ajouter();
    tester_initialiser();

    // Un tableau de 5 monnaies
    t_monnaie porte_monnaie[CAPACITE];

    //Initialiser les monnaies
    for (int i = 0; i < CAPACITE; i++)
    {
        char devise;
        float valeur;
        printf("Veuillez rentrer la valeur et la devise de la monnaie %i : ", i + 1);
        scanf("%f %c", &valeur, &devise);
        porte_monnaie[i].valeur = valeur;
        porte_monnaie[i].devise = devise;
    }

    // Afficher la somme des toutes les monnaies qui sont dans une devise entrée par l'utilisateur.

    char d;
    printf("\nDe quelle devise voulez-vous faire la somme des monnaies de votre porte monnaie ? ");
    scanf(" %c", &d);

    float s = 0;
    for (int i = 0; i < CAPACITE; i++)
    {
        if (porte_monnaie[i].devise == d)
        {
            s += porte_monnaie[i].valeur;
        }
    }
    printf("\nLa somme des monnaies dont la devise est %c est : %1.2f\n", d, s);

    return EXIT_SUCCESS;
}
