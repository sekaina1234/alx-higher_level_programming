#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node 3-starwars_title.js <movie-id>');
} else {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    }
  });
}
