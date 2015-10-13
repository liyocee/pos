(function(angular){
    "use strict";
    angular.module("pos.sales", [
        "ui.router",
        "toastr",
        "ui.bootstrap",
        "ui.bootstrap.tpls",

        "pos.sales.controllers",
        "pos.sales.routes",
        "pos.sales.services"
    ]);

})(angular);
