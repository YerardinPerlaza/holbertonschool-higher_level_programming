#!/usr/bin/node

require('request').get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      require('request').get(character, function (err, resp, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
