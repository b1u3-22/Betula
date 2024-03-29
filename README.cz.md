<p align="center">
    <img src="assets/readme_banner.png"/>
</p>
<p align="center">
  <img src="https://img.shields.io/tokei/lines/github/b1u3-22/betula?label=počet řádků&style=flat-square">
  <img src="https://img.shields.io/github/last-commit/b1u3-22/betula?label=poslední commit&style=flat-square">
  <img src="https://img.shields.io/codacy/grade/0d411bbe46ec4c7598650cfd9668aadf?label=známka&style=flat-square">
  <img src="https://img.shields.io/github/repo-size/b1u3-22/betula?label=velikost repozitáře&style=flat-square">
</p>
<p align="center">
    English version can be found
    <a href="README.md"> here</a>
</p>
<p align="center">
    <b>Moderní, Opensource a lehce přístupný systém pro bytová družstva</b>
</p>
<p align="center">
    <a href="#přehled--">Přehled</a>
    •
    <a href="#funkce--">Funkce</a>
    •
    <a href="#instalace--">Instalace</a>
    •
    <a href="#demo--">Demo</a>
    •
    <a href="#screenshoty--">Screenshoty</a>
</p>

## Přehled :book:
Betula je informační systém pro bytová družstva. Vytváří prostor pro sdílení informací nejen se širokým světem, ale také pouze se členy daného družstva.

## Funkce :dizzy:
### Hlavní stránka
Na hlavní stránce se zobrazují především kontakní informace jako email, adresa a telefonní čísla \
Dále se zde nachází malá galerie se třemi obrázky a krátkým popisem

### Galerie
Celá galerie zobrazující veškeré obrázky, které do informačního systému nahrajete \
K fotkám lze také přidat krátký popis

### Systém
Samotný systém, kam se už dostanou pouze uživatelé. Zobrazují se zde informace o financích jako zůstatek na účtu a status půjček \
Samozřejmě zde uživatelé také vidí příspěvky, které mohou přidávat správci

### Nastavení
Celý systém lze nastavit právě z této stránky \
Změny mohou provádět ppouze správci a lze změnit následující:
* Hlavní stránka
    * Emaily
    * Telefonní čísla
    * Obrázek na pozadí
    * Popis
    * Obrázky malé galerie
* Galerie
      * Fotky
      * Informace o fotkách
* Systémová stránka
    * Stav účtu
    * Správa půjček
        * Přidání nebo odebrání
        * Zbývající částky
        * Měsíční splátka
    * Správa uživatelů
        * Přidání a odebrání
        * Změna hesla 
        * Email
        * Oprávnění

## Instalace :cd:
Betulu lze nainstalovat pomocí **Dockeru** :whale2: použitím jedné z automaticky postavených image
*(Pokud si zvolíte image s tagem **latest**, prosím dejte pozor na to, že tyto vydání mohou obsahovat škodlivé změny. Proto doporučuji používat image s tagem **stable**)*

### Instalace pomocí `docker-compsose`
```docker
version: "3.4"
services:
  betula:
    image: /b1u322/betula:stable # nebo /b1u322/betula:latest
    container_name: betula
    ports:
      - 80:80
    volumes:
      betula_config:/config
      betula_images:/images
    restart: unless-stopped
```

## Demo :house:
> Bude přidáno

## Obrázky :framed_picture:
> Bude přidáno