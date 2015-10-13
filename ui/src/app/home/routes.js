(function(anglular){
    "use strict";

    angular.module("pos.home.routes", ["pos.common"])

        .config(function config($stateProvider) {
            $stateProvider
                .state("home", {
                    url: "/",
                    views: {
                        "main-container": {
                            templateUrl: "home/tpls/home.tpl.html"
                        },
                        "header@home": {
                            templateUrl: "home/tpls/header.tpl.html"
                        },
                        "content@home": {
                            templateUrl: "home/tpls/content.tpl.html"
                        },
                        "footer@home": {
                            templateUrl: "common/tpls/footer.tpl.html"
                        }
                    },
                    data: {pageTitle: "Home"}
                });
        });

})(angular);
