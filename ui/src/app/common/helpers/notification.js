(function(angular){
    "use strict";
    angular.module("pos.common.utils.notifications", [])

    .service("Pos.Notification", function(){
        var toastrOptions = {
            "closeButton": true,
            "debug": false,
            "newestOnTop": false,
            "progressBar": false,
            "positionClass": "toast-top-center",
            "preventDuplicates": false,
            "onclick": null,
            "showDuration": "300",
            "hideDuration": "1000",
            "timeOut": "5000",
            "extendedTimeOut": "1000",
            "showEasing": "swing",
            "hideEasing": "linear",
            "showMethod": "fadeIn",
            "hideMethod": "fadeOut"
        };
        this.error = function(tytle, msg){
            var title = tytle || "An Error Occured";
            toastr.error(msg, title, toastrOptions);
        };

        this.success = function(tytle, msg){
            var title = tytle || "Success";
            toastr.success(msg, title, toastrOptions);
        };

        this.warning = function(tytle, msg){
            var title = tytle || "Warning";
            toastr.warning(msg, title, toastrOptions);
        };

        this.info = function(tytle, msg){
            var title = tytle || "Info";
            toastr.info(msg, title, toastrOptions);
        };
    });
})(angular);
