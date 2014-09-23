gitmill.namespace 'gitmill.locale', (exports) ->
  'use strict'

  exports.set = (locale) ->
    return if locale == gitmill.settings.LOCALE
    $.cookie 'locale', locale,
      expires: 365
    window.location.reload(true)
