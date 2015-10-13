(function(anglular){
    "use strict";
    angular.module("pos.auth.routes", [
        "pos.auth.controllers"
    ])
    .config(function config($stateProvider) {
        $stateProvider
            .state("login", {
                url: "/login",
                views: {
                    "main-container": {
                        templateUrl: "auth/tpls/login.tpl.html",
                        controller: "Pos.Login.Controller as vm"
                    },
                    "header@login": {
                        templateUrl: "common/tpls/sub_header.tpl.html"
                    },
                    "error@login": {
                        templateUrl: "common/tpls/error.tpl.html"
                    }
                },
                data: {pageTitle: "Member Login"}
            })
            .state("signup", {
                url: "/signup",
                views: {
                    "main-container": {
                        templateUrl: "auth/tpls/signup.tpl.html",
                        controller: "Pos.MemberRegistration.Controller as vm"
                    },
                    "header@signup": {
                        templateUrl: "common/tpls/sub_header.tpl.html"
                    }
                },
                data: {pageTitle: "Member Signup"}
            });
    });

})(angular);
