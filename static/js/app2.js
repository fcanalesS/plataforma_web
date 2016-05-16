var rotate = document.getElementById('rotate');
noUiSlider.create(rotate, {
    start: 0,
    range: {'min': 0, 'max': 360},
    step: 90
});

rotate.noUiSlider.on('end', function (values, handle) {
    jQuery.ajax({
        method: 'get',
        url: '/rotate',
        data: {angle: parseFloat(values)}
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
    })
});

//**********************************************************************************************//

var blur = document.getElementById('blur');
noUiSlider.create(blur, {
    start: 0,
    range: {'min': 1, 'max': 100},
    step: 1
});

blur.noUiSlider.on('end', function (values, handle) {
    jQuery.ajax({
        method: 'get',
        url: '/blur',
        data: {blur: parseInt(values)}
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
    })
});

//**********************************************************************************************//

var sharp = document.getElementById('sharp');
noUiSlider.create(sharp, {
    start: 0,
    range: {'min': 1, 'max': 60},
    step: 1
});

sharp.noUiSlider.on('end', function (values, handle) {
    jQuery.ajax({
        method: 'get',
        url: '/sharp',
        data: {sharp: parseInt(values)}
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
    })
});

//**********************************************************************************************//

jQuery('#mirror').click(function () {
    jQuery.ajax({
        method: 'get',
        url: '/mirror'
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
    });
});

//**********************************************************************************************//

function setBorder() {
    jQuery('#border_1').val(parseInt(sliders3[0].noUiSlider.get()));
    jQuery('#border_2').val(parseInt(sliders3[1].noUiSlider.get()));
}
var sliders3 = document.getElementsByClassName('sliders3');

for (var i = 0; i < sliders3.length; i++) {

    noUiSlider.create(sliders3[i], {
        start: 0,
        step: 1,
        connect: "lower",
        orientation: "horizontal",
        range: {
            'min': 0,
            'max': 500
        }
    });
    // Bind the color changing function
    // to the slide event.
    sliders3[i].noUiSlider.on('slide', setBorder)
}

jQuery('#btn-border').on('click', function () {
    jQuery.ajax({
        method: 'get',
        url: '/border',
        data: {
            val1: jQuery('#border_1').val(),
            val2: jQuery('#border_2').val()
        }
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
        //document.getElementById('imagen').innerHTML= 'asdasdasd'
    })
});