#!/usr/bin/env python3
"""
Tohle je skript pro stahovani webu.

Autor: XXX

Priklad pouziti:

  ./scraper_cli.py --starting-url https://www.smartprague.eu/aktuality/
                   --link-selektor a.tile
                   --nadpis-selektor ".jumbotron h1"

"""

from dateutil.parser import parse
from bs4 import BeautifulSoup
import requests
import sys
import os.path as op
import csv
from urllib.parse import urljoin


# -----------------------------------------------------------------------------
# NADPIS
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------

def main():
    output_path = "myfile.csv"
    # Tohle budeme měnit!
    # starting_url = "https://www.smartprague.eu/aktuality/"
    # link_selektor = "a.tile"
    # nadpis_selektor = ".jumbotron h1"
    # fulltext_selektor = ".col-lg-10 p"
    starting_url = "https://www.6dhub.cz"
    link_selektor = "div.article_tile a"
    nadpis_selektor = "div.container h1"
    fulltext_selektor = "div.single__body p"

    starting_url = "https://www.komora.cz/aktuality/"
    link_selektor = ".main-content article h2 a"
    nadpis_selektor = ".headline h1"
    fulltext_selektor = "div.content p"

    starting_url = "https://www.eduin.cz/blogy"
    link_selektor = "h1.entry-title a"
    nadpis_selektor = "h2.page-title"
    fulltext_selektor = ".content p"

if output_path:
        print("mam ukladat do souboru", output_path)
    else:
        print("mam printovat do konzole, ale to neni implementovano")
        return 1
    # -------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------
    list_pro_analyzu, data_list = [], []  # type: list[dict]

    odkazy = najdi_odkazy(starting_url, link_selektor)
    odkazy = odkazy[:15]  # XXX omezim se na min clanku abych toho tolik nestahoval
    for url in odkazy:
        vystup_ze_stranky = {}

        html = stahni_html(url)

        if fulltext_selektor:
            fulltext = najdi_selektorem(html, fulltext_selektor)
        else:
            fulltext = None  # nezadal jsem fulltext_selector, tak se to nestazim nacist ze stranky
        nadpis = najdi_selektorem(html, nadpis_selektor)
        data_list.append(dict(url=url, nadpis=nadpis, fulltext=fulltext))
        list_pro_analyzu.append((nadpis, fulltext))

    for article in data_list:
        print(article)
    # print("zapisuji do souboru", output_path)
    # zapis_do_souboru(data_list, output_path)

    print("hotovo")
    return 0


def stahni_html(starting_url):
    """
        Tohle stahuje cosi

        Example:


        """
    r = requests.get(starting_url)
    if r.status_code != 200:
        raise RuntimeError("odkaz %s vratil status %d" % (starting_url, r.status_code))
    html = r.text

    return html


# -----------------------------------------------------------------------------

def najdi_odkazy(starting_url, link_selektor):
    html = stahni_html(starting_url)
    soup = BeautifulSoup(html, "html.parser")
    link_selektorem_list = []
    for a_elem in soup.select(link_selektor):
        href = urljoin(starting_url, a_elem["href"])

        link_selektorem_list.append(href)

    return link_selektorem_list


def najdi_selektorem(html, selektor) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    nalezene_texty = []

    for elem in soup.select(selektor):
        text = elem.text
        nalezene_texty.append(text)

    return " ".join(nalezene_texty)


def zapis_do_souboru(data_list, output_path):
    fieldnames = ["url", "nadpis", "fulltext"]  # xxx doplněn perex

    with open(output_path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames, delimiter=',')
        writer.writeheader()
        for row_dict in data_list:
            writer.writerow(row_dict)
    return writer


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    sys.exit(main())