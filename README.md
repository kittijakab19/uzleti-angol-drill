# Üzleti angol drill

Gyakorlóoldal az üzleti angol jegyzet (Topic 1–5) szószedetéből és tananyagszövegéből.

- **Gyakorlás** – kiegészítős és feleletválasztós kérdések a szótári példamondatokból, a definíciókból és a magyar jelentésekből; `i` gombbal magyar tipp.
- **Szókincs kártyák** – párosítós játék: angol szó ↔ angol leírás, vagy angol szó ↔ magyar jelentés, 4–30 párig.
- **Szókincs** – mind a 479 szócikk (kiejtés, szófaj, definíció, kollokációk, példamondat), magyar fordítással az `i` gomb mögött.
- **Szókincs → Tesztelés** – beírós teszt a szűrt szólistából, választható iránnyal: magyar jelentésből angol szó, vagy angol szóból magyar jelentés.
- **Leírások** – a jegyzet teljes szövege témakörönként, bekezdésenként előhívható magyar fordítással.
- **Haladás** – találati arány, témakörönkénti bontás, nehéz szavak külön gyakorlása. Az eredmény a böngésződben tárolódik.

## Használat

Online: a GitHub Pages cím (Settings → Pages → Branch: `main`, mappa: `/`).

Helyben:

```bash
python3 serve.py       # http://localhost:8931/index.html, telefonról is a helyi hálózatról
```

Vagy nyisd meg dupla kattintással az `uzleti-angol-drill.html` fájlt – abban minden adat benne van, internet nélkül is működik.

## Keresők

Minden oldal `<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">` fejlécet kap, így a Google és a többi kereső nem indexeli. A `robots.txt` szándékosan engedi a bejárást, különben a keresők nem látnák magát a noindex utasítást.

## Fájlok

| fájl | mit tartalmaz |
| --- | --- |
| `index.html` | az oldal (adat nélkül) |
| `data.js` | 479 szócikk + 525 bekezdésnyi tananyagszöveg, magyar fordításokkal |
| `uzleti-angol-drill.html` | egyfájlos, offline változat |
| `serve.py`, `start.command` | helyi webszerver |
| `page-source.html`, `make-standalone.py` | forrás és a build script az egyfájlos változathoz |
