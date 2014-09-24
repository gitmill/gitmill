debug.setLevel(9) if window.location.search is '?debug'

((window) ->
  'use strict'

  namespace = (target, name, block) ->
    [target, name, block] = [window, arguments...] if arguments.length < 3
    top = target
    target = target[item] or= {} for item in name.split '.'
    block target, top

  namespace 'gitmill', (exports, top) ->
    exports.namespace =  namespace

)(window)

gitmill.namespace 'gitmill.settings', (exports) ->
  'use strict'

  $('div.js-settings div').each ->
    key = $(@).data('key')
    value =  $(@).data('value')
    return if not key
    exports[key] = value
    debug.setLevel(9) if key is 'DEBUG' and value
    debug.info 'gitmill.settings.' + key, value
  $('div.js-settings').remove()


gitmill.namespace 'gitmill', (exports) ->
  'use strict'

  app = exports.app = Ember.Application.create()
  app.Router.reopen
    location: 'history'

  app.Router.map ->
    @resource 'about'
    @resource 'user',
      path: '/:username'
    @resource 'repository',
      path: '/:username/:name'

  app.ApplicationAdapter = DS.RESTAdapter.extend
    namespace: 'api'
