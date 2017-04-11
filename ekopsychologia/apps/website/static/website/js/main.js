$(function(){
    $("#newsletter-sign-in").on("submit", function(e){
        e.preventDefault();
        var form = $(this);
        form.find(".msg").remove();
        $.post(form.attr("action"), form.serialize(), function (data) {
            console.log(data);
            if (data.status == "OK") {
                    form.find("input[name='email']").val("").after('<span class="msg success">' + data.success + '</span>');
            }else if (data.status == "NOK") {
                form.find("input[name='email']").after('<span class="msg error">' + data.error + '</span>');
            }
        }).fail(function (data) {
            alert("Nie udało się zapisać do newslettera");
        });

    });
})




 $(document).ready(function(){

        $('.single-item').slick({

            accessibility: true,
            dots: true,
            autoplay: false,
            autoplaySpeed: 5000,
        });
        $('.partner-1').slick({
           dots: false,
            arrows: false,
            autoplay: true,
            fade: true,
            centerMode: true,
            autoplaySpeed: 5000,
        });

    });

    //article height

    function set_news_height() {
        var sizes = [];
        $(".compared-text-part2").height('auto');
        $(".compared-text-part").height('auto');

        $(".compared-text-part").each(function(){
            sizes.push($(this).height());
        });
        $(".compared-text-part").height(Math.max.apply(null, sizes));
        $(".compared-text-part2").each(function(){
            sizes.push($(this).height());
        });
        $(".compared-text-part2").height(Math.max.apply(null, sizes));
    }

    function is_desktop(){
        return $(window).width() >= 736;
    }

    $(function(){
        var resize_timeout = null;

        setTimeout(function(){
            if(is_desktop()){
                set_news_height();
            }
        }, 200);

        $(window).resize(function() {
            if(is_desktop()){

                if(resize_timeout != null){
                    clearTimeout(resize_timeout);
                }

                resize_timeout = setTimeout(function(){
                    set_news_height();
                }, 200);

            }
        });

    });