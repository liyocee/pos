(function(angular){
    "use strict";
    angular.module("pos.common.services", [])
    .service("storageService", ["$window", function($window){
        this.store = function(key, value){
            $window.localStorage.setItem(key, JSON.stringify(value));
        };

        this.retrieve = function(key){
            return JSON.parse($window.localStorage.getItem(key));
        };

        this.remove = function(key){
            $window.localStorage.removeItem(key);
        };
    }]);
})(angular);
