
#include "date.h"
#ifndef ENSEIGNANT_H
	#define ENSEIGNANT_H
	struct enseignant {
		char *nom;
		Date *d_naissance;
	};
	typedef struct enseignant enseignant; 
#endif