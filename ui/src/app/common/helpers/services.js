(function(angular){
    "use strict";
    angular.module("pos.common.utils.services", [])
    .service("Pos.HelperService", ["Pos.Auth.AuthService", function(AuthService){
        return {
            addOrganization: function(data){
                var organization = {organization: AuthService.getUser().organization.id};
                return _.extend(data, organization);
            }
        };
    }]);
})(angular);
