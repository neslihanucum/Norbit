/*==============================================================*/
// Raque Contact Form  JS
/*==============================================================*/
(function ($) {
    "use strict"; // Start of use strict
    $("#contactForm").validator().on("submit", function (event) {
        if (event.isDefaultPrevented()) {
            // handle the invalid form...
            formError();
            submitMSG(false, "Lütfen formu eksiksiz doldurunuz.");
        } else {
            // everything looks good!
            event.preventDefault();
            submitForm();
        }
    });




    function formSuccess(){
        $("#contactForm")[0].reset();
        submitMSG(true, "Mesajınız Gönderildi!")
    }

    function formError(){
        $("#contactForm").removeClass().addClass('animate__animated animate__shakeX').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
            $(this).removeClass();
        });
    }

    function submitMSG(valid, msg){
        if(valid){
            var msgClasses = "h4 submit-post-info tada animated text-success";
        } else {
            var msgClasses = "h4 submit-post-info text-danger";
        }
        $("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
    }
}(jQuery)); // End of use strict