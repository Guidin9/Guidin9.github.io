// Theme toggle, header rule on scroll, and the contact form's "sent" notice.
(function () {
  var root = document.documentElement;

  function systemDark() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  function currentTheme() {
    return root.getAttribute('data-theme') || (systemDark() ? 'dark' : 'light');
  }

  var toggle = document.querySelector('[data-theme-toggle]');
  if (toggle) {
    var labels = { dark: toggle.getAttribute('data-label-light'), light: toggle.getAttribute('data-label-dark') };
    var metas = document.querySelectorAll('meta[name="theme-color"]');
    var sync = function () {
      var theme = currentTheme();
      toggle.setAttribute('aria-label', labels[theme]);
      // A manual choice overrides the media-matched theme-color pair.
      if (root.hasAttribute('data-theme')) {
        for (var i = 0; i < metas.length; i++) metas[i].setAttribute('content', theme === 'dark' ? '#0c1621' : '#f3f5f7');
      }
    };
    sync();
    if (window.matchMedia) {
      var mq = window.matchMedia('(prefers-color-scheme: dark)');
      if (mq.addEventListener) mq.addEventListener('change', sync);
    }
    toggle.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
      sync();
    });
  }

  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  var notice = document.querySelector('[data-sent]');
  if (notice && /[?&]success=true/.test(window.location.search)) {
    notice.hidden = false;
    if (window.history && history.replaceState) {
      history.replaceState(null, '', window.location.pathname + window.location.hash);
    }
  }
})();
