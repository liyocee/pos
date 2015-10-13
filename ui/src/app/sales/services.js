(function(angular){
    angular.module("pos.sales.services", [
        "pos.common",
        "pos.auth.services"
    ])
    .service("Pos.Sales.Service", ["Restangular", "Pos.Auth.AuthService",
    function(api, AuthService){
        var baseApi = api.all("pos").all("sales");
        var userId = AuthService.getUser().id;
        var organizationId = AuthService.getUser().organization.id;
        this.sales = {
            create: function(data){
                return baseApi.post(data);
            },
            list: function(filters){
                var query_param = {
                    organization: organizationId
                };
                _.extend(query_param, filters);
                return baseApi.customGET("", query_param);
            },
            get: function(prospectId){
                return api.one("prospect", prospectId).get();
            },
            update: function(propsectId, data){
                return api.one("prospect", prospectId).patch(data);
            }
        };
    }]);
})(angular);
