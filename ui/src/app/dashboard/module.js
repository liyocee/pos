(function(angular){
    "use strict";
    angular.module("pos.dashboard", [
        "ui.router",
        "toastr",
        "ui.bootstrap",
        "ui.bootstrap.tpls",
        "pos.dashboard.routes",
        "pos.dashboard.controllers",
        "pos.dashboard.services"
    ]);

})(angular);
