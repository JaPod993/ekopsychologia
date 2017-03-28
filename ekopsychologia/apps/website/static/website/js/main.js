$(".show_on_hover").stop().animate({"opacity": "0.5"});
$(".show_on_hover").hover(function () {
    $(this).stop().animate({
        "opacity": "1"
    }, "fast");
}, function () {
    $(this).stop().animate({
        "opacity": "0.5"
    }, "fast");
});