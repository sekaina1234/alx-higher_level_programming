$(document).ready(function() {
  $('#language_code').on('keypress', function(event) {
    if (event.which === 13) {
      translateHello();
    }
  });

  $('#btn_translate').click(translateHello);

  function translateHello() {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    });
  }
});
