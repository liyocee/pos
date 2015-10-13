(function (window) {
    "use strict";

    var setts = {
        "SERVER_URL": "{{server_url}}",
        "DEBUG": {{debug}},
        "ACTIONS": {
            "RESTRICT": []
        },
    };

    window.POS_SETTINGS= setts;

})(window);
