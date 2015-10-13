(function(anglular){
    "use strict";

    angular.module("pos.products.routes.base", [
        "pos.common"
    ])

    .config(function config($stateProvider) {
        $stateProvider
            // setup
            .state("base.products", {
                url: "/products",
                abstract: true,
                views: {
                    "content@base": {
                        templateUrl: "products/tpls/common/base.tpl.html"
                    },
                    "base-content@base.products": {
                        templateUrl: "products/tpls/common/base-content.tpl.html"
                    },
                    "sub-menu@base.products": {
                        templateUrl: "products/tpls/common/menu.tpl.html"
                    },
                    "content-header@base.products": {
                        templateUrl: "common/tpls/content-header.tpl.html",
                        controller: ["$scope",function($scope){$scope.title="Products";}]
                    }
                },
                data: {pageTitle: "Products"}
            });
    });

})(angular);
