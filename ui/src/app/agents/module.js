(function(angular){
    "use strict";
    angular.module("pos.agents", [
        "ui.router",
        "toastr",
        "ui.bootstrap",
        "ui.bootstrap.tpls",

        "pos.agents.controllers",
        "pos.agents.routes",
        "pos.agents.services",
        "pos.agents.forms"
    ]);

})(angular);
