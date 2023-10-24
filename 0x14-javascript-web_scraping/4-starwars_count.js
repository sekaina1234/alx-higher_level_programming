#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Usage: node 4-starwars_count.js <API URL>');
} else {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      const filmsData = JSON.parse(body);
      const wedgeAntillesFilms = filmsData.results
        .filter(film => film.characters.includes("https://swapi-api.alx-tools.com/api/people/18/"));

      console.log(wedgeAntillesFilms.length);
    }
  });
}
