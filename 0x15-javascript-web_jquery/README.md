0x15. JavaScript - Web jQuery

# JavaScript and jQuery Exercises

This repository contains a series of JavaScript and jQuery exercises that cover various tasks, from changing the text color of an HTML element to making API requests and updating the DOM. These exercises are meant to help you practice your web development skills and jQuery knowledge.

## Task List

1. **No jQuery - document loaded** - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000). You must use `document.querySelector` to select the HTML tag. You can't use the jQuery API.

2. **With jQuery** - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000). You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API.

3. **Click and turn red** - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag `DIV#red_header`. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API.

4. **Add `.red` class** - Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API.

5. **Toggle classes** - Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`. The `<header>` element must always have one class: `red` or `green`, never both at the same time and never empty. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API.

6. **List of elements** - Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`. The new element must be: `<li>Item</li>`. The new element must be added to `UL.my_list`. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API.

7. **Change the text** - Write a JavaScript script that updates the text of the `<header>` element to "New Header!!!" when the user clicks on `DIV#update_header`. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API.

8. **Star wars character** - Write a JavaScript script that fetches the character name from the URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`. The name must be displayed in the HTML tag `DIV#character`. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API.

9. **Star Wars movies** - Write a JavaScript script that fetches and lists the title for all movies using the URL: `https://swapi-api.alx-tools.com/api/films/?format=json`. All movie titles must be listed in the HTML tag `UL#list_movies`. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API.

10. **Say Hello!** - Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of "hello" from that fetch in the HTML tag `DIV#hello`. The translation of "hello" must be displayed in the HTML tag `DIV#hello`. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API. Your script must work when it is imported from the `<head>` tag.

11. **No jQuery - document loaded (Advanced)** - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000). You must use `document.querySelector` to select the HTML tag. You can't use the jQuery API. Note: Your script must be imported from the `<head>` tag, not at the end of the HTML.

12. **List, add, remove (Advanced)** - Write a JavaScript script that adds, removes, and clears LI elements from a list when the user clicks. The new element must be: `<li>Item</li>`. The new element must be added to `UL.my_list`. When the user clicks on `DIV#add_item`, a new element is added to the list. When the user clicks on `DIV#remove_item`, the last element is removed from the list. When the user clicks on `DIV#clear_list`, all elements of the list are removed. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API. Your script must work when imported from the `<head>` tag.

13. **Say hello to everybody! (Advanced)** - Write a JavaScript script that fetches and prints how to say "Hello" depending on the language. You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`. The language code will be the value entered in the tag `INPUT#language_code` (e.g., es, fr, en, etc.). The translation must be fetched when the user clicks on `INPUT#btn_translate` or presses ENTER when the focus is on `INPUT#language_code`. The translation of "Hello" must be displayed in the HTML tag `DIV#hello`. You can't use `document.querySelector` to select the HTML tag. You must use the jQuery API. Your script must work when imported from the `<head>` tag.

## Getting Started

To get started with any of these tasks, you can follow these general steps:

1. Clone this repository to your local machine:

2. Navigate to the task directory that you want to work on, e.g., `task-0-no-jquery`.

3. Open the HTML file (e.g., `index.html`) in your web browser to see the initial state and behavior.

4. Review the JavaScript file (e.g., `script.js`) to understand the task requirements and starter code.

5. Implement the necessary changes in the JavaScript file to achieve the task's objectives.

6. Test your solution by opening the HTML file in your browser.

7. Continue with the next task or exercise as needed.

## Prerequisites

You should have a basic understanding of HTML, JavaScript, and jQuery. Make sure you have a code editor and a web browser installed on your computer for testing.

Before starting, make sure you have a basic understanding of JavaScript and jQuery. If not, consider reviewing the following resources:
Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
How to select HTML elements in JavaScript
How to select HTML elements with JQuery
What are differences between ID, class and tag name selectors
How to modify an HTML element style
How to get and update an HTML element content
How to modify the DOM
How to make a GET request with JQuery Ajax
How to make a POST request with JQuery Ajax
How to listen/bind to DOM events