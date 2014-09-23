gitmill.namespace 'gitmill.ajax', (exports) ->
  'use strict'

  call = (method, func, data, callback) ->
    if data
      data =
        data: JSON.stringify(data)

    request = $.ajax
      type: method
      url: '/ajax' + func
      dataType: 'json'
      data: data or {}
      beforeSend: (xhr) ->
        xhr.setRequestHeader 'X-CSRFToken', $.cookie('csrftoken') if method is 'POST'

    request.done (data) ->
      callback data, {} if callback
      location.href = data.redirect if data and data.redirect and data.redirect.slice(0, 1) isnt "/"

    request.error (xhr, txt_status) ->
      return if not callback
      callback null,
        error: txt_status

  exports.get = (func, data, callback) -> call 'GET', func, data, callback
  exports.post = (func, data, callback) -> call 'POST', func, data, callback

