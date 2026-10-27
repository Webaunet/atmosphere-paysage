(function () {
  var b = document.querySelector('.burger'), n = document.getElementById('nav');
  if (b && n) {
    var set = function (o) { b.setAttribute('aria-expanded', o); n.classList.toggle('open', o); b.setAttribute('aria-label', o ? 'Fermer le menu' : 'Ouvrir le menu'); };
    b.addEventListener('click', function () { set(b.getAttribute('aria-expanded') !== 'true'); });
    n.addEventListener('click', function (e) { if (e.target.closest('a')) set(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { set(false); b.focus(); } });
    window.addEventListener('resize', function () { if (window.innerWidth > 980) set(false); });
  }
  var r = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: .12 });
    r.forEach(function (el) { io.observe(el); });
  } else { r.forEach(function (el) { el.classList.add('in'); }); }
})();

(function () {
  var f = document.getElementById('devis');
  if (!f) return;
  var sum = document.getElementById('summary'), recap = document.getElementById('recap');
  var rules = {
    nom: function (v) { return v.trim().length < 2 ? 'Indiquez votre nom.' : ''; },
    tel: function (v) { return /^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.\-]*\d{2}){4}$/.test(v.trim()) ? '' : 'Indiquez un numéro valide, par exemple 06 00 00 00 00.'; },
    commune: function (v) { return v.trim().length < 2 ? 'Indiquez la commune du chantier.' : ''; },
    besoin: function (v) { return v ? '' : 'Choisissez votre besoin.'; }
  };
  function check(id) {
    var el = document.getElementById(id), msg = rules[id] ? rules[id](el.value) : '';
    document.getElementById('err-' + id).textContent = msg;
    el.setAttribute('aria-invalid', msg ? 'true' : 'false');
    return !msg;
  }
  Object.keys(rules).forEach(function (id) { document.getElementById(id).addEventListener('blur', function () { check(id); }); });
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var ok = true, first = null;
    Object.keys(rules).forEach(function (id) { if (!check(id)) { ok = false; first = first || document.getElementById(id); } });
    if (!ok) { first.focus(); return; }
    var v = function (id) { return document.getElementById(id).value.trim(); };
    var t = 'Demande de devis - Atmosphère Paysage\nNom : ' + v('nom') + '\nTéléphone : ' + v('tel') + '\nCommune : ' + v('commune') + '\nBesoin : ' + v('besoin') + (v('message') ? '\nMessage : ' + v('message') : '');
    recap.textContent = t;
    document.getElementById('sms').href = 'sms:0669718436?&body=' + encodeURIComponent(t);
    f.hidden = true; sum.hidden = false; sum.focus();
  });
  document.getElementById('copy').addEventListener('click', function () {
    var t = recap.textContent, c = document.getElementById('copied');
    var done = function () { c.textContent = 'Demande copiée.'; };
    if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(t).then(done, function () { c.textContent = 'Copie impossible : sélectionnez le texte.'; }); }
    else { var r = document.createRange(); r.selectNodeContents(recap); var s = getSelection(); s.removeAllRanges(); s.addRange(r); try { document.execCommand('copy'); done(); } catch (x) { c.textContent = 'Copie impossible : sélectionnez le texte.'; } }
  });
  document.getElementById('edit').addEventListener('click', function () { sum.hidden = true; f.hidden = false; document.getElementById('nom').focus(); });
})();
