import sys
sys.path.append('dblp-python/')
import dblp

import codecs
import yaml
import hashlib
import re

def run(directory):

	fin = open(directory+'/url.yml')
	urls = yaml.load(fin)
	fin.close()
	# fout.write('---\n')
	fdict = {}

	for url_id,url in urls.items():
		author = dblp.Author(url['url'].strip('\n'))
		name = author.name.split(' ')
		adict = {}

		print author.name
		for pub in author.publications:
			if pub.authors:
				hashcode = hashlib.sha224(unicode(pub)).hexdigest()
				first = pub.authors[0].split(' ')
				pdict = {}
				# fout.write('  id_publication_'+re.sub(r'[^a-zA-Z]','_',pub.title.lower())+':\n')
				pdict['hash'] = hashcode
				# fout.write('    hash: '+hashcode+'\n')
				pdict['title'] = pub.title.replace('\'','')
				# fout.write('    title: "'+pub.title.replace('\'','')+'"\n')
				pdict['authors'] = []
				# fout.write('    authors:\n')
				for pubAuthor in pub.authors:
					pdict['authors'].append(unicode(pubAuthor))
				# 	fout.write('    - '+pubAuthor+'\n')
				

				# fout.write('    booktitle:')
				if pub.booktitle:
					pdict['booktitle'] = unicode(pub.booktitle)
				# 	fout.write(' '+pub.booktitle)
				# fout.write('\n')

				# fout.write('    chapter:')
				if pub.chapter:
					pdict['chapter'] = unicode(pub.chapter)
				# 	fout.write(' '+pub.chapter)
				# fout.write('\n')

				# fout.write('    citations:')
				if pub.citations:
					pdict['citations'] = unicode(pub.citations)
				# 	fout.write(' "'+unicode(pub.citations)+'"')
				# fout.write('\n')

				# fout.write('    crossref:')
				if pub.crossref:
					pdict['crossref'] = unicode(pub.crossref)
				# 	fout.write(' "'+unicode(pub.crossref)+'"')
				# fout.write('\n')

				# fout.write('    editors:')
				if pub.editors:
					pdict['editors'] = unicode(pub.editors)
				# 	fout.write(' "'+unicode(pub.editors)+'"')
				# fout.write('\n')

				# fout.write('    ee:')
				if pub.ee:
					pdict['ee'] = unicode(pub.ee)
				# 	fout.write(' "'+pub.ee+'"')
				# fout.write('\n')

				# fout.write('    isbn:')
				if pub.isbn:
					pdict['isbn'] = unicode(pub.isbn)
				# 	fout.write(' "'+unicode(pub.isbn)+'"')
				# fout.write('\n')

				# fout.write('    journal:')
				if pub.journal:
					pdict['journal'] = unicode(pub.journal)
				# 	fout.write(' "'+pub.journal+'"')
				# fout.write('\n')

				# fout.write('    mdate:')
				if pub.mdate:
					pdict['mdate'] = unicode(pub.mdate)
				# 	fout.write(' "'+unicode(pub.mdate)+'"')
				# fout.write('\n')

				# fout.write('    month:')
				if pub.month:
					pdict['month'] = unicode(pub.month)
				# 	fout.write(' "'+unicode(pub.month)+'"')
				# fout.write('\n')

				# fout.write('    number:')
				if pub.number:
					pdict['number'] = unicode(pub.number)
				# 	fout.write(' "'+unicode(pub.number)+'"')
				# fout.write('\n')

				# fout.write('    pages:')
				if pub.pages:
					pdict['pages'] = unicode(pub.pages)
				# 	fout.write(' "'+unicode(pub.pages)+'"')
				# fout.write('\n')

				# fout.write('    publisher:')
				if pub.publisher:
					pdict['publisher'] = unicode(pub.publisher)
				# 	fout.write(' "'+unicode(pub.publisher)+'"')
				# fout.write('\n')

				# fout.write('    school:')
				if pub.school:
					pdict['school'] = unicode(pub.school)
				# 	fout.write(' "'+unicode(pub.school)+'"')
				# fout.write('\n')

				# fout.write('    series:')
				if pub.series:
					pdict['series'] = unicode(pub.series)
				# 	fout.write(' "'+unicode(pub.series)+'"')
				# fout.write('\n')

				# fout.write('    sub_type:')
				if pub.sub_type:
					pdict['sub_type'] = unicode(pub.sub_type)
				# 	fout.write(' "'+unicode(pub.sub_type)+'"')
				# fout.write('\n')

				# fout.write('    type:')
				if pub.type:
					pdict['type'] = unicode(pub.type)
				# 	fout.write(' "'+unicode(pub.type)+'"')
				# fout.write('\n')

				# fout.write('    url:')
				if pub.url:
					pdict['url'] = unicode(pub.url)
				# 	fout.write(' "'+unicode(pub.url)+'"')
				# fout.write('\n')

				# fout.write('    volume:')
				if pub.volume:
					pdict['volume'] = unicode(pub.volume)
				# 	fout.write(' "'+unicode(pub.volume)+'"')
				# fout.write('\n')

				# fout.write('    year:')
				if pub.year:
					pdict['year'] = unicode(pub.year)
				# 	fout.write(' "'+unicode(pub.year)+'"')
				# fout.write('\n')

				# fout.write('\n')

				adict['id_publication_'+re.sub(r'[^a-zA-Z]','_',pub.title.lower())] = pdict

			

		fdict['id_'+name[len(name)-1]+'_'+name[0]] = adict
		
		# fout.write('id_'+name[len(name)-1]+'_'+name[0]+':\n')

	fout = codecs.open(directory+'/publications.yml','w','utf-8')	
	out = yaml.dump(fdict,default_flow_style=False,default_style='"')
	fout.write(out)
	fout.close()




