(function(angular){
    "use strict";
    angular.module("pos.dashboard.controllers", [
        "pos.auth.services",
        "pos.dashboard.services",
        "ngC3",
        "leaflet-directive"
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
            angular.extend($scope, {
                nairobi: {
                    lat: -1.3001776,
                    lng: 36.790838,
                    zoom: 8
                },
                markers: {}
            });
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
                        angular.extend($scope, {
                            markers: data.markers
                        });
                    });
                }, function(error){
                    console.log(error);
                });


        }]);

})(angular);
