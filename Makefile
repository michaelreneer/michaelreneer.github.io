INPUTDIR=$(CURDIR)/content
OUTPUTDIR=$(CURDIR)/output
PUBLISHDIR=$(CURDIR)/../master
CONFFILE=$(CURDIR)/pelicanconf.py
PUBLISHCONF=$(CURDIR)/publishconf.py
PUBLISHEXCLUDE=$(CURDIR)/excludes.txt

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make clean                       remove the generated files         '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make publish                     generate using production settings '
	@echo '                                                                       '

clean:
	find $(OUTPUTDIR) -mindepth 1 -delete

html: clean
	pelican $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)

regenerate: clean
	pelican -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)

serve:
	cd $(OUTPUTDIR) && python -m SimpleHTTPServer

publish:
	pelican $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF)
	rsync -rv --delete --exclude-from $(PUBLISHEXCLUDE) $(OUTPUTDIR)/ $(PUBLISHDIR)

.PHONY: help clean html regenerate serve publish
