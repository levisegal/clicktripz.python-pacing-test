IMAGE = clicktripz/python-test
MOUNTDIRECTORY = /sample
.PHONY: run build tty

build:
	docker build --rm -t $(IMAGE) .

tests:
	docker run -v $(PWD):$(MOUNTDIRECTORY) -it --rm $(IMAGE) dumb-init python /sample/tests.py

tty:
	docker run -v $(PWD):$(MOUNTDIRECTORY) -it --rm $(IMAGE) dumb-init /bin/bash