import dblppy
import codecs
import yaml
import hashlib
import re

fin = open('../_data/url.yml')
urls = yaml.load(fin)
fout = codecs.open('publications.yml', 'w', 'utf-8')
fout.write('---\n')

for url_id, url in urls.items():
    author = dblppy.Author(url['url'].strip('\n'))
    name = author.name.split(' ')
    fout.write('id_' + name[len(name) - 1] + '_' + name[0] + ':\n')
    print author.name
    for pub in author.publications:
        if pub.authors:
            hashcode = hashlib.sha224(str(pub)).hexdigest()
            first = pub.authors[0].split(' ')
            fout.write('  id_publication_' + re.sub(r'[^a-zA-Z]', '_', pub.title.lower()) + ':\n')
            fout.write('    hash: ' + hashcode + '\n')
            fout.write('    title: "' + pub.title.replace('\'', '') + '"\n')
            fout.write('    authors:\n')
            for pubAuthor in pub.authors:
                fout.write('    - ' + pubAuthor + '\n')

            fout.write('    booktitle:')
            if pub.booktitle:
                fout.write(' ' + pub.booktitle)
            fout.write('\n')

            fout.write('    chapter:')
            if pub.chapter:
                fout.write(' ' + pub.chapter)
            fout.write('\n')

            fout.write('    citations:')
            if pub.citations:
                fout.write(' "' + str(pub.citations) + '"')
            fout.write('\n')

            fout.write('    crossref:')
            if pub.crossref:
                fout.write(' "' + str(pub.crossref) + '"')
            fout.write('\n')

            fout.write('    editors:')
            if pub.editors:
                fout.write(' "' + str(pub.editors) + '"')
            fout.write('\n')

            fout.write('    ee:')
            if pub.ee:
                fout.write(' "' + pub.ee + '"')
            fout.write('\n')

            fout.write('    isbn:')
            if pub.isbn:
                fout.write(' "' + str(pub.isbn) + '"')
            fout.write('\n')

            fout.write('    journal:')
            if pub.journal:
                fout.write(' "' + pub.journal + '"')
            fout.write('\n')

            fout.write('    mdate:')
            if pub.mdate:
                fout.write(' "' + str(pub.mdate) + '"')
            fout.write('\n')

            fout.write('    month:')
            if pub.month:
                fout.write(' "' + str(pub.month) + '"')
            fout.write('\n')

            fout.write('    number:')
            if pub.number:
                fout.write(' "' + str(pub.number) + '"')
            fout.write('\n')

            fout.write('    pages:')
            if pub.pages:
                fout.write(' "' + str(pub.pages) + '"')
            fout.write('\n')

            fout.write('    publisher:')
            if pub.publisher:
                fout.write(' "' + str(pub.publisher) + '"')
            fout.write('\n')

            fout.write('    school:')
            if pub.school:
                fout.write(' "' + str(pub.school) + '"')
            fout.write('\n')

            fout.write('    series:')
            if pub.series:
                fout.write(' "' + str(pub.series) + '"')
            fout.write('\n')

            fout.write('    sub_type:')
            if pub.sub_type:
                fout.write(' "' + str(pub.sub_type) + '"')
            fout.write('\n')

            fout.write('    type:')
            if pub.type:
                fout.write(' "' + str(pub.type) + '"')
            fout.write('\n')

            fout.write('    url:')
            if pub.url:
                fout.write(' "' + str(pub.url) + '"')
            fout.write('\n')

            fout.write('    volume:')
            if pub.volume:
                fout.write(' "' + str(pub.volume) + '"')
            fout.write('\n')

            fout.write('    year:')
            if pub.year:
                fout.write(' "' + str(pub.year) + '"')
            fout.write('\n')

            fout.write('\n')

fin.close()
fout.close()




