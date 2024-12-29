#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first positional argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Define the API URL for the specified movie ID
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch movie details (Status Code: ${response.statusCode})`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  // Fetch and print character names in order
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      if (charResponse.statusCode === 200) {
        const character = JSON.parse(charBody);
        console.log(character.name);
      } else {
        console.error(`Error fetching character: ${charResponse.statusCode}`);
      }
    });
  });
});
