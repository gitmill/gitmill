DIR = ../../static/css
GITMILL_TARGET = gitmill.css
GITMILL_SOURCES = \
	bootstrap/bootstrap.css \
	fontawesome/fontawesome.css \
	gitmill/gitmill.sass.css \

.PHONY: all
all: debug

.PHONY: debug
debug: $(DIR)/$(GITMILL_TARGET)

.PHONY: release
release: $(DIR)/$(GITMILL_TARGET)
	@cat $(GITMILL_TARGET) | sed 's/\/\*!/\/**/g' | yui-compressor --type css > $(DIR)/$(GITMILL_TARGET)

$(DIR)/$(GITMILL_TARGET): $(GITMILL_TARGET)
	@mkdir -p $(DIR)
	@cat $(GITMILL_TARGET) > $(DIR)/$(GITMILL_TARGET)

$(GITMILL_TARGET): $(GITMILL_SOURCES)
	@cat $(GITMILL_SOURCES) > $(GITMILL_TARGET)

%.sass.css: %.sass $(shell find . -type f -iname _\*.sass)
	@cat $< | sass --compass --load-path . > $<.css

.PHONY: clean
clean:
	@find . -iname \*.sass.css -exec rm -f {} \;
	@rm -rf .sass-cache
	@rm -f $(GITMILL_TARGET)
	@rm -rf $(DIR)

