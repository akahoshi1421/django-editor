var thefile;

$(document).on("click", "#change",function(){
    let pass = $("#pass").val();
    let data = $("#edit-file").val();

    $.ajax({
        type: "POST",
        url: window.location.origin + "/api/v1/override",
        data: {"pass": pass, "edit-file": data},
        dataType: "json",
        success: function(response){
            if(response["res"] == "SUCCESS"){
                $(".success").fadeIn(300).delay(1000).fadeOut(300);
            }
            else{
                $(".danger").fadeIn(300).delay(1000).fadeOut(300);
            }
        }
    })
});

$(document).on("click", "#py",function(){
    $.ajax({
        type: "POST",
        url: window.location.origin + "/api/v1/pyexecute",
        data: {"pass": $("h1 span").text()},
        dataType: "json",
        success: function(res){
            $("#out").text(res["res"]);
        }
    })
});

$(document).on("click", "#gcc", function(){
    $.ajax({
        type: "POST",
        url: window.location.origin + "/api/v1/gcc",
        data: {"pass": $("h1 span").text()},
        dataType: "json",
        success: function(res){
            $("#out").text(res["res"]);
        }
    })
});

$(document).on("click", "#c", function(){
    $.ajax({
        type: "POST",
        url: window.location.origin + "/api/v1/c",
        data: {"pass": $("h1 span").text()},
        dataType: "json",
        success: function(res){
            $("#out").text(res["res"]);
        }
    })
});

$(document).on("click", "#js", function(){
    $.ajax({
        type: "POST",
        url: window.location.origin + "/api/v1/js",
        data: {"pass": $("h1 span").text()},
        dataType: "json",
        success: function(res){
            $("#out").text(res["res"]);
        }
    })
});


$(document).on("click", "#filechange-btn", () => {
    let filepass = $("h1 span").text().split("/");
    delete filepass[filepass.length - 1];
    let dir = filepass.join("/");
    $.ajax({
        type: "POST",
        url: window.location.origin + "/api/v1/filenamechange",
        data: {"newpass": dir + $("#filechange").val(), "oldpass": $("h1 span").text()},
        dataType: "json",
        success: (res) => {
            $("#file").val(dir + $("#filechange").val());
            $("#submit").click();
        }
    })
});

$(window).on("load", function(){
    let pass =  $("h1 span").text();
    if(pass.substr(-3) == ".py"){
        $("#py").show();
    }
    else if(pass.substr(-2) == ".c"){
        $("#gcc").show();
        $("#c").show();
    }
    else if(pass.substr(-3) == ".js"){
        $("#js").show();
    }

    //ファイル名の表示
    thefile = $("#filechange").val().split("/").pop();
    $("#filechange").val(thefile);
});
