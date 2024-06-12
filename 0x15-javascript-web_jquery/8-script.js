$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        const movies = data.results;
        movies.forEach(function(movie) {
            $('<li></li>').text(movie.title).appendTo('#list_movies');
        });
    });
});
