# -*- coding: utf-8 -*-
"""Assemble index.html, l'outil de signature de courriel CCG.

    python outils/build.py

Le logo est encode dans la page. Une fois construite, elle n'a besoin de rien :
ni serveur, ni image hebergee, ni connexion.
"""
import base64, io, os

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
B64 = base64.b64encode(
    open(os.path.join(ICI, 'logo-ccg.png'), 'rb').read()).decode('ascii')

HTML = r"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Signature de courriel — CCG</title>
<style>
  :root{
    --ground:#F5F7FA; --panel:#FFFFFF; --edge:#DCE3EC;
    --ink:#13294B; --ink-2:#4C5768; --ink-3:#8A94A6;
    --bleu:#1F5FBF; --rouge:#D4202A; --jaune:#F5C518;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--ground);color:var(--ink);
    font:15px/1.6 'Segoe UI',system-ui,-apple-system,sans-serif}
  .wrap{max-width:900px;margin:0 auto;padding:36px 22px 90px}
  h1{font-size:27px;margin:0;letter-spacing:-.02em}
  .chapo{margin-top:10px;color:var(--ink-2);max-width:62ch}
  h2{font-size:17px;margin:34px 0 12px;color:var(--bleu)}
  .carte{background:var(--panel);border:1px solid var(--edge);border-radius:12px;padding:22px}
  .grille{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  @media(max-width:680px){.grille{grid-template-columns:1fr}}
  label{display:block;font-size:12.5px;font-weight:600;color:var(--ink-2);
    text-transform:uppercase;letter-spacing:.06em;margin-bottom:5px}
  label .doux{font-weight:400;text-transform:none;letter-spacing:0;color:var(--ink-3)}
  input,select{width:100%;padding:9px 11px;border:1px solid var(--edge);border-radius:8px;
    font:15px 'Segoe UI',sans-serif;color:var(--ink);background:#fff}
  input:focus,select:focus{outline:2px solid var(--bleu);outline-offset:1px;border-color:var(--bleu)}
  optgroup{font-weight:600;color:var(--ink-3)}
  optgroup option{font-weight:400;color:var(--ink)}
  .plein{grid-column:1/-1}
  .case{display:flex;align-items:center;gap:7px;margin-top:8px;font-size:13.5px;
    font-weight:400;text-transform:none;letter-spacing:0;color:var(--ink-2);cursor:pointer}
  .case input{width:auto;margin:0;accent-color:var(--bleu);cursor:pointer}
  .apercu{background:#fff;border:1px dashed var(--edge);border-radius:12px;padding:24px;
    margin-top:14px;overflow-x:auto}
  button{background:var(--bleu);color:#fff;border:0;border-radius:8px;
    padding:11px 20px;font:600 15px 'Segoe UI',sans-serif;cursor:pointer}
  button:hover{background:#17499A}
  .actions{display:flex;gap:10px;align-items:center;margin-top:16px;flex-wrap:wrap}
  .etat{font-size:14px;color:#1B6B4A;font-weight:600}
  ol{padding-left:20px;color:var(--ink-2)} ol li{margin-bottom:9px}
  code{background:#EEF1F6;border:1px solid var(--edge);border-radius:5px;
    padding:1px 6px;font-family:ui-monospace,Consolas,monospace;font-size:.88em;color:#1D3A55}
  .note{border-left:3px solid var(--jaune);background:#FEFAEC;border-radius:0 10px 10px 0;
    padding:14px 18px;margin-top:16px;color:var(--ink-2);font-size:14.5px}
  .note strong{color:var(--ink)}
</style>
</head>
<body>
<div class="wrap">

  <h1>Signature de courriel CCG</h1>
  <p class="chapo">Chaque collaborateur ouvre ce fichier, saisit ses coordonnées, copie la
     signature et la colle dans Outlook. Le logo est intégré au fichier : rien à héberger.</p>

  <h2>1. Vos coordonnées</h2>
  <div class="carte">
    <div class="grille">
      <div>
        <label for="choixFormule">Formule de politesse</label>
        <select id="choixFormule">
          <optgroup label="Bilingue">
            <option>Cordialement / Regards,</option>
            <option>Bien cordialement / Best regards,</option>
          </optgroup>
          <optgroup label="Français">
            <option>Cordialement,</option>
            <option>Bien cordialement,</option>
            <option>Bien à vous,</option>
            <option>Sincères salutations,</option>
            <option>Respectueusement,</option>
            <option>Merci et bonne journée,</option>
          </optgroup>
          <optgroup label="English">
            <option>Best regards,</option>
            <option>Kind regards,</option>
            <option>Regards,</option>
            <option>Sincerely,</option>
            <option>Many thanks,</option>
          </optgroup>
          <option value="">Aucune formule</option>
        </select>
      </div>
      <div>
        <label for="formule">Texte de la formule <span class="doux">— modifiable</span></label>
        <input id="formule" value="Cordialement / Regards,">
      </div>
      <div>
        <label for="prenom">Prénom</label>
        <input id="prenom" value="Siradio">
      </div>
      <div>
        <label for="nom">Nom</label>
        <input id="nom" value="Diallo">
      </div>
      <div>
        <label for="fonction">Fonction</label>
        <input id="fonction" value="Senior Consultant Data &amp; Analytics">
      </div>
      <div>
        <label for="tel1">Téléphone professionnel</label>
        <input id="tel1" value="+224 610 84 18 16">
        <label class="case" for="wa1"><input type="checkbox" id="wa1">
          Ce numéro est aussi sur WhatsApp</label>
      </div>
      <div>
        <label for="tel2">Second téléphone <span class="doux">— facultatif</span></label>
        <input id="tel2" value="+33 7 66 86 15 97">
        <label class="case" for="wa2"><input type="checkbox" id="wa2" checked>
          Ce numéro est aussi sur WhatsApp</label>
      </div>
      <div>
        <label for="mail">Courriel</label>
        <input id="mail" value="siradio.diallo@ccggroupe.com">
      </div>
      <div class="plein">
        <label for="adresse">Adresse <span class="doux">— facultative, laisser vide pour retirer la ligne</span></label>
        <input id="adresse" value="Sanoyah km 38 / Conakry République de Guinée">
      </div>
      <div class="plein">
        <label for="linkedin">LinkedIn <span class="doux">— facultatif, laisser vide pour retirer la ligne</span></label>
        <input id="linkedin" value="https://www.linkedin.com/in/ss-diallo/">
      </div>
      <div class="plein">
        <label for="site">Site</label>
        <input id="site" value="www.ccggroupe.com">
      </div>
    </div>
  </div>

  <h2>2. Aperçu</h2>
  <div class="apercu" id="apercu"></div>
  <div class="actions">
    <button id="copier">Copier la signature</button>
    <span class="etat" id="etat"></span>
  </div>

  <h2>3. Installation</h2>
  <div class="carte">
    <ol>
      <li><strong>Outlook (bureau)</strong> — Fichier → Options → Courrier → Signatures.
          Créer une signature, coller avec <code>Ctrl+V</code>, enregistrer.
          Définir la signature par défaut pour les nouveaux messages et les réponses.</li>
      <li><strong>Outlook sur le web</strong> — Paramètres → Courrier → Rédiger et répondre →
          Signature électronique. Coller, puis cocher les deux cases d’insertion automatique.</li>
    </ol>
    <div class="note">
      <p><strong>Les champs laissés vides disparaissent.</strong> Adresse, second téléphone
         et LinkedIn sont facultatifs : sans saisie, la ligne correspondante n’apparaît pas,
         et aucun espace vide ne subsiste.</p>
      <p style="margin-bottom:0"><strong>La casse du nom est corrigée automatiquement.</strong>
         Que vous saisissiez <code>SIRADIO</code>, <code>siradio</code> ou <code>Siradio</code>,
         la signature affiche <code>Siradio</code>. Les noms composés sont respectés :
         <code>JEAN-PIERRE</code> devient <code>Jean-Pierre</code>. La signature porte toujours
         le prénom avant le nom.</p>
    </div>
  </div>

  <h2>4. Ce qu’il ne faut pas modifier</h2>
  <div class="carte">
    <p style="margin:0;color:var(--ink-2)">La signature est bâtie en tableaux avec des styles en
       ligne. C’est archaïque, mais c’est la seule construction qu’Outlook rende correctement —
       il utilise le moteur de Word, qui ignore la mise en page moderne. Ne pas remplacer les
       tableaux par des blocs, ne pas déplacer les styles dans une feuille séparée : la plupart
       des messageries la supprimeraient.</p>
  </div>

</div>

<script>
const LOGO_CCG = 'data:image/png;base64,__B64__';
(function () {
  const $ = (id) => document.getElementById(id);
  const ids = ['formule', 'prenom', 'nom', 'fonction', 'tel1', 'tel2', 'mail',
               'adresse', 'linkedin', 'site'];
  const cases = ['wa1', 'wa2'];

  // Le collaborateur tape comme il veut ; la signature, elle, reste uniforme.
  // Une lettre debute un mot apres un espace, un trait d'union ou une apostrophe.
  const capitaliser = (s) => s.replace(/\s+/g, ' ').trim().toLocaleLowerCase('fr')
    .replace(/(^|[\s'’-])(\p{L})/gu, (m, sep, c) => sep + c.toLocaleUpperCase('fr'));

  const echappe = (s) => String(s).replace(/[&<>"]/g, (c) =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const val = (id) => echappe($(id).value.trim());

  // Tableaux + styles en ligne : la seule construction qu'Outlook rende juste.
  function signature() {
    const police = "font-family:Calibri,Arial,Helvetica,sans-serif";
    const corps = police + ";font-size:14px;color:#1A1A1A;line-height:1.55";

    const formule = val('formule');
    const nomAffiche = echappe([capitaliser($('prenom').value), capitaliser($('nom').value)]
      .filter(Boolean).join(' '));
    const fonction = val('fonction');
    const tel1 = val('tel1'), tel2 = val('tel2');
    const mail = val('mail'), adresse = val('adresse');
    const linkedin = val('linkedin'), site = val('site');
    const brut = (t) => t.replace(/[^+0-9]/g, '');

    // Un pictogramme par ligne, comme dans les signatures existantes.
    const ligne = (picto, contenu) =>
      '<tr><td style="padding:1px 8px 1px 0;vertical-align:top;font-size:14px;">' + picto + '</td>'
      + '<td style="padding:1px 0;vertical-align:top;' + corps + ';">' + contenu + '</td></tr>';

    const lien = (href, texte, couleur) =>
      '<a href="' + href + '" style="color:' + (couleur || '#1155CC') + ';text-decoration:underline;">'
      + texte + '</a>';

    // La mention WhatsApp suit le numero concerne, pas la ligne entiere.
    const numero = (t, wa) => t
      ? lien('tel:' + brut(t), t, '#1A1A1A')
        + (wa ? ' <strong style="color:#1F5FBF;">(WhatsApp)</strong>' : '')
      : '';
    const tels = [numero(tel1, $('wa1').checked), numero(tel2, $('wa2').checked)]
      .filter(Boolean).join(' &nbsp;|&nbsp; ');

    const lignes = [];
    if (tels) lignes.push(ligne('&#128222;', '<strong>' + tels + '</strong>'));
    if (mail) lignes.push(ligne('&#9993;', lien('mailto:' + mail, mail)));
    if (adresse) lignes.push(ligne('&#128205;', '<strong>' + adresse + '</strong>'));
    if (linkedin) lignes.push(ligne('&#128279;', 'LinkedIn&nbsp;: ' + lien(linkedin, linkedin)));
    if (site) {
      const href = /^https?:/i.test(site) ? site : 'https://' + site.replace(/^www\./i, 'www.');
      lignes.push(ligne('&#127760;', lien(href, site)));
    }

    // Deux colonnes : le logo, puis un filet vertical qui porte les informations.
    return [
      formule ? '<div style="' + corps + ';padding:0 0 16px 0;">' + formule + '</div>' : '',
      '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;', police, ';">',
        '<tr>',
          '<td style="padding:0 18px 0 0;vertical-align:top;">',
            '<img src="', LOGO_CCG, '" alt="CCG" width="110" height="76" ',
              'style="display:block;border:0;outline:none;text-decoration:none;">',
          '</td>',
          '<td style="padding:0 0 0 18px;border-left:2px solid #1F5FBF;vertical-align:top;">',
            '<div style="', police, ';font-size:16px;font-weight:bold;color:#1F5FBF;',
              'line-height:1.3;">', nomAffiche, '</div>',
            '<div style="', police, ';font-size:14px;font-weight:bold;color:#1A1A1A;',
              'line-height:1.4;padding-top:2px;">', fonction, '</div>',
            '<div style="height:9px;line-height:9px;font-size:0;">&nbsp;</div>',
            '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">',
              lignes.join(''),
            '</table>',
          '</td>',
        '</tr>',
      '</table>'].join('');
  }

  function rafraichir() { $('apercu').innerHTML = signature(); }
  ids.forEach((id) => $(id).addEventListener('input', rafraichir));
  cases.forEach((id) => $(id).addEventListener('change', rafraichir));

  // Le menu ne fait que pre-remplir : le champ texte reste la source.
  $('choixFormule').addEventListener('change', () => {
    $('formule').value = $('choixFormule').value;
    rafraichir();
  });

  rafraichir();

  function dire(msg) {
    $('etat').textContent = msg;
    setTimeout(() => { $('etat').textContent = ''; }, 3000);
  }

  $('copier').addEventListener('click', async () => {
    const html = signature();
    try {
      await navigator.clipboard.write([new ClipboardItem({
        'text/html': new Blob([html], { type: 'text/html' }),
        'text/plain': new Blob([$('apercu').innerText], { type: 'text/plain' }),
      })]);
      dire('Signature copiée — collez-la dans Outlook.');
    } catch (e) {
      const s = window.getSelection(), r = document.createRange();
      r.selectNodeContents($('apercu'));
      s.removeAllRanges(); s.addRange(r);
      dire(document.execCommand('copy')
        ? 'Signature copiée — collez-la dans Outlook.'
        : 'Copie refusée : sélectionnez l’aperçu et faites Ctrl+C.');
      s.removeAllRanges();
    }
  });
})();
</script>
</body>
</html>
"""

HTML = HTML.replace('__B64__', B64)
chemin = os.path.join(RACINE, 'index.html')
io.open(chemin, 'w', encoding='utf-8').write(HTML)
print('  ecrit : %s (%d ko)' % (chemin, os.path.getsize(chemin) / 1024))
