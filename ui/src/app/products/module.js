(function(angular){
    "use strict";
    angular.module("pos.products", [
        "ui.router",
        "toastr",
        "ui.bootstrap",
        "ui.bootstrap.tpls",

        "pos.products.controllers",
        "pos.products.routes",
        "pos.products.services",
        "pos.products.forms"
    ]);

})(angular);
