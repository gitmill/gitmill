.PHONY: all
all: debug

.PHONY: debug
debug: html
	@cd media/css && make
	@cd media/js && make

.PHONY: release
release: html
	@cd media/css && make release
	@cd media/js && make release

.PHONY: html
html:
	@cd media/html && make

.PHONY: clean
clean:
	@cd media/html && make clean
	@cd media/css && make clean
	@cd media/js && make clean
	@find . -iname \*.pyc -delete
	@find . -iname \*~ -delete
	@find . -iname \*.mo -delete
