.PHONY: all service bundle spawn
SERVICE=sample_c

all: bundle

service:
	$(MAKE) -C src
	cp src/$(SERVICE) service/ro/

bundle: service
	rm -f ../$(SERVICE).tgz
	tar caf ../$(SERVICE).tgz *
	@echo "#### Double check ../$(SERVICE).tgz and submit it :) ####"

spawn: service
	( cd service/rw && socat tcp-l:6666,reuseaddr,fork exec:"../ro/$(SERVICE)" )
