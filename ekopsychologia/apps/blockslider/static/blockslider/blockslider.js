jQuery(function(){

    $('textarea').each(function(){
        var textarea = $(this);
        var editor = CodeMirror.fromTextArea(textarea.get(0), {
          lineNumbers: true,
          mode: "htmlmixed",
          autoCloseTags: true
        });

    });


});