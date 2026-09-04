# Signature de courriel CCG

Page autonome qui compose la signature de courriel des collaborateurs CCG.
Le collaborateur ouvre `index.html`, saisit ses coordonnées, copie le résultat
et le colle dans Outlook. Rien à installer, rien à héberger.

## Ce que la page produit

```
Cordialement / Regards,

┌────────┐ │  Siradio Diallo
│  logo  │ │  Senior Consultant Data & Analytics
│  CCG   │ │
└────────┘ │  📞  +224 610 84 18 16  |  +33 7 66 86 15 97 (WhatsApp)
           │  ✉   siradio.diallo@ccggroupe.com
           │  🔗  LinkedIn : …
           │  🌐  www.ccggroupe.com
```

Adresse, second téléphone et LinkedIn sont facultatifs : un champ vide retire
sa ligne, sans laisser d'espace. La mention WhatsApp est une case à cocher,
rattachée au numéro concerné et non à la ligne entière.

La casse du nom est corrigée au rendu : `SIRADIO`, `siradio` et `Siradio`
donnent tous `Siradio`. Les noms composés et les apostrophes sont respectés —
`JEAN-PIERRE` devient `Jean-Pierre`, `o'NEILL` devient `O'Neill`. La signature
porte toujours le prénom avant le nom, quel que soit l'ordre de saisie.

Les particules font exception à la règle : `de souza` devient `De Souza`.
Aucune méthode automatique ne distingue de façon fiable une particule d'un nom.

## Diffusion

`index.html` se suffit à lui-même : le logo y est encodé, il n'y a ni script
externe ni feuille de style distante. On peut donc l'envoyer en pièce jointe,
le déposer sur un partage réseau ou le servir par GitHub Pages — dans les trois
cas il fonctionne, y compris hors connexion.

Deux points valent d'être rappelés aux collaborateurs : la fonction doit être
libellée comme dans l'organigramme, et le courriel en `prenom.nom@ccggroupe.com`.
C'est là que les signatures divergent en pratique.

## Reconstruire la page

```bash
python outils/build.py
```

Le script lit `outils/logo-ccg.png`, l'encode en base64 et réécrit `index.html`.
Toute modification passe par `outils/build.py` : éditer `index.html` à la main
serait perdu à la reconstruction suivante.

## Ce qu'il ne faut pas moderniser

La signature est bâtie en tableaux avec des styles en ligne. C'est archaïque,
mais c'est la seule construction qu'Outlook rende correctement : il utilise le
moteur de rendu de Word, qui ignore la mise en page moderne. Ne pas remplacer
les tableaux par des blocs, ne pas déplacer les styles dans une feuille séparée
— la plupart des messageries la supprimeraient au collage.

Les pictogrammes sont des caractères, pas des images. Ils survivent au
copier-coller et ne se transforment pas en carré vide chez un destinataire qui
bloque les images distantes, ce que fait Outlook par défaut.
