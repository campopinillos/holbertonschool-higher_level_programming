$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (responseText, statusText) => {
  if (statusText === 'success') {
    $('div#character').text(responseText.name);
  }
});
