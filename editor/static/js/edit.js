$(document).on("click", "#change",function(){
    console.log("aaa");
    let pass = $("#pass").val();
    let data = $("#edit-file").val();

    $.ajax({
        type: "POST",
        url: window.location.origin + "/api/v1/override",
        data: {"pass": pass, "edit-file": data},
        dataType: "json",
        success: function(response){
            ;
        }
    })
});