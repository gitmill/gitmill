DIR = ../../static/js
GITMILL_TARGET = gitmill.js
GITMILL_SOURCES = \
	debug.js \
	jquery/jquery.js \
	jquery/jquery.cookie.coffee.js \
	handlebars.js \
	ember.js \
	moment.js \
	bootstrap/bootstrap.js \
	gitmill/gitmill.coffee.js \
	gitmill/gitmill.locale.coffee.js \
	gitmill/gitmill.utils.coffee.js \
	gitmill/gitmill.ajax.coffee.js \
	gitmill/gitmill.app.coffee.js \

.PHONY: all
all: debug

.PHONY: debug
debug: $(DIR)/$(GITMILL_TARGET)

.PHONY: release
release: $(DIR)/$(GITMILL_TARGET)
	@cat $(GITMILL_TARGET) | sed 's/\/\*!/\/**/g' | yui-compressor --type js > $(DIR)/$(GITMILL_TARGET)

$(DIR)/$(GITMILL_TARGET): $(GITMILL_TARGET)
	@mkdir -p $(DIR)
	@cat $(GITMILL_TARGET) > $(DIR)/$(GITMILL_TARGET)

$(GITMILL_TARGET): $(GITMILL_SOURCES)
	@cat $(GITMILL_SOURCES) > $(GITMILL_TARGET)

%.coffee.js: %.coffee
	@cat $< | coffee -c -s > $<.js

.PHONY: clean
clean:
	@find . -iname \*.coffee.js -exec rm -f {} \;
	@rm -f $(GITMILL_TARGET)
	@rm -rf $(DIR)

