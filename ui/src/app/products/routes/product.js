(function(anglular){
    "use strict";

    angular.module("pos.products.routes.product", [
        "pos.products.routes.base"
    ])

    .config(function config($stateProvider) {
        $stateProvider
            // products
            .state("base.products.list", {
                url: "/list",
                views: {
                    "content@base.products": {
                        templateUrl: "products/tpls/product/list.tpl.html",
                        controller: "Pos.Products.List.Controller as vm"
                    },
                    "content-header@base.setup": {
                        templateUrl: "common/tpls/content-header.tpl.html",
                        controller: ["$scope",function($scope){$scope.title="Products";}]
                    }
                },
                data: {pageTitle: "Products"}
            })
            .state("base.products.create", {
                url: "/create",
                views: {
                    "content@base.products": {
                        templateUrl: "products/tpls/product/create.tpl.html",
                        controller: "Pos.Products.Create.Controller as vm"
                    },
                    "content-header@base.setup": {
                        templateUrl: "common/tpls/content-header.tpl.html",
                        controller: ["$scope",function($scope){$scope.title="Add Product";}]
                    }
                },
                data: {pageTitle: "Create Product"}
            })
            .state("base.products.view", {
                url: "/:id",
                views:{
                    "content@base.products": {
                        templateUrl: "products/tpls/product/view.tpl.html",
                        controller: "Pos.Products.View.Controller as vm"
                    },
                    "content-header@base.setup": {
                        templateUrl: "common/tpls/content-header.tpl.html",
                        controller: ["$scope",function($scope){
                            $scope.title="Product Details";
                        }]
                    }
                },
                data: {pageTitle: "View Product"}
            });
    });

})(angular);
