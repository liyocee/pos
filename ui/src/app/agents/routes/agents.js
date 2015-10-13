(function(anglular){
    "use strict";

    angular.module("pos.agents.routes.product", [
        "pos.agents.routes.base"
    ])

    .config(function config($stateProvider) {
        $stateProvider
            // agents
            .state("base.agents.list", {
                url: "/list",
                views: {
                    "content@base.agents": {
                        templateUrl: "agents/tpls/agent/list.tpl.html",
                        controller: "Pos.Agents.List.Controller as vm"
                    },
                    "content-header@base.setup": {
                        templateUrl: "common/tpls/content-header.tpl.html",
                        controller: ["$scope",function($scope){$scope.title="Agents";}]
                    }
                },
                data: {pageTitle: "Agents"}
            })
            .state("base.agents.create", {
                url: "/create",
                views: {
                    "content@base.agents": {
                        templateUrl: "agents/tpls/agent/create.tpl.html",
                        controller: "Pos.Agents.Create.Controller as vm"
                    },
                    "content-header@base.setup": {
                        templateUrl: "common/tpls/content-header.tpl.html",
                        controller: ["$scope",function($scope){$scope.title="Add Product";}]
                    }
                },
                data: {pageTitle: "Create Agent"}
            })
            .state("base.agents.view", {
                url: "/:id",
                views:{
                    "content@base.agents": {
                        templateUrl: "agents/tpls/agent/view.tpl.html",
                        controller: "Pos.Agents.View.Controller as vm"
                    },
                    "content-header@base.setup": {
                        templateUrl: "common/tpls/content-header.tpl.html",
                        controller: ["$scope",function($scope){
                            $scope.title="Product Details";
                        }]
                    }
                },
                data: {pageTitle: "View Agent"}
            });
    });

})(angular);
