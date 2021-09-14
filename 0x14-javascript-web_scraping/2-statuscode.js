#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (error, r) {
  if (error) {
    console.log(error);
  }
  console.log('code: ' + r.statusCode);
});
