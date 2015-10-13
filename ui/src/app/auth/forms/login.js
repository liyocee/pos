(function(angular){
    angular.module("pos.auth.forms.login", ["pos.common.utils.forms"])

    .service("Pos.Form.Login", function(){
        var formFields = function(options){
            return [
                {
                    key: "username",
                    type: "input",

                    templateOptions: {
                        placeholder: "Username",
                        label: "Username:",
                        required:true
                    }

                },
                {
                    key: "password",
                    type: "input",
                    templateOptions: {
                        placeholder: "Password",
                        type: "password",
                        label: "Password:",
                        required:true
                    }

                },
                {
                    key: "keepMeLogged",
                    type: "checkbox",
                    templateOptions: {
                        label: "Keep me logged in",
                        required:false
                    }

                }
            ];
        };
        this.getForm = function(options){
            return formFields(options);
        };

    });
})(angular);
