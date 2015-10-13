(function(angular){
    "use strict";
    angular.module("pos.auth.controllers", [
        "pos.auth.services",
        "pos.auth.forms",
        "pos.common.services"
    ])
    .controller("Pos.UserProfile.Controller",
        ["Pos.Auth.AuthService", "Pos.Notification",
        function (AuthService, notification) {
            var vm = this;
            vm.user = AuthService.getUser();
            vm.logout = function(){
                notification.info("Logout", "Successfully logged out");
                AuthService.logout();
            };
        }]
    )

    .controller("Pos.Login.Controller",
        ["$scope","$stateParams", "Pos.Auth.AuthService", "Pos.Form.Login",
        function ($scope,$stateParams, AuthService, Form) {
            var vm = this;
            vm.user = {};
            vm.userFields = Form.getForm();
            vm.login = function(user){
                AuthService.login(
                    user.username, user.password, $scope);
            };
        }]
    )
    .controller("Pos.MemberRegistration.Controller",
        ["$scope","$state", "Pos.Organization.Form.Registration",
        "Pos.Auth.AuthService", "Pos.Notification",
        "storageService","AUTH_KEY",
        function ($scope, $state, Form, AuthService, notification, storage, AUTH_KEY) {
            storage.remove(AUTH_KEY);
            var vm = this;
            vm.user = {
                profile: {
                    first_name: "",
                    last_name: "",
                    email: "",
                    password: ""
                }
            };
            vm.confirmPassword = {};
            var formOptions = {
                user: {model: vm.user},
                password: {model: vm.confirmPassword},
                profile: {model: vm.user.profile}
            };
            vm.userFields = Form.getForm(formOptions);
            vm.signup = function(user){
                vm.promise = AuthService.register(user);
                vm.promise.then(
                    function(){
                        notification.success("Success", "Registration was successful");
                        $state.go("login");
                    },
                    function(error){
                        notification.error("Error", "An error occured");
                        console.log(error);
                    }
                );
            };
        }]
    )
    ;

})(angular);
