
(function(angular) {
    'use strict';
    angular.module('pos.common.utils.forms', ['formly', 'formlyBootstrap'])
    .constant('formCheck', apiCheck())
    .config(function config(formlyConfigProvider, formCheck) {
        // set templates here
        formlyConfigProvider.setType({
            name: 'matchField',
            apiCheck: function(){
                return {
                    data: formCheck.shape({
                        fieldToMatch: formCheck.string
                    })
                };
            },
            apiCheckOptions: {
                prefix: 'matchField type'
            },
            defaultOptions: function matchFieldDefaultOptions(options) {
                return {
                    expressionProperties: {
                        'templateOptions.disabled': function(viewValue, modelValue, scope) {
                                var matchField = find(scope.fields, 'key', options.data.fieldToMatch);
                                if (!matchField) {
                                    throw new Error('Could not find a field for the key ' + options.data.fieldToMatch);
                                }
                                var model = options.data.modelToMatch || scope.model;
                                var originalValue = model[options.data.fieldToMatch];
                                var invalidOriginal = matchField.formControl && matchField.formControl.$invalid;
                                return !originalValue || invalidOriginal;
                            },
                        'data.validate': function(viewValue, modelValue, scope) {
                                if(scope.fc){
                                    scope.fc.$validate();
                                }
                            }
                    },
                    validators: {
                        fieldMatch: {
                            expression: function(viewValue, modelValue, fieldScope) {
                                var value = modelValue || viewValue;
                                var model = options.data.modelToMatch || fieldScope.model;
                                return value === model[options.data.fieldToMatch];
                            },
                            message: options.data.matchFieldMessage || '"Must match"'
                        }
                    }
                };
                function find(array, prop, value) {
                    var foundItem;
                    array.some(function(item) {
                        if (item[prop] === value) {
                            foundItem = item;
                        }
                        return !!foundItem;
                    });
                    return foundItem;
                }
            }
        });
        // datepicker
        formlyConfigProvider.setType({
            name: 'datepicker',
            template: '<input class="form-control" ng-model="model[options.key]" is-open="to.isOpen" datepicker-options="to.datepickerOptions" />',
            wrapper: ['bootstrapLabel', 'bootstrapHasError'],
            defaultOptions: {
                ngModelAttrs: (function(){
                    function camelize(string) {
                        string = string.replace(/[\-_\s]+(.)?/g, function(match, chr) {
                            return chr ? chr.toUpperCase() : '';
                        });
                        // Ensure 1st char is always lowercase
                        return string.replace(/^([A-Z])/, function(match, chr) {
                            return chr ? chr.toLowerCase() : '';
                        });
                    }
                    var attributes = [
                        'date-disabled',
                        'custom-class',
                        'show-weeks',
                        'starting-day',
                        'init-date',
                        'min-mode',
                        'max-mode',
                        'format-day',
                        'format-month',
                        'format-year',
                        'format-day-header',
                        'format-day-title',
                        'format-month-title',
                        'year-range',
                        'shortcut-propagation',
                        'datepicker-popup',
                        'show-button-bar',
                        'current-text',
                        'clear-text',
                        'close-text',
                        'close-on-date-selection',
                        'datepicker-append-to-body'
                    ];

                    var bindings = [
                        'datepicker-mode',
                        'min-date',
                        'max-date'
                    ];

                    var ngModelAttrs = {};

                    angular.forEach(attributes, function(attr) {
                        ngModelAttrs[camelize(attr)] = {attribute: attr};
                    });

                    angular.forEach(bindings, function(binding) {
                        ngModelAttrs[camelize(binding)] = {bound: binding};
                    });
                    return ngModelAttrs;
                })(),
                templateOptions:{
                    onFocus: function($viewValue, $modelValue, scope) {
                        scope.to.isOpen = !scope.to.isOpen;
                    },
                    datepickerOptions: {}
                }
            }
        }
        );

        //editable form fields
        formlyConfigProvider.setType({
            extends: 'input',
            template: '<div><span editable-text="model[options.key]" e-name="{{::id}}">{{ model[options.key] || "empty" }}</span></div>',
            name: 'editableInput'
        });

        formlyConfigProvider.setType({
            name: 'ui-select',
            extends: 'select',
            template: '<ui-select ng-model="model[options.key]" theme="bootstrap" ng-required="{{to.required}}" ng-disabled="{{to.disabled}}" reset-search-input="false"> <ui-select-match placeholder="{{to.placeholder}}"> {{$select.selected[to.labelProp || \'name\']}} </ui-select-match> <ui-select-choices group-by="to.groupBy" repeat="option[to.valueProp || \'value\'] as option in to.options | filter: $select.search"> <div ng-bind-html="option[to.labelProp || \'name\'] | highlight: $select.search"></div> </ui-select-choices> </ui-select>'
        });

        formlyConfigProvider.setType({
            name: 'ui-select-select2',
            extends: 'ui-select',
            template: '<ui-select ng-model="model[options.key]" theme="select2" ng-required="{{to.required}}" ng-disabled="{{to.disabled}}" reset-search-input="false"> <ui-select-match placeholder="{{to.placeholder}}"> {{$select.selected[to.labelProp || \'name\']}} </ui-select-match> <ui-select-choices group-by="to.groupBy" repeat="option[to.valueProp || \'value\'] as option in to.options | filter: $select.search"> <div ng-bind-html="option[to.labelProp || \'name\'] | highlight: $select.search"></div> </ui-select-choices> </ui-select>'
        });

        formlyConfigProvider.setType({
            name: 'ui-select-selectize',
            extends: 'ui-select',
            template: '<ui-select ng-model="model[options.key]" theme="selectize" ng-required="{{to.required}}" ng-disabled="{{to.disabled}}" reset-search-input="false"> <ui-select-match placeholder="{{to.placeholder}}"> {{$select.selected[to.labelProp || \'name\']}} </ui-select-match> <ui-select-choices group-by="to.groupBy" repeat="option[to.valueProp || \'value\'] as option in to.options | filter: $select.search"> <div ng-bind-html="option[to.labelProp || \'name\'] | highlight: $select.search"></div> </ui-select-choices> </ui-select>'
        });

        formlyConfigProvider.setWrapper({
            name: 'loading',
            templateUrl: 'common/tpls/form_select_loading.tpl.html'
        });
    });

})(angular);
