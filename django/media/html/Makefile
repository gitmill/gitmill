DIR = ../../template
SOURCES = $(shell find . -type f -not -name .\* -name \*.haml)
TARGETS = $(patsubst ./%.haml, $(DIR)/%, $(SOURCES))

.PHONY: all
all: $(TARGETS)

$(DIR)/%: %.haml
	@mkdir -p `dirname $@`
	@rm -f $@
	@echo "$< => $@"
	@haml -t ugly -q $< $@

.PHONY: clean
clean:
	@rm -rf $(DIR)
