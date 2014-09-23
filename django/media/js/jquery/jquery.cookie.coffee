(($) ->
  'use strict'

  pluses = /\+/g

  raw = (s) -> s

  decoded = (s) ->
    decodeURIComponent s.replace pluses, ' '
 
  $.cookie = (key, value, options) ->   

    # key and at least value given, set cookie...
    if value isnt `undefined` and not /Object/.test(Object::toString.call(value))
      options = $.extend {}, $.cookie.defaults, options

      if value is null
        options.expires = -1
        value = ''

      if typeof options.expires is 'number'
        days = options.expires
        t = options.expires = new Date()
        t.setDate t.getDate() + days

      value = String(value)

      # use expires attribute, max-age is not supported by IE
      cookie = [
        encodeURIComponent(key), '=', (if options.raw then value else encodeURIComponent(value)),
        (if options.expires then '; expires=' + options.expires.toUTCString() else ''),
        (if options.path then '; path=' + options.path else ''),
        (if options.domain then '; domain=' + options.domain else ''),
        (if options.secure then '; secure' else '')
      ].join ''
      debug.debug 'jquery.cookie', cookie

      return (document.cookie = cookie)

    # key and possibly options given, get cookie...
    options = value or $.cookie.defaults or {}
    decode = (if options.raw then raw else decoded)

    for cookie in document.cookie.split '; '
      parts = cookie and cookie.split '='
      if decode(parts.shift()) is key
        return decode parts.join '='
    return null

  $.cookie.defaults =
    path: '/'

) jQuery

