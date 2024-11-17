#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
    console.error('Missing movie ID');
    process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error('Error fetching data:', error);
        return;
    }

    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error('Error fetching character:', error);
                return;
            }

            const character = JSON.parse(body);
            console.log(character.name);
        });
    });
});
