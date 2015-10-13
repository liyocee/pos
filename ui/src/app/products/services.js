(function(angular){
    angular.module("pos.products.services", [
        "pos.common",
        "pos.auth.services",
        "pos.common.utils.services"
    ])
    .service("Pos.Products.Service", ["Restangular", "Pos.Auth.AuthService",
    "Pos.HelperService",
    function(api, AuthService, HelperService){
        var baseApi = api.all("pos").all("product_types");
        var orgId = AuthService.getUser().organization.id;
        // product types
        this.productTypes = {
            create: function(data){
                return baseApi.post(HelperService.addOrganization(data));
            },
            list: function(filters){
                var query_param = {
                    pos: orgId
                };
                _.extend(query_param, filters);
                return baseApi.customGET("", query_param);
            },
            get: function(productId){
                return baseApi.one("", productId).get();
            },
            update: function(productId, data){
                return baseApi.one("", productId).patch(data);
            }
        };
    }]);
})(angular);
