(function(angular){
    "use strict";
    angular.module("pos.auth", [
        "pos.common.services",
        "pos.auth.services",
        "pos.auth.interceptors",
        "pos.auth.forms",
        "pos.auth.controllers",
        "pos.auth.routes"
    ]);

})(angular);
