(function(anglular){
    "use strict";

    angular.module("pos.agents.routes.base", [
        "pos.common"
    ])

    .config(function config($stateProvider) {
        $stateProvider
            // setup
            .state("base.agents", {
                url: "/agents",
                abstract: true,
                views: {
                    "content@base": {
                        templateUrl: "agents/tpls/common/base.tpl.html"
                    },
                    "base-content@base.agents": {
                        templateUrl: "agents/tpls/common/base-content.tpl.html"
                    },
                    "sub-menu@base.agents": {
                        templateUrl: "agents/tpls/common/menu.tpl.html"
                    },
                    "content-header@base.agents": {
                        templateUrl: "common/tpls/content-header.tpl.html",
                        controller: ["$scope",function($scope){$scope.title="Sales Agents";}]
                    }
                },
                data: {pageTitle: "Sales Agents"}
            });
    });

})(angular);
