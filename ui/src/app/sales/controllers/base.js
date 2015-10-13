(function(angular){
    "use strict";
    angular.module("pos.sales.controllers.base", [
            "pos.sales.services"
        ])
    .controller("Pos.Sales.List.Controller",
        ["NgTableParams", "Pos.Sales.Service", function (NgTableParams, SalesService) {
            var vm = this;
            vm.service = {
                name: SalesService,
                key: "pos"
            };

        }]
    )
    .controller("Pos.Sales.View.Controller",
        ["$state", "$stateParams", "Pos.Sales.Form.Board",
        "Pos.Sales.Service","Pos.Notification",
        function ($state, $stateParams, Form, PosService, notification) {
            var vm = this;
            vm.promise = PosService.pos.get($stateParams.id);
            vm.promise.then(
                function(data){vm.sales = data;},
                function(error){console.log(error);}
            );
            vm.updateSales = function(sales, field){
                var dt = {};
                dt[field] = sales;
                vm.promise = PosService.sales.update(
                    $stateParams.id, dt);
                vm.promise.then(
                    function(data){
                        vm.sales=data;
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
