(function(angular){
    angular.module("pos.auth.forms.registration", ["pos.common"])

    .service("Pos.Organization.Form.Registration", function(){
        var registrationFormFields = function(options){
            return [
                {
                    key: "first_name",
                    model: options.profile.model,
                    type: "input",
                    templateOptions: {
                        placeholder: "Company Name",
                        label: "Company Name:",
                        type: "text",
                        required:true
                    }
                },
                {
                    key: "email",
                    model: options.profile.model,
                    type: "input",
                    templateOptions: {
                        placeholder: "Company Email",
                        type: "email",
                        label: "Company Email:",
                        required:true
                    }

                },
                {
                    key: "password",
                    model: options.profile.model,
                    type: "input",
                    templateOptions: {
                        placeholder: "Password",
                        type: "password",
                        label: "Password:",
                        required:true
                    }

                },
                {
                    key: "confirmPassword",
                    optionsTypes: ["matchField"],
                    model: options.password.model,
                    type: "input",
                    templateOptions: {
                        "type": "password",
                        "label": "Confirm Password",
                        "placeholder": "Please re-enter your password",
                        "required": true
                    },
                    data: {
                        "fieldToMatch": "password",
                        "modelToMatch": options.profile.model,
                        "matchFieldMessage": "$viewValue + \" does not match \" + options.data.modelToMatch.email"
                    }
                },
                {
                    key: "terms_of_use",
                    type: "checkbox",
                    templateOptions: {
                        label: "I Agree to Terms of use.",
                        required:true
                    }

                }
            ];
        };
        this.getForm = function(options){
            return registrationFormFields(options);
        };

    });
})(angular);
