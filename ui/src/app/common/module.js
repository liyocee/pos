(function(angular){
    "use strict";
    angular.module("pos.common", [
        "ui.router",
        "pos.common.routes",
        "pos.common.utils",
        "pos.common.filters",
        "pos.common.services",
        "pos.common.directives"
    ]);

})(angular);
