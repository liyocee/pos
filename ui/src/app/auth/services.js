(function(angular){
    "use strict";
    angular.module("pos.auth.services", ["pos.common.services"])
    .service("Pos.Auth.AuthService", ["$state","$window", "$http", "Restangular", "storageService",
        "HOME_PAGE_NAME","AUTH_KEY", "Pos.Notification",
        function($state,$window, $http, api, storage, HOME_PAGE, AUTH_KEY, notification){
        var storeKey = AUTH_KEY;
        var setCredentials = function(credz){
            storage.store(storeKey, credz);
        };

        var getToken = function(){
            var credz = storage.retrieve(storeKey);
            if(credz){
                return credz.token;
            }
        };

        var getUser = function(){
            var credz = storage.retrieve(storeKey);
            if(credz){
                return credz.user;
            }else{
                $state.go("login");
            }
        };

        var login = function(username, password, scope){
            var data = {
                username: username,
                password: password
            };
            scope.login_promise = api.all("auth").all("login").post(data);
            scope.login_promise.then(
                function(data){
                    var credz = {
                        token: data.key,
                        user: data.user
                    };
                    setCredentials(credz);
                    $window.location.replace("/dashboard");
                    notification.success("Login", "Successfully logged in");
                },
                function(error){
                    scope.alert = "Invalid username/password combination";
                    notification.error("Error", "Error logging in");
                });
        };
        var logout = function(){
            storage.remove(storeKey);
            api.all("auth").all("logout").post({}).then(
                function(data){
                    $state.go("home");
                },
                function(error){
                    $state.go("home");
                });

        };

        var register = function(data){
            var baseApi = api.all("pos");
            return baseApi.all("organization").post(data);
        };

        return {
            "setCredentials": setCredentials,
            "getToken": getToken,
            "login": login,
            "logout": logout,
            "getUser": getUser,
            "register": register
        };
    }])
    ;
})(angular);
