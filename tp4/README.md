# Travaux pratiques : séance 4

## Opérateurs connexes : travail évalué

Dans ce TP nous allons travailler sur les opérateurs connexes.

Ce travail sera évalué et donnera lieu à un rapport sous forme de fichier `README.md` dans votre dépôt git, à l'intérieur du répertoire `TP4`.
Ce rapport devra contenir un ensemble de jeux d'essais permettant d'évaluer qualitativement la justesse de votre implémentation.
Chaque exercice donnera lieu à un texte qui expliquera la démarche employée et justifiera les choix d'implémentation.

Pour les jeux de tests, considérer des images suffisamment variées et représentatives (images binaires, images en niveaux de gris, images naturelles, etc.).

## Extrema régionaux

1.  Implémenter en Python deux fonctions permettant de calculer les maxima régionaux et les minima régionaux d'une image. 

2. Comparer votre implémentation avec l'implémentation proposée dans `scikit-image` : https://scikit-image.org/docs/dev/api/skimage.morphology.html#skimage.morphology.local_maxima

## Reconstruction géodésique

1. Implémenter en Python l'opérateur de reconstruction géodésique.
Vous pourrez vous appuyer sur l'algorithme décrit dans cet article :
https://people.cmm.minesparis.psl.eu/users/marcoteg/cv/publi_pdf/MM_refs/Vincent/Vincent_Reconstruction_10.1.1.116.5241.pdf
 
2. Comparer votre implémentation avec l'implémentation proposée dans `scikit-image` : https://scikit-image.org/docs/dev/api/skimage.morphology.html#skimage.morphology.reconstruction

## Filtrage par dynamique

Implémenter deux fonctions `hmin_filter` (respectivement `hmax_filter`) permettant de supprimer les minima régionaux (respectivement maxima régionaux) dont la dynamique est inférieure à $`h`$ (respectivement supérieure à $`h`$).



## Applications 

1. Seuillage par hystérèse

    Bien souvent, un seuillage global d’une image ne permet pas de segmenter efficacement des objets. Le principe du seuillage par hystérese est le suivant :

    - on utilise un seuil large pour conserver le maximum de points des objets à segmenter (image $`f_1`$).
    - on utilise un seuil étroit pour conserver uniquement des points appartenant aux objets à segmenter (image $`f_2`$).
    on reconstruit les objets à segmenter en effectuant une reconstruction géodésique par dilatation de l’image du seuil étroit dans l’image du seuil large.
    Voir également : http://dpt-info.u-strasbg.fr/~cronse/TIDOC/FEAT/double.html

    Ainsi dans le résultat final apparaîtront uniquement les composantes connexes de `f_1` contenant les points de `f_2`. Cette technique ne fonctionne que si, dans $`f_1`$, il n’existe aucune connexion entre les objets à segmenter et les objets indésirables (bruit, fond de l’image...). 
    Illustrez l’intérêt de cette technique sur l’image ci-dessous et écrire le code correspondant.

    <img src="pcb_gray.png" width="400">

   
    


