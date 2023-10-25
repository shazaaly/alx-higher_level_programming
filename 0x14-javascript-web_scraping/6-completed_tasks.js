#!/usr/bin/node

const url = 'https://jsonplaceholder.typicode.com/todos';
const request = require('request');
let users_completed = {};

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const todos = JSON.parse(body);
  todos.forEach(todo => {

    if (todo.completed === true) {
      if (users_completed[todo.userId] === undefined) {
        users_completed[todo.userId] = 1;
      }else {
        users_completed[todo.userId]++;
      }
    }
  });
  console.log(users_completed);
});
