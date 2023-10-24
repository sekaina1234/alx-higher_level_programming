#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Usage: node 6-completed_tasks.js <API URL>');
} else {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      const todos = JSON.parse(body);

    
      const completedTasks = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completedTasks[todo.userId]) {
            completedTasks[todo.userId]++;
          } else {
            completedTasks[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasks);
    }
  });
}
