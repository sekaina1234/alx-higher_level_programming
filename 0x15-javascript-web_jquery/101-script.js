$(document).ready(function() {
  // Add item to the list
  $('#add_item').click(function() {
    $('ul.my_list').append('<li>Item</li>');
  });

  // Remove the last item from the list
  $('#remove_item').click(function() {
    $('ul.my_list li:last-child').remove();
  });

  // Clear the entire list
  $('#clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
