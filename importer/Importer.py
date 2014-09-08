import dblp

import codecs
import yaml
import hashlib
import re
import lxml
import time


def run(directory):

    fin = open(directory + '/url.yml')
    urls = yaml.load(fin)
    fin.close()
    # fout.write('---\n')
    fdict = {}

    for url_id, url in urls.items():
        try:
            author = dblp.Author(url['url'].strip('\n'))
            name = author.name.split(' ')
            adict = {}

            print author.name
            # for pub in author.publications:
            for i in range(len(author.publications)):
                try:
                    pub = author.publications[i]
                    if pub.authors:
                        hashcode = hashlib.sha224(unicode(pub)).hexdigest()
                        first = pub.authors[0].split(' ')
                        pdict = {}
                        pdict['hash'] = hashcode
                        pdict['title'] = pub.title.replace('\'', '')
                        pdict['authors'] = []
                        for pubAuthor in pub.authors:
                            pdict['authors'].append(unicode(pubAuthor))
                        if pub.booktitle:
                            pdict['booktitle'] = unicode(pub.booktitle)
                        if pub.chapter:
                            pdict['chapter'] = unicode(pub.chapter)
                        if pub.citations:
                            pdict['citations'] = unicode(pub.citations)
                        if pub.crossref:
                            pdict['crossref'] = unicode(pub.crossref)
                        if pub.editors:
                            pdict['editors'] = unicode(pub.editors)
                        if pub.ee:
                            pdict['ee'] = unicode(pub.ee)
                        if pub.isbn:
                            pdict['isbn'] = unicode(pub.isbn)
                        if pub.journal:
                            pdict['journal'] = unicode(pub.journal)
                        if pub.mdate:
                            pdict['mdate'] = unicode(pub.mdate)
                        if pub.month:
                            pdict['month'] = unicode(pub.month)
                        if pub.number:
                            pdict['number'] = unicode(pub.number)
                        if pub.pages:
                            pdict['pages'] = unicode(pub.pages)
                        if pub.publisher:
                            pdict['publisher'] = unicode(pub.publisher)
                        if pub.school:
                            pdict['school'] = unicode(pub.school)
                        if pub.series:
                            pdict['series'] = unicode(pub.series)
                        if pub.sub_type:
                            pdict['sub_type'] = unicode(pub.sub_type)
                        if pub.type:
                            pdict['type'] = unicode(pub.type)
                        if pub.url:
                            pdict['url'] = unicode(pub.url)
                        if pub.volume:
                            pdict['volume'] = unicode(pub.volume)
                        if pub.year:
                            pdict['year'] = unicode(pub.year)

                        adict['id_publication_' + pub.url] = pdict
                        time.sleep(0.5)
                        # adict['id_publication_'+re.sub(r'[^a-zA-Z]','_',pub.title.lower())]
                        # = pdict
                except lxml.etree.XMLSyntaxError:
                    print i
                    break
        except lxml.etree.XMLSyntaxError:
            print url
            continue

        # use the full name of the people as the id
        fdict['id_' + name[len(name) - 1].lower() + '_' + name[0].lower()] = adict

    fout = codecs.open(directory + '/publications.yml', 'w', 'utf-8')
    out = yaml.dump(fdict, default_flow_style=False, default_style='"')
    fout.write(out)
    fout.close()
