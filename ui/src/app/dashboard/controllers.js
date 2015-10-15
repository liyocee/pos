(function(angular){
    "use strict";
    angular.module("pos.dashboard.controllers", [
        "pos.auth.services",
        "pos.dashboard.services",
        "ngC3"
    ])

    .controller("Pos.Dashboard.Controller",
        ["$scope","$stateParams", "Pos.Reports.Service",
        function ($scope,$stateParams, ReportsService) {
            $scope.salesChart = {
                options: {
                    type: "pie"
                },
                series: []
            };
            $scope.agentsChart = {
                options: {
                    type: "pie"
                },
                series: []
            };
            ReportsService.reports.list().then(
                function(data){
                    _.each(data.products, function(product){
                        $scope.salesChart.series.push({
                            name: product.name,
                            data: [product.count]
                        });
                    });
                    _.each(data.agents, function(agent){
                        $scope.agentsChart.series.push({
                            name: agent.name,
                            data: [agent.count]
                        });
                    });
                }, function(error){
                    console.log(error);
                });


        }]);

})(angular);
