(function(angular){
    "use strict";
    angular.module("pos.agents.controllers.product", [
            "pos.agents.services",
            "pos.agents.forms",
            "pos.auth.services"
        ])
    .controller("Pos.Agents.List.Controller",
        ["NgTableParams", "Pos.Agents.Service", function (NgTableParams, AgentsService) {
            var vm = this;
            vm.service = {
                name: AgentsService,
                key: "agents"
            };

        }]
    )
    .controller("Pos.Agents.Create.Controller",
        ["$state", "Pos.Agents.Form.Agent", "Pos.Agents.Service",
        "Pos.Notification",
        function ($state, Form, AgentsService, notification) {
            var vm = this;
            vm.agent = {
                profile: {
                    first_name: "",
                    last_name: "",
                    email: "",
                    password: ""
                }
            };
            vm.confirmPassword = {};
            var formOptions = {
                password: {model: vm.confirmPassword},
                profile: {model: vm.agent.profile}
            };
            vm.agentFields = Form.getForm(formOptions);
            vm.create = function(agent){
                vm.promise = AgentsService.agents.create(agent);
                vm.promise.then(
                    function(data){
                        notification.success("Success", "Sales Agent Created successfully");
                        $state.go("base.agents.list");
                    },
                    function(error){
                        notification.error("Error", "Error creating the Sales Agent");
                        console.log(error);
                    }
                );
            };
        }]
    )
    .controller("Pos.Agents.View.Controller",
        ["$state", "$stateParams",
        "Pos.Agents.Service","Pos.Notification","Pos.Auth.AuthService",
        function ($state, $stateParams, AgentsService, notification, AuthService) {
            var vm = this;
            vm.promise = AgentsService.agents.get($stateParams.id);
            vm.promise.then(
                function(data){vm.agent = data;},
                function(error){console.log(error);}
            );
            vm.updateAgent = function(agent, field){
                var dt = {
                    profile: {
                        id: AuthService.getUser().id
                    }
                };
                dt.profile[field] = agent;
                vm.promise = AgentsService.agents.update(
                    $stateParams.id, dt);
                vm.promise.then(
                    function(data){
                        vm.agent=data;
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
