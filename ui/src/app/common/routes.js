(function(anglular){
    "use strict";
    angular.module("pos.common.routes", [])
    .config(function config($stateProvider) {
        $stateProvider
            .state("base", {
                abstract: true,
                url: "",
                views: {
                    "main-container": {
                        templateUrl: "common/tpls/main-container.tpl.html"
                    },
                    "main@base": {
                        templateUrl: "common/tpls/main.tpl.html"
                    },
                    "footer@base": {
                        templateUrl: "common/tpls/footer.tpl.html"
                    },
                    "control-side-bar@base": {
                        templateUrl: "common/tpls/control-side-bar.tpl.html"
                    },
                    "control-side-bar-bg@base": {
                        templateUrl: "common/tpls/control-side-bar-bg.tpl.html"
                    },
                    "header@base": {
                        templateUrl: "common/tpls/header.tpl.html",
                        controller: "Pos.UserProfile.Controller as vm"
                    },
                    "nav@base": {
                        templateUrl: "common/tpls/side_nav.tpl.html",
                        controller : ["$scope", "$state", function ($scope, $state){ $scope.$state = $state;}]
                    }
                },
                data: {pageTitle: "Pos"}
            })
            ;
    });

})(angular);
