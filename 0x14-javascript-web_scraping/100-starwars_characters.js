#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node 100-starwars_characters.js <Movie ID>');
} else {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error(characterError);
          } else if (characterResponse.statusCode !== 200) {
            console.error(`Character request failed with status code: ${characterResponse.statusCode}`);
          } else {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
          }
        });
      });
    }
  });
}
