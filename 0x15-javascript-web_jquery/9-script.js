$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',

    success: function (data) {
      console.log(data.hello);
      $('#hello').append(data.hello);
    },

    error: function (jqXHR, textStatus, errorThrown) {
      console.log('Error:', errorThrown);
    }
  });
});
