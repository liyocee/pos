(function(angular){
    angular.module("pos.agents.forms.agent", [
        "pos.common",
        "pos.agents.services"
    ])

    .service("Pos.Agents.Form.Agent", function(){
        var registrationFormFields = function(options){
            return [
                {
                    key: "first_name",
                    model: options.profile.model,
                    type: "input",
                    templateOptions: {
                        placeholder: "Agent First Name",
                        label: "Agent Name:",
                        type: "text",
                        required:true
                    }
                },
                {
                    key: "last_name",
                    model: options.profile.model,
                    type: "input",
                    templateOptions: {
                        placeholder: "Agent Last Name",
                        label: "Agent Last Name:",
                        type: "text",
                        required:true
                    }
                },
                {
                    key: "email",
                    model: options.profile.model,
                    type: "input",
                    templateOptions: {
                        placeholder: "Agent Email",
                        type: "email",
                        label: "Agent Email:",
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
                        label: "Agent Password:",
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
                }
            ];
        };
        this.getForm = function(options){
            return registrationFormFields(options);
        };

    });
})(angular);
