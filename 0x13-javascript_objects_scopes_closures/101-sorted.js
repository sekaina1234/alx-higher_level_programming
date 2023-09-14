#!/usr/bin/node

const data = require('./101-data').dict;

const reversedData = {};

for (const key in data) {
  if (data.hasOwnProperty(key)) {
    const occurrence = data[key].toString();
    if (!reversedData[occurrence]) {
      reversedData[occurrence] = [];
    }
    reversedData[occurrence].push(key);
  }
}

console.log(reversedData);
