(function(angular){
    "use strict";

    describe("tests for home routes:", function() {

        var $state;

        beforeEach(function() {
            module("posApp");
            inject(function ( _$state_) {
                $state = _$state_;
            });
        });
        it("should respond to defaulted url", function () {
            expect($state.href("home", { id: 1 })).toEqual("/");
        });
    });

})(angular);
