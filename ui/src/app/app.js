(function(angular){
    "use strict";
    angular.module("posApp", [
        //third-party stuff
        "ngAnimate",
        "ngCookies",
        "formly",
        "formlyBootstrap",
        "xeditable",
        "ui.select",
        "restangular",
        "cgBusy",
        "ngTable",
        //our stuff
        "templates-app",
        "posConfig",
        "pos.home",
        "pos.dashboard",
        "pos.common",
        "pos.sales",
        "pos.auth",
        "pos.products",
        "pos.agents"
    ])
    .run(["editableOptions", function(editableOptions){
        editableOptions.theme = "bs3";
    }]);

})(angular);
