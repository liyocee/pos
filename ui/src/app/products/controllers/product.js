(function(angular){
    "use strict";
    angular.module("pos.products.controllers.product", [
            "pos.products.services",
            "pos.products.forms"
        ])
    .controller("Pos.Products.List.Controller",
        ["NgTableParams", "Pos.Products.Service", function (NgTableParams, ProductService) {
            var vm = this;
            vm.service = {
                name: ProductService,
                key: "productTypes"
            };

        }]
    )
    .controller("Pos.Products.Create.Controller",
        ["$state", "Pos.Products.Form.Product", "Pos.Products.Service",
        "Pos.Notification",
        function ($state, Form, ProductService, notification) {
            var vm = this;
            vm.product = {};
            vm.productFields = Form.getForm({});
            vm.create = function(product){
                vm.promise = ProductService.productTypes.create(product);
                vm.promise.then(
                    function(data){
                        notification.success("Success", "Product Created successfully");
                        $state.go("base.products.list");
                    },
                    function(error){
                        notification.error("Error", "Error creating the product");
                        console.log(error);
                    }
                );
            };
        }]
    )
    .controller("Pos.Products.View.Controller",
        ["$state", "$stateParams",
        "Pos.Products.Service","Pos.Notification",
        function ($state, $stateParams, ProductsService, notification) {
            var vm = this;
            vm.promise = ProductsService.productTypes.get($stateParams.id);
            vm.promise.then(
                function(data){vm.product = data;},
                function(error){console.log(error);}
            );
            vm.updateProduct = function(product, field){
                var dt = {};
                dt[field] = product;
                vm.promise = ProductsService.productTypes.update(
                    $stateParams.id, dt);
                vm.promise.then(
                    function(data){
                        vm.product=data;
                        notification.success("Success", "Details successfully updated");
                        return true;
                    },
                    function(error){
                        console.log(error);
                        notification.error("Error", "Error updating the details");
                        return false;
                    }
                );
            };
        }]
    )
    ;

})(angular);
