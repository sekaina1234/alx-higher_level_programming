$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    var movies = data.results;

    for (var i = 0; i < movies.length; i++) {
      var title = movies[i].title;
      $('#list_movies').append('<li>' + title + '</li>');
    }
  });
});
