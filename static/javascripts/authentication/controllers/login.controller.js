/**
* LoginController
* @namespace thinkster.authentication.controllers
*/
(function() {
    'use strict';
    
    angular
        .module('thinkster.authentication.controllers')
        .controller('LoginController', LoginController);
        
    LoginController.$inject = ['$location', '$scope', 'Authentication'];
    
    /**
    * @namespace LoginController
    */
    function LoginController($location, $scope, Autentication) {
        var vm = this;
        
        vm.login = login;
        
        activate();
        
        /**
        * @name activate
        * @desc Actions to be performed when this controller is instantiated
        * @memberOf thinkster.authentication.controllers.LoginController
        */
        function activate() {
            // If the user is authenticated, they should not be here
            if (Autentication.isAuthenticated()) {
                $location.url('/');
            }
        }
        
        /**
        * @name login
        * @desc Log the user in
        * @memberOf thinkster.authentication.controllers.LoginController
        */
        function login() {
            Autentication.login(vm.email, vm.password);
        }
    }
})();