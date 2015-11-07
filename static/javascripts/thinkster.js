(function() {
    'use strict';
    
    angular
        .module('thinkster', [
            'thinkster.config',
            'thinkster.routes',
            'thinkster.authentication'
        ])
        .run(run);
        
    run.$inject = ['$http'];
        
    angular
        .module('thinkster.routes', ['ngRoute']);
    
    angular
        .module('thinkster.config', []);
    
    /**
    * @name run
    * @desc Update xsrf $http headers to align with Django's defaults
    */
    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CRSFToken';
        $http.defaults.xsrfCookieName = 'crsftoken'
    }
})();
