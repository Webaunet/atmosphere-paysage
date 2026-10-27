import re,os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE='https://webaunet.github.io/atmosphere-paysage/'
PHONE_SVG='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
NAV=[('index.html','Accueil'),('prestations.html','Prestations'),('zone.html','Zone d’intervention'),('contact.html','Contact')]
def header(cur):
    links=''.join(f'<a href="{h}"{" aria-current=\"page\"" if h==cur else ""}>{t}</a>' for h,t in NAV)
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{SITE}" aria-label="Atmosphère Paysage, accueil"><img src="images/logo.png" width="520" height="303" alt="Atmosphère Paysage"></a>
    <nav class="nav" id="nav" aria-label="Navigation principale">
      {links}
    </nav>
    <div class="head-right">
      <a class="btn head-call" href="tel:0669718436" aria-label="Appeler le 06 69 71 84 36">{PHONE_SVG}<span>06 69 71 84 36</span></a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="nav" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>'''
FOOTER=f'''<footer class="site-footer">
  <div class="wrap foot">
    <div><a class="logo" href="{SITE}" aria-label="Atmosphère Paysage, accueil"><img src="images/logo.png" width="520" height="303" alt="Atmosphère Paysage"></a><p class="maq">Maquette de site vitrine</p></div>
    <nav aria-label="Pied de page"><a href="prestations.html">Prestations</a><a href="zone.html">Zone d’intervention</a><a href="contact.html">Contact</a></nav>
    <div>Gometz-la-Ville (91) · <a href="tel:0669718436">06 69 71 84 36</a></div>
  </div>
</footer>'''
FAV="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%232f4a34'/%3E%3Ctext x='32' y='47' font-family='Georgia,serif' font-style='italic' font-size='44' text-anchor='middle' fill='%23f7f3ea'%3EA%3C/text%3E%3C/svg%3E"
def page(cur,title,desc,body):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
{header(cur)}

<main id="contenu">
{body}
</main>

{FOOTER}
<script src="js/main.js"></script>
</body>
</html>
'''
def ic(d):return f'<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
I_BENCH=ic('<path="M6 30h36M10 30v10M38 30v10M8 22h32v8H8zM14 22v-8h20v8"/>'.replace('path="','path d="'))
I_PERGOLA=ic('<path d="M6 40V14M42 40V14M2 14h44M10 14v6M18 14v6M26 14v6M34 14v6M40 14v6"/>')
I_WALL=ic('<path d="M6 12h36v8H6zM6 20h36v10H6zM6 30h36v8H6zM20 12v8M32 20v10M14 30v8M28 30v8"/>')
I_GATE=ic('<path d="M6 40V12M42 40V12M6 12h6M36 12h6M12 40V16c0-6 12-6 12 0M36 40V16c0-6-12-6-12 0M24 16v24M6 28h36"/>')
I_PIN=ic('<path d="M24 43s14-12 14-23a14 14 0 0 0-28 0c0 11 14 23 14 23z"/><circle cx="24" cy="20" r="5"/>')
I_HOME=ic('<path d="M6 22 24 8l18 14M10 20v22h28V20M20 42V30h8v12"/>')
I_BUILD=ic('<path d="M10 42V8h20v34M30 18h8v24M16 14h8M16 22h8M16 30h8M4 42h40"/>')
I_TREE=ic('<path d="M24 42V26M24 26c-8 0-14-5-14-12S16 4 24 4s14 3 14 10-6 12-14 12zM18 42h12"/>')
I_PHONE=ic('<rect x="14" y="4" width="20" height="40" rx="4"/><path d="M22 38h4"/>')
I_LAND=ic('<path d="M10 6v36M10 8h26l-6 8 6 8H10"/>')

# ---------------- PRESTATIONS
tick=lambda items:'<ul class="ticks">'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
pres=f'''<section class="section s-ivory hero page-hero">
  <div class="wrap">
    <div class="trait" aria-hidden="true"></div>
    <div class="hero-grid">
      <div>
        <p class="eyebrow">Nos prestations</p>
        <h1>Tout pour votre jardin, <em>en un seul lieu.</em></h1>
        <p class="lead">Aménagement, entretien, menuiserie paysagère, maçonnerie, portails et clôtures : Atmosphère Paysage intervient du dessin du jardin jusqu’à son entretien régulier.</p>
        <div class="cta-row"><a class="btn" href="contact.html">Demander un devis gratuit</a><a class="btn ghost" href="tel:0669718436">Appeler le 06 69 71 84 36</a></div>
      </div>
      <div class="mosaic" aria-label="Aperçu de nos prestations">
        <div class="m1"><img src="images/haies.jpg" width="900" height="491" alt="Paysagiste taillant une haie avec un taille-haie"></div>
        <div class="m2"><img src="images/elagage.jpg" width="900" height="491" alt="Élagueur encordé dans un arbre, troncs coupés au sol"></div>
        <div class="m3"><img src="images/allee.jpg" width="900" height="491" alt="Allée dallée bordée d’un muret en pierre et de massifs"></div>
      </div>
    </div>
  </div>
</section>

<section class="section s-sage s-curve" id="amenagement">
  <div class="wrap split">
    <div class="arch-b reveal"><img src="images/conception.jpg" width="900" height="491" loading="lazy" alt="Deux personnes consultant le plan d’un jardin sur une tablette" style="object-position:72% 50%"></div>
    <div class="reveal">
      <p class="eyebrow">Aménagement paysager</p>
      <h2>Concevoir, planter, décorer.</h2>
      <p class="lead2">Nous nous rendons sur place pour l’état des lieux, puis nous vous conseillons avant d’établir votre devis gratuit.</p>
      {tick(['Conception de jardin','Décoration paysagère','Pose de plantes et de massifs','Taille de haies et de végétaux','Abattage d’arbres','Dessouchage : rabotage des souches et des arbres morts'])}
    </div>
  </div>
</section>

<section class="section s-forest s-curve on-dark" id="entretien">
  <div class="wrap split rev">
    <div class="reveal">
      <p class="eyebrow">Entretien de jardin</p>
      <h2>Un jardin soigné, toute l’année.</h2>
      <p class="lead2">Pour l’entretien régulier de votre espace vert, nous vous proposons un contrat d’entretien renouvelable à l’année.</p>
      {tick(['Tonte de la pelouse','Traitement et regarnissage de pelouse','Installation d’arrosage automatique','Récupération d’eau de pluie','Élagage de vos arbres'])}
      <div class="cta-row" style="margin-top:30px"><a class="btn" href="contact.html">Parler de mon entretien</a></div>
    </div>
    <div class="arch-b reveal"><img src="images/entretien.jpg" width="900" height="502" loading="lazy" alt="Tonte d’une pelouse devant une maison entourée de haies fleuries" style="object-position:30% 50%"></div>
  </div>
</section>

<section class="section s-ivory s-curve" id="ouvrages">
  <div class="wrap">
    <div class="reveal"><p class="eyebrow">Ouvrages sur mesure</p><h2>Bois, pierre et métal<br>pour structurer l’espace.</h2></div>
    <div class="steps three">
      <div class="step c-moss reveal">{I_PERGOLA}<span class="n">Menuiserie paysagère</span><h3>Bois</h3><p>Aménagement de terrasse, installation de ponton, pose de pergola et de carport.</p></div>
      <div class="step c-clay reveal">{I_WALL}<span class="n">Maçonnerie</span><h3>Pierre</h3><p>Muret de jardin, bassin d’agrément et pavage de vos allées.</p></div>
      <div class="step c-bark reveal">{I_GATE}<span class="n">Portails et clôtures</span><h3>Fermetures</h3><p>Pose de portails et de portillons, clôtures et barrières de jardin.</p></div>
    </div>
  </div>
</section>

<section class="section s-bark s-curve on-dark band-end">
  <div class="wrap band">
    <div><p class="eyebrow">Un projet en tête ?</p><h2>Nous venons voir votre jardin.</h2></div>
    <div class="band-actions"><a class="btn" href="contact.html">Devis gratuit</a><a class="btn ghost" href="tel:0169769608">01 69 76 96 08</a></div>
  </div>
</section>'''

# ---------------- ZONE
chips=lambda l:'<div class="zone-chips big">'+''.join(f'<span>{c}</span>' for c in l)+'</div>'
zone=f'''<section class="section s-ivory hero page-hero">
  <div class="wrap">
    <div class="trait" aria-hidden="true"></div>
    <div class="hero-grid">
      <div>
        <p class="eyebrow">Zone d’intervention</p>
        <h1>Dans toute l’<em>Essonne</em>, jusqu’à votre porte.</h1>
        <p class="lead">Atmosphère Paysage se déplace chez vous pour l’aménagement et l’entretien de votre jardin, depuis Gometz-la-Ville.</p>
        <div class="cta-row"><a class="btn" href="contact.html">Vérifier mon secteur</a><a class="btn ghost" href="tel:0669718436">06 69 71 84 36</a></div>
      </div>
      <div class="arch-wrap"><div class="arch"><img src="images/allee.jpg" width="900" height="491" alt="Allée dallée bordée d’un muret en pierre et de massifs, devant une maison" style="object-position:40% 50%"></div><div class="stamp"><b>Île-de-France</b>Essonne et alentours</div></div>
    </div>
  </div>
</section>

<section class="section s-forest s-curve on-dark" id="communes">
  <div class="wrap">
    <div class="reveal"><p class="eyebrow">Communes</p><h2>Nos secteurs d’intervention</h2>
    <p class="lead2">Nous intervenons notamment autour de ces communes, et dans tout l’Essonne :</p></div>
    {chips(['Gometz-la-Ville','Bures-sur-Yvette','Gif-sur-Yvette','Palaiseau','Saint-Rémy-lès-Chevreuse','Verrières-le-Buisson','Garches'])}
    <p class="reveal">Votre commune n’apparaît pas ? Appelez-nous : nous vous dirons si nous pouvons nous déplacer.</p>
  </div>
</section>

<section class="section s-sage s-curve" id="clients">
  <div class="wrap">
    <div class="reveal"><p class="eyebrow">Pour qui ?</p><h2>Chaque terrain,<br>chaque interlocuteur.</h2></div>
    <div class="steps three">
      <div class="step c-moss reveal">{I_HOME}<span class="n">Particuliers</span><h3>Votre jardin</h3><p>Aménagement, entretien et ouvrages pour la maison.</p></div>
      <div class="step c-olive reveal">{I_BUILD}<span class="n">Professionnels</span><h3>Vos espaces verts</h3><p>Un prestataire unique pour vos extérieurs.</p></div>
      <div class="step c-bark reveal">{I_LAND}<span class="n">Collectivités</span><h3>Vos communes</h3><p>Les représentants de collectivités peuvent aussi nous solliciter.</p></div>
    </div>
    <p class="note-line reveal">Dans tous les cas : visite sur place, état des lieux, puis devis gratuit.</p>
  </div>
</section>

<section class="section s-forest s-curve on-dark band-end">
  <div class="wrap band">
    <div><p class="eyebrow">Une question sur votre secteur ?</p><h2>Appelez-nous directement.</h2></div>
    <div class="band-actions"><a class="btn" href="tel:0669718436">06 69 71 84 36</a><a class="btn ghost" href="tel:0169769608">01 69 76 96 08</a></div>
  </div>
</section>'''

# ---------------- CONTACT
def field(i,label,inner,hint=''):
    return f'<div class="field"><label for="{i}">{label}</label>{inner}<p class="error" id="err-{i}" role="alert"></p></div>'
opts=['Aménagement paysager','Entretien de jardin','Abattage ou élagage','Terrasse, pergola ou carport','Maçonnerie (muret, bassin, allée)','Portail ou clôture','Contrat d’entretien annuel','Autre projet']
sel='<select id="besoin" name="besoin" required aria-describedby="err-besoin"><option value="">Choisir…</option>'+''.join(f'<option>{o}</option>' for o in opts)+'</select>'
contact=f'''<section class="section s-ivory hero page-hero contact-hero">
  <div class="wrap">
    <div class="trait" aria-hidden="true"></div>
    <div class="contact-grid">
      <div>
        <p class="eyebrow">Contact</p>
        <h1>Demandez votre <em>devis gratuit.</em></h1>
        <p class="lead">Dites-nous où vous êtes et ce que vous souhaitez : nous vous recontactons, puis nous nous déplaçons pour l’état des lieux.</p>
        <ul class="direct only-d">
          <li><a href="tel:0669718436">{I_PHONE}<span><small>Mobile</small>06 69 71 84 36</span></a></li>
          <li><a href="tel:0169769608">{PHONE_SVG}<span><small>Fixe</small>01 69 76 96 08</span></a></li>
          <li><div>{I_PIN}<span><small>Adresse</small>Gometz-la-Ville (91)</span></div></li>
        </ul>
      </div>
      <div class="form-card">
        <form id="devis" novalidate>
          <h2>Votre demande</h2>
          {field('nom','Nom','<input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="err-nom">')}
          {field('tel','Téléphone','<input id="tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" required placeholder="06 00 00 00 00" aria-describedby="err-tel">')}
          {field('commune','Commune du chantier','<input id="commune" name="commune" type="text" autocomplete="address-level2" required aria-describedby="err-commune">')}
          {field('besoin','Votre besoin',sel)}
          {field('message','Message (facultatif)','<textarea id="message" name="message" rows="3" aria-describedby="err-message"></textarea>')}
          <button class="btn full" type="submit">Préparer ma demande</button>
        </form>
        <div class="summary" id="summary" hidden tabindex="-1">
          <p class="ok">{ic('<path d="M10 25l9 9 19-20"/>')}<span>Demande prête. Envoyez-la en un geste :</span></p>
          <pre id="recap"></pre>
          <div class="sum-actions">
            <a class="btn" id="sms" href="sms:0669718436">Envoyer par SMS</a>
            <button class="btn ghost" type="button" id="copy">Copier</button>
            <a class="btn ghost" href="tel:0669718436">Appeler</a>
          </div>
          <p class="copied" id="copied" role="status"></p>
          <button class="link" type="button" id="edit">Modifier ma demande</button>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section s-bark s-curve on-dark band-end">
  <div class="wrap">
    <div class="reveal"><p class="eyebrow">Après votre demande</p><h2>Ce qui se passe ensuite.</h2></div>
    <ul class="direct only-m">
          <li><a href="tel:0669718436">{I_PHONE}<span><small>Mobile</small>06 69 71 84 36</span></a></li>
          <li><a href="tel:0169769608">{PHONE_SVG}<span><small>Fixe</small>01 69 76 96 08</span></a></li>
          <li><div>{I_PIN}<span><small>Adresse</small>Gometz-la-Ville (91)</span></div></li>
        </ul>
    <div class="steps three">
      <div class="step c-moss reveal">{I_PIN}<span class="n">1</span><h3>Nous venons chez vous</h3><p>État des lieux de votre jardin, sur place.</p></div>
      <div class="step c-olive reveal">{I_TREE}<span class="n">2</span><h3>Nous vous conseillons</h3><p>Des conseils pour réaliser votre projet.</p></div>
      <div class="step c-clay reveal">{I_BENCH}<span class="n">3</span><h3>Vous recevez un devis gratuit</h3><p>Puis les travaux, ou un contrat d’entretien annuel.</p></div>
    </div>
  </div>
</section>'''

pages={
 'prestations.html':('Prestations | Atmosphère Paysage, paysagiste à Gometz-la-Ville','Aménagement, entretien de jardin, menuiserie paysagère, maçonnerie, portails et clôtures : les prestations d’Atmosphère Paysage à Gometz-la-Ville (91).',pres),
 'zone.html':('Zone d’intervention | Atmosphère Paysage, Gometz-la-Ville','Atmosphère Paysage intervient dans tout l’Essonne depuis Gometz-la-Ville : Bures-sur-Yvette, Gif-sur-Yvette, Palaiseau et alentours.',zone),
 'contact.html':('Contact et devis gratuit | Atmosphère Paysage, Gometz-la-Ville','Contactez Atmosphère Paysage à Gometz-la-Ville (91) : 06 69 71 84 36 ou 01 69 76 96 08. Devis gratuit pour votre jardin.',contact),
}
for f,(t,d,b) in pages.items():
    open(f,'w',encoding='utf-8').write(page(f,t,d,b))
# accueil : en-tête et pied de page communs
s=open('index.html',encoding='utf-8').read()
s=re.sub(r'<header class="site-header">.*?</header>',lambda m:header('index.html'),s,flags=re.S)
s=re.sub(r'<footer class="site-footer">.*?</footer>',lambda m:FOOTER,s,flags=re.S)
open('index.html','w',encoding='utf-8').write(s)
print('ok')
