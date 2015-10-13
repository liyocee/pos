(function(angular){
    angular.module("pos.products.forms.product", [
        "pos.common",
        "pos.products.services"
    ])

    .service("Pos.Products.Form.Product", [function(){
        var formFields = function(options){
            return [
                {
                    key: "name",
                    type: "input",
                    templateOptions: {
                        placeholder: "Name ",
                        label: "Product Name:",
                        required:true
                    }
                }
            ];
        };
        this.getForm = function(options){
            return formFields(options);
        };

    }]);
})(angular);
