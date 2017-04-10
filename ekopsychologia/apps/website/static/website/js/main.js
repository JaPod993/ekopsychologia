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


