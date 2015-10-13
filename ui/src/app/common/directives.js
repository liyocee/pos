(function(angular){
    "use strict";
    angular.module("pos.common.directives", ["ngTable"])
    .directive("drfGrid", ["NgTableParams","PAGINATION_COUNT", function(NgTableParams, page_count){
        return {
            restrict: "EA",
            link: function(scope, elem, attrs){
                scope.$watchCollection(attrs.drfGrid,function(options){
                    var service = options.name[options.key];
                    var promise = options.key+"promise";
                    scope[promise] = service.list();
                    scope[options.key] = new NgTableParams({
                        page: 1,
                        count: page_count
                    }, {
                        total: 0,           // length of data
                        getData: function(params) {
                            var page = {
                                page: params.page(),
                                page_size: params.count(),
                                ordering: params.orderBy().join(",")
                            };
                            scope[promise] = service.list(page);
                            return scope[promise].then(
                                function(data){
                                    params.total(data.count);
                                    return data.results;
                                },
                                function(error){
                                    params.total(0);
                                    return [];
                                }
                            );
                        }
                    });
                });

            }
        };
    }]);
})(angular);
