# mertdemirdoven.me

Source of my personal site: projects, internship, CV and contact. Served by GitHub Pages at
[mertdemirdoven.me](https://mertdemirdoven.me).

- `index.html` is Turkish, `en/index.html` is English. Both share `assets/css/site.css` and
  `assets/js/site.js`.
- Plain HTML and CSS, no build step. Fonts: Archivo from Google Fonts.
- `assets/Cv/` holds the CV in Turkish (`Mert_Demirdoven_CV.pdf`) and English
  (`Mert_Demirdoven_CV_EN.pdf`). Both are generated: edit `_cv/cv.py`, then run
  `powershell -ExecutionPolicy Bypass -File _cv\build.ps1` (needs Python and Chrome).
  Jekyll skips folders that start with `_`, so `_cv/` is not published.
- `/restoranmanage` redirects to the RestoranManage demo.

To preview locally:

```sh
python -m http.server 8000
```

then open http://localhost:8000.
