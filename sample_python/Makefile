.PHONY: all service bundle spawn
SERVICE=sample_py

all: bundle

service:
	cp src/$(SERVICE) service/ro/

bundle: service
	rm -f ../$(SERVICE).tgz
	tar caf ../$(SERVICE).tgz *
	@echo "#### Double check ../$(SERVICE).tgz and submit it :) ####"

spawn: service
	( cd service/rw && socat tcp-l:6666,reuseaddr,fork exec:"../ro/$(SERVICE)" )
