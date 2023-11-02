$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',

    success: function (data) {
      let items = data.results;
      for (let index = 0; index < items.length; index++) {
        let title = items[index].title;
        $('ul#list_movies').append('<li>' + title + '</li>');
      }
    },

    error: function (jqXHR, textStatus, errorThrown) {
      console.log('Error:', errorThrown);
    }
  });
});
