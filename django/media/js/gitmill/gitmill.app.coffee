gitmill.namespace 'gitmill.app', (exports) ->
  'use strict'

  app = exports.app = Ember.Application.create()
  app.Router.map ->
    @resource 'about'
