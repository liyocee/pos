(function (angular, _) {
    "use strict";

    angular.module("posConfig", [
        "ui.router",
        "restangular",
        "pos.auth.interceptors"
    ])
    .constant("HOME_PAGE_NAME", "base.dashboard")
    .constant("SERVER_URL", window.POS_SETTINGS.SERVER_URL)
    .constant("AUTH_KEY", "pos.auth.token")
    .constant("PAGINATION_COUNT", 3)
    .config(["$locationProvider", function ($locationProvider) {
        $locationProvider.html5Mode(true);
    }])

    .config(["$httpProvider", function ($httpProvider) {
        $httpProvider.defaults.headers.common = {
            "Content-Type": "application/json",
            "Accept": "application/json, */*"
        };
    }])

    .config(["$httpProvider", function ($http) {
        $http.defaults.xsrfHeaderName = "X-CSRFToken";
        $http.defaults.xsrfCookieName = "csrftoken";
    }])

    .config(["$logProvider", function ($logProvider) {
        $logProvider.debugEnabled(window.POS_SETTINGS.DEBUG);
    }])
    .config(["RestangularProvider", "SERVER_URL", function(RestangularProvider, SERVER_URL){
        RestangularProvider.setBaseUrl(SERVER_URL);
        RestangularProvider.setRequestSuffix("/");
    }])
    .config(function ($httpProvider) {
        $httpProvider.interceptors.push("POS.Auth.AuthInterceptor");
    })

    .config(["$urlRouterProvider", "HOME_PAGE_NAME",
        function ($urlRouterProvider, HOME_PAGE_NAME) {
            // https://github.com/angular-ui/ui-router/issues/600
            $urlRouterProvider.otherwise( function($injector, $location) {
                var $state = $injector.get("$state");
                $state.go(HOME_PAGE_NAME);
            });
        }
    ]);

})(angular, _);
