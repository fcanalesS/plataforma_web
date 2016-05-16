jQuery('#go-back').click(function () {
    document.reload()
});

jQuery('#enhanced').click(function () {
    jQuery.get('/enhanced', function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
        //document.write(result)
    })
});

jQuery('#negative').click(function () {
    jQuery.get('/negative', function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
        //document.write(result)
    })
});

jQuery('#sepia').click(function () {
    jQuery.get('/sepia', function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
        //document.write(result)
    })
});


function setBGR() {
    jQuery('#blueInp').val(sliders[0].noUiSlider.get());
    jQuery('#greenInp').val(sliders[1].noUiSlider.get());
    jQuery('#redInp').val(sliders[2].noUiSlider.get());
}
var sliders = document.getElementsByClassName('sliders');

for (var i = 0; i < sliders.length; i++) {

    noUiSlider.create(sliders[i], {
        start: 0,
        step: 1,
        connect: "lower",
        orientation: "horizontal",
        range: {
            'min': -100,
            'max': 100
        }
    });
    // Bind the color changing function
    // to the slide event.
    sliders[i].noUiSlider.on('slide', setBGR)
}

jQuery('#btn-bgr').on('click', function () {
    jQuery.ajax({
        method: 'get',
        url: '/bgr',
        data: {
            blue: jQuery('#blueInp').val(),
            green: jQuery('#greenInp').val(),
            red: jQuery('#redInp').val()
        }
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
        //document.getElementById('imagen').innerHTML= 'asdasdasd'
    })
});

function setBC() {
    jQuery('#brightInp').val(sliders2[0].noUiSlider.get());
    jQuery('#contrastInp').val(sliders2[1].noUiSlider.get());

}
var sliders2 = document.getElementsByClassName('sliders2');

for (var i = 0; i < sliders2.length; i++) {

    noUiSlider.create(sliders2[i], {
        start: 0,
        step: 1,
        connect: "lower",
        orientation: "horizontal",
        range: {
            'min': -100,
            'max': 100
        }
    });
    sliders2[i].noUiSlider.on('slide', setBC)
}

jQuery('#btn-bc').on('click', function () {
    jQuery.ajax({
        method: 'get',
        url: '/brillo-contraste',
        data: {
            brillo: jQuery('#brightInp').val(),
            contraste: jQuery('#contrastInp').val()
        }
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
    })
});
