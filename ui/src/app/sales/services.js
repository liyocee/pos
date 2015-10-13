(function(angular){
    angular.module("pos.sales.services", [
        "pos.common",
        "pos.auth.services"
    ])
    .service("Pos.Sales.Service", ["Restangular", "Pos.Auth.AuthService",
    function(api, AuthService){
        var baseApi = api.all("pos").all("prospect");
        var userId = AuthService.getUser().id;
        this.prospects = {
            create: function(data){
                return baseApi.post(data);
            },
            list: function(filters){
                return baseApi.customGET("", filters);
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
