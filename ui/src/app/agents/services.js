(function(angular){
    angular.module("pos.agents.services", [
        "pos.common",
        "pos.auth.services",
        "pos.common.utils.services"
    ])
    .service("Pos.Agents.Service", ["Restangular", "Pos.Auth.AuthService",
    "Pos.HelperService",
    function(api, AuthService, HelperService){
        var baseApi = api.all("pos").all("agent");
        var orgId = AuthService.getUser().organization.id;
        // agents
        this.agents = {
            create: function(data){
                return baseApi.post(HelperService.addOrganization(data));
            },
            list: function(filters){
                var query_param = {
                    organization: orgId
                };
                _.extend(query_param, filters);
                return baseApi.customGET("", query_param);
            },
            get: function(agentId){
                return baseApi.one("", agentId).get();
            },
            update: function(agentId, data){
                return baseApi.one("", agentId).patch(data);
            }
        };
    }]);
})(angular);
