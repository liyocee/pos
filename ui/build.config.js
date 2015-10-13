/**
 * This file/module contains all configuration for the build process.
 */
module.exports = {
    /**
     * The `build_dir` folder is where our projects are compiled during
     * development and the `compile_dir` folder is where our app resides once it"s
     * completely built.
     */
    build_dir: "build",
    compile_dir: "bin",


    /**
     * custom settings file
     */
    settings_file: "settings.js",


    /**
     * This is a collection of file patterns that refer to our app code (the
     * stuff in `src/`). These file paths are used in the configuration of
     * build tasks. `js` is all project javascript, less tests. `ctpl` contains
     * our reusable components" (`src/common`) template HTML files, while
     * `atpl` contains the same, but for our app"s code. `html` is just our
     * main HTML file, `less` is our main stylesheet, and `unit` contains our
     * app"s unit tests.
     */
    app_files: {
        js: [ "src/**/*.js", "!src/**/*.spec.js", "!src/assets/**/*.js", "!src/<%= settings_file %>" ],
        jsunit: [ "src/**/*.spec.js" ],

        coffee: [ "src/**/*.coffee", "!src/**/*.spec.coffee" ],
        coffeeunit: [ "src/**/*.spec.coffee" ],

        atpl: [ "src/app/**/*.tpl.html" ],
        ctpl: [ "src/common/**/*.tpl.html" ],

        html: [ "src/index.html" ],
        less: "src/less/main.less"
    },

    /**
     * This is a collection of files used during testing only.
     */
    test_files: {
        js: [
            "vendor/angular-mocks/angular-mocks.js"
        ]
    },

    /**
     * This is the same as `app_files`, except it contains patterns that
     * reference vendor code (`vendor/`) that we need to place into the build
     * process somewhere. While the `app_files` property ensures all
     * standardized files are collected for compilation, it is the user"s job
     * to ensure non-standardized (i.e. vendor-related) files are handled
     * appropriately in `vendor_files.js`.
     *
     * The `vendor_files.js` property holds files to be automatically
     * concatenated and minified with our project source files.
     *
     * The `vendor_files.css` property holds any CSS files to be automatically
     * included in our app.
     *
     * The `vendor_files.assets` property holds any assets to be copied along
     * with our app"s assets. This structure is flattened, so it is not
     * recommended that you use wildcards.
     */
    vendor_files: {
        js: [
            "vendor/admin-lte/plugins/jQuery/jQuery-2.1.4.min.js",
            "vendor/jquery-ui/jquery-ui.min.js",
            "vendor/api-check/dist/api-check.js",
            "vendor/angular/angular.js",
            "vendor/restangular/dist/restangular.js",
            "vendor/angular-formly/dist/formly.js",
            "vendor/angular-formly-templates-bootstrap/dist/angular-formly-templates-bootstrap.js",
            "vendor/underscore/underscore.js",
            "vendor/admin-lte/bootstrap/js/bootstrap.js",
            "vendor/angular-toastr/dist/angular-toastr.js",
            "vendor/angular-ui-select/dist/select.js",
            "vendor/angular-animate/angular-animate.js",
            "vendor/angular-cookies/angular-cookies.js",
            "vendor/angular-resource/angular-resource.js",
            "vendor/angular-ui-router/release/angular-ui-router.js",
            "vendor/angular-bootstrap/ui-bootstrap.js",
            "vendor/angular-bootstrap/ui-bootstrap-tpls.js",
            "vendor/moment/moment.js",
            "vendor/angular-xeditable/dist/js/xeditable.js",
            "vendor/admin-lte/plugins/sparkline/jquery.sparkline.js",
            "vendor/admin-lte/plugins/jvectormap/jquery-jvectormap-1.2.2.min.js",
            "vendor/admin-lte/plugins/jvectormap/jquery-jvectormap-world-mill-en.js",
            "vendor/admin-lte/plugins/datepicker/bootstrap-datepicker.js",
            "vendor/admin-lte/plugins/daterangepicker/daterangepicker.js",
            "vendor/admin-lte/plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.all.min.js",
            "vendor/admin-lte/plugins/slimScroll/jquery.slimscroll.min.js",
            "vendor/admin-lte/plugins/fastclick/fastclick.min.js",
            "vendor/toastr/toastr.js",
            "vendor/angular-busy/dist/angular-busy.js",
            "vendor/ng-table/dist/ng-table.js",
            "vendor/admin-lte/dist/js/app.js",
            "src/assets/js/*"
        ],
        css: [
        ],
        assets: {
            fontawesome: "vendor/fontawesome/fonts/*",
            glyphicons: "vendor/admin-lte/bootstrap/fonts/*",
            ionicons: "vendor/ionicons/fonts/*",
            css:[
            ],
            imgs: [
                "src/assets/img/*",
                "vendor/admin-lte/dist/img/*"
            ]
        }
    },

    connect : {
        options: {
            port: 8012,
            hostname: "*",
            keepalive: true,
            middleware: function (connect, options, middlewares) {
                var modRewrite = require("connect-modrewrite");
                middlewares.unshift(modRewrite(["^[^\\.]*$ /index.html [L]"]));
                return middlewares;
            }
        },
        dev: {
            options: {
                base: "build"
            }
        },
        prod: {
            options: {
                base: "bin"
            }
        }
    }
};
