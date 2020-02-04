let tickers = [];
let periods = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'];
let intervals = ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'];

function graph() {
    let data = {}
    data.stocks = tickers;
    data.period = periods[$('#period-slider').val()];
    data.interval = intervals[$('#interval-slider').val()];
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
    $('#tickers-list').append('<li><div class="ticker-item">' + $('#ticker-input').val() + '<span data-name="' + $('#ticker-input').val() + '" onclick="remove(this)" class="ticker-remove">&#10006;</span></div></li>');
    tickers.push($('#ticker-input').val());
    $('#ticker-input').val('')
}


function periodUpdate(){
    $('#period-label').html(periods[$('#period-slider').val()])
}

function intervalUpdate(){
    $('#interval-label').html(intervals[$('#interval-slider').val()])
}

function remove(ticker) {
    let name = $(ticker).data('name')
    let index = tickers.indexOf(name)
    if (index != -1)
        tickers.splice(tickers,1)
    $(ticker).parent().remove();
}

