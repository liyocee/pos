(function(anglular){
    "use strict";

    angular.module("pos.dashboard.routes", ["pos.common"])

        .config(function config($stateProvider) {
            $stateProvider
                .state("base.dashboard", {
                    url: "/dashboard",
                    views: {
                        "content@base": {
                            templateUrl: "dashboard/tpls/dashboard.tpl.html"
                        }
                    },
                    data: {pageTitle: "Dashboard"},
                    options: {
                        reload: true
                    }
                });
        });

})(angular);
