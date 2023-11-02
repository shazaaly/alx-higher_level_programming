$(document).ready(function () {
  // Your jQuery code goes here
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
