jQuery('#convolucion').click(function () {
    jQuery.ajax({
        method: 'get',
        url: '/convolucion',
        data: {conv: jQuery('#convolucion').val(), desconv: jQuery('#desconvolucion').val()}
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
    });
});

jQuery('#fourier').click(function () {
    jQuery.ajax({
        method: 'get',
        url: '/fourier'
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
    });
});

jQuery('#dip-gauss').click(function () {
    jQuery.ajax({
        method: 'get',
        url: '/disp-gaussian'
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
    });
});