let tickers = [];
let timeRanges = ['5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'];

function graph() {
    let data = {}
    data.stocks = tickers;
    data.time = timeRanges[$('#time-slider').val()];
    var settings = {
        'url': 'http://23.254.164.217:5000/compare',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': '*/*',
        },
        'data': JSON.stringify(data)
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

function sliderUpdate(){
    $('#time-label').html(timeRanges[$('#time-slider').val()])
}
