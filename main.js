let tickers = [];

function graph() {
    var settings = {
        'url': 'http://23.254.164.217:5000/compare',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': '*/*',
        },
        'data': '{"stocks":["' + tickers.join("\",\"") + '"]}'
    }
      
    $.ajax(settings).done(function (response) {
        $('#graph').attr('src',"results.png?" + new Date().getTime());
        console.log(response)
    });
}

function addTicker() {
    $('#tickers-list').append('<li>' + $('#ticker-input').val() + '</li>');
    tickers.push($('#ticker-input').val());
    $('#ticker-input').val('')
}