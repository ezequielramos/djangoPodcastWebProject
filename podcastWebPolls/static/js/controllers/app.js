// Define the `phonecatApp` module
var phonecatApp = angular.module('phonecatApp', []);

// Define the `PhoneListController` controller on the `phonecatApp` module

PhoneListController = function($scope, $http) {

    _self = this;

    _self.load = function(){

      $http({
          method: 'GET',
          url: '/myapp/list/usuarios'
      }).then(function successCallback(response) {
          _self.users = response.data;
      });

    };

    _self.botao = function(){

        data = {login:'teste',nome:'teste',senha:'teste',email:'teste'};

        $http.post('/myapp/list/usuarios', data).then(function(response){
            _self.load();
        });

    }

    _self.load();

}

phonecatApp.controller('PhoneListController', PhoneListController);