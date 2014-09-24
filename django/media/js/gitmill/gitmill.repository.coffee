gitmill.namespace 'gitmill.repository', (exports) ->
  'use strict'

  gitmill.app.Repository = DS.Model.extend
    username: DS.attr 'string'
    name: DS.attr 'string'
    description: DS.attr 'string'
    user: DS.belongsTo('user', async: true)

  gitmill.app.RepositoryRoute = Ember.Route.extend
    model: (params) ->
      @store.find 'repository', params.username + '/' + params.name

