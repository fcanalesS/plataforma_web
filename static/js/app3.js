jQuery('#convolucion').click(function () {
    jQuery.ajax({
        method: 'get',
        url: '/convolucion',
        data: {conv: jQuery('#convolucion').val(), desconv: jQuery('#desconvolucion').val()}
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
    });
});

jQuery('#desconvolucion').click(function () {
    location.reload()
});

jQuery('#fourier').click(function () {
    alert('Modulo no implementado. ! ! !')
});


jQuery('#dip-gauss').click(function () {
    jQuery.ajax({
        method: 'get',
        url: '/disp-gaussian'
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
    });
});