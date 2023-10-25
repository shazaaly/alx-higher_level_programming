#!/usr/bin/node

const url = 'https://jsonplaceholder.typicode.com/todos';
const request = require('request');
const userCompleted = {};

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    todos.forEach(todo => {
      if (todo.completed === true) {
        if (userCompleted[todo.userId] === undefined) {
          userCompleted[todo.userId] = 1;
        } else {
          userCompleted[todo.userId] += 1;
        }
      }
    });
    console.log(userCompleted);
  }
});
