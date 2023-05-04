#!/usr/bin/node

const request = require('request');

const movies = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movies;
let person = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(filmEndPoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      person = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (person.length > 0) {
    for (const q of person) {
      await new Promise(resolve => request(q, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const i of names) {
    if (i === names[names.length - 1]) {
      process.stdout.write(i);
    } else {
      process.stdout.write(i + '\n');
    }
  }
};

getCharNames();
