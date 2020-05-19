const url = 'https://www.fourtonfish.com/hellosalut/?';

$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), (data, textStatus) => {
      if (textStatus === 'success') {
        $('DIV#hello').html(data.hello);
      }
    });
  });
});
