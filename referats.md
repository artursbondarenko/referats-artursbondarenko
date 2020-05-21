---
title: "Mans Referats"
author: Arturs Bondarenko
date: "20-05-2020"
subject: "Python"
keywords: [Markdown, Example]
lang: "en"
subtitle: "Te bija jābūt nosaukumam"
titlepage: true
titlepage-color: "3C9F53"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFFFFF"
titlepage-rule-height: 2
...

# Pieslēdzam moduli un dabujam HTML saturu 

```python
from bs4 import BeautifulSoup
from urllib.request import *
```

Izmantojot modeli BeautifulSoup mēs apstradajam HTML. Dabujam to url un lasam visu ko satur vietne 

```python
def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html
```
## Dabujam bildes

Vispirms izveidojām funkciju kura palīdz mums ieiet vietne. Parsejam HTML lai dabūt bildes adressi. Pēc tam parējam uz "src" pec ID nosaukuma un lejupielādēt bildes

```python
def main():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    for i in range(1):
        html = get_html(url +str(i))
        soup = BeautifulSoup(html, 'html.parser')
        saraksts = soup.find_all(class_='preview')
        for a in saraksts:
            secondary_html = get_html(a['href'])
            secondary_soup = BeautifulSoup(secondary_html, 'html.parser')
            bilde = secondary_soup.find(id='wallpaper')['src']
            urlretrieve(bilde, "bilde.jpg"  )
            print('Download')
```

Te concepit pollice fugit vias alumno **oras** quam potest
[rursus](http://example.com#rursus) optat. Non evadere orbem equorum, spatiis,
vel pede inter si.

1. Punkts
2. Vel viens punkts
3. Un par bezmaksu vel vienu

\begin{equation}\label{eq:neighbor-propability}
    print("Hello World")
\end{equation}

Tamen condeturque saxa Pallorque num et ferarum promittis inveni lilia iuvencae
adessent arbor. Florente perque at condeturque saxa et ferarum promittis tendebat. Armos nisi obortas refugit me.

> Et nepotes poterat, se qui. Euntem ego pater desuetaque aethera Maeandri, et
[Dardanio geminaque](http://example.com#Dardanio_geminaque) cernit. Lassaque poenas
nec, manifesta $\pi r^2$ mirantia captivarum prohibebant scelerato gradus unusque
dura.

- Permulcens flebile simul
- Iura tum nepotis causa motus diva virtus Acrota. Tamen condeturque saxa Pallorque num et ferarum promittis inveni lilia iuvencae adessent arbor. Florente perque at ire arcum.