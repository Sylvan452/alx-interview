#!/usr/bin/node

const axios = require('axios');

if (process.argv.length > 2) {
  const filmId = process.argv[2];
  const API_URL = `https://swapi.dev/api/films/${filmId}/`;

  axios.get(API_URL)
    .then(response => {
      const charactersURL = response.data.characters;
      const characterPromises = charactersURL.map(url => axios.get(url));

      Promise.all(characterPromises)
        .then(responses => {
          const characterNames = responses.map(response => response.data.name);
          console.log(characterNames.join('\n'));
        })
        .catch(error => {
          console.error(error);
        });
    })
    .catch(error => {
      console.error(error);
    });
}
