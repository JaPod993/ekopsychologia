$(function () {
    $("#newsletter-sign-in").on("submit", function (e) {
        e.preventDefault();
        var form = $(this);
        form.find(".msg").remove();
        $.post(form.attr("action"), form.serialize(), function (data) {
            console.log(data);
            if (data.status == "OK") {
                form.find("input[name='email']").val("").after('<span class="msg success">' + data.success + '</span>');
            } else if (data.status == "NOK") {
                form.find("input[name='email']").after('<span class="msg error">' + data.error + '</span>');
            }
        }).fail(function (data) {
            alert("Nie udało się zapisać do newslettera");
        });

    });


    // obszary dzialania sprawdzanie # i otwieranie
 if(window.location.hash != ""){
	$('button[data-target="'+ window.location.hash +'"]').trigger('click');
	$('html, body').animate({
        scrollTop: $('button[data-target="'+ window.location.hash +'"]').offset().top
    }, 1000);
}
});
var eventFired = 0;

if ($(window).width() > 768) {
  $(function() {
	 //$('.item').matchHeight({ byRow: true });
	$('.item').matchHeight({ property: 'min-height' });

    $('button[data-toggle="collapse"]').parent().on('hidden.bs.collapse', function(){
        $.fn.matchHeight._update();
    });
    $('button[data-toggle="collapse"]').parent().on('shown.bs.collapse', function(){
        $.fn.matchHeight._update();
    });
});


}
else {

    eventFired = 1;
}

$(window).on('resize', function() {
    if (!eventFired) {
        if ($(window).width() > 768) {
           $(function() {
	 //$('.item').matchHeight({ byRow: true });
	$('.item').matchHeight({ property: 'min-height' });

    $('button[data-toggle="collapse"]').parent().on('hidden.bs.collapse', function(){
        $.fn.matchHeight._update();
    });
    $('button[data-toggle="collapse"]').parent().on('shown.bs.collapse', function(){
        $.fn.matchHeight._update();
    });
});

        } else {

        }
    }
});







$(window).load(function () {

    if ($('.osiagniecia-bg').length > 0) {
        var hasBeenTrigged = false;
        var odleglosc = $('.osiagniecia-bg').offset().top - 550 - $('.osiagniecia-bg').height();

        $(window).scroll(function () {
            if ($(this).scrollTop() >= odleglosc && !hasBeenTrigged) { // if scroll is greater/equal then 100 and hasBeenTrigged is set to false.


                $('.osiagniecia-cyfry').each(function () {
                    $(this).prop('Counter', 0).animate({
                        Counter: $(this).text()
                    }, {
                        duration: 4000,
                        easing: 'swing',
                        step: function (now) {
                            $(this).text(Math.ceil(now));
                        }
                    });
                });
                hasBeenTrigged = true;
            }
        });
    }
});


$(document).ready(function () {

    $('.single-item').slick({

        accessibility: true,
        dots: true,
        autoplay: true,
        autoplaySpeed: 7000,
        speed: 1500,
    });
    $('.partner-1').slick({
        dots: false,
        arrows: false,
        autoplay: true,
        fade: true,
        centerMode: true,
        autoplaySpeed: 5000,
    });
    $('.opinie-slider').slick({

        accessibility: true,
        dots: true,
        autoplay: true,
        autoplaySpeed: 10000,
        speed: 1500,
    });



});

//article height

function set_news_height() {
    var sizes = [];
    $(".compared-text-part2").height('auto');
    $(".compared-text-part").height('auto');

    $(".compared-text-part").each(function () {
        sizes.push($(this).height());
    });
    $(".compared-text-part").height(Math.max.apply(null, sizes));
    $(".compared-text-part2").each(function () {
        sizes.push($(this).height());
    });
    $(".compared-text-part2").height(Math.max.apply(null, sizes));
}


function is_desktop() {
    return $(window).width() >= 736;
}

$(function () {
    var resize_timeout = null;

    setTimeout(function () {
        if (is_desktop()) {
            set_news_height();
        }
    }, 200);

    $(window).resize(function () {
        if (is_desktop()) {

            if (resize_timeout != null) {
                clearTimeout(resize_timeout);
            }

            resize_timeout = setTimeout(function () {
                set_news_height();
            }, 200);

        }
    });


});


