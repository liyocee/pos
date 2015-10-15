(function(angular){
    angular.module("pos.dashboard.services", [
        "pos.common",
        "pos.auth.services"
    ])
    .service("Pos.Reports.Service", ["Restangular", "Pos.Auth.AuthService",
    function(api, AuthService){
        var baseApi = api.all("reports");
        var userId = AuthService.getUser().id;
        var organizationId = AuthService.getUser().organization.id;
        this.reports = {
            list: function(){
                var query_param = {
                    organization: organizationId
                };
                return baseApi.customGET("", query_param);
            }
        };
    }]);
})(angular);
