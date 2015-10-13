(function(anglular){
    "use strict";

    angular.module("pos.sales.routes.base", [
        "pos.common"
    ])

    .config(function config($stateProvider) {
        $stateProvider
            // sales
            .state("base.sales", {
                url: "/sales",
                abstract: true,
                views: {
                    "content@base": {
                        templateUrl: "sales/tpls/common/base.tpl.html"
                    },
                    "base-content@base.sales": {
                        templateUrl: "sales/tpls/common/base-content.tpl.html"
                    },
                    "content-header@base.sales": {
                        templateUrl: "common/tpls/content-header.tpl.html",
                        controller: ["$scope",function($scope){$scope.title="Sales";}]
                    }
                },
                data: {pageTitle: "Sales"}
            })
            .state("base.sales.list", {
                    url: "/list",
                    views: {
                        "content@base.sales": {
                            templateUrl: "sales/tpls/list.tpl.html",
                            controller: "Pos.Sales.List.Controller as vm"
                        },
                        "content-search@base.sales": {
                            templateUrl: "common/tpls/content-search.tpl.html"
                        },
                        "content-controls@base.sales": {
                            templateUrl: "sales/tpls/content-controls-grid.tpl.html"
                        },
                        "content-header@base.sales": {
                            templateUrl: "common/tpls/content-header.tpl.html",
                            controller: ["$scope",function($scope){$scope.title="Added Sales";}]
                        }
                    },
                    data: {pageTitle: "All Sales"}
                })
            .state("base.sales.view", {
                    url: "/:id",
                    views:{
                        "content@base.sales": {
                            templateUrl: "sales/tpls/view.tpl.html",
                            controller: "Pos.Sales.View.Controller as vm"
                        },
                        "content-controls@base.sales": {
                            templateUrl: "sales/tpls/content-controls-view.tpl.html"
                        },
                        "content-header@base.sales": {
                            templateUrl: "common/tpls/content-header.tpl.html",
                            controller: ["$scope",function($scope){
                                $scope.title="Sales Details";
                            }]
                        }
                    },
                    data: {pageTitle: "View Sales"}
                });
    });

})(angular);
