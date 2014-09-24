gitmill.namespace 'gitmill.user', (exports) ->
  'use strict'

  gitmill.app.User = DS.Model.extend
    username: DS.attr 'string'
    first_name: DS.attr 'string'
    last_name: DS.attr 'string'
    repositories: DS.hasMany('repository', async: true)

  gitmill.app.UserRoute = Ember.Route.extend
    model: (params) ->
      @store.find 'user', params.username

