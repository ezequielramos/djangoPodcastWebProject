// Define the `phonecatApp` module
var phonecatApp = angular.module('phonecatApp', []);

// Define the `PhoneListController` controller on the `phonecatApp` module

var PhoneListController = function($scope, $http) {

    var _self = this;

    _self.load = function(){

      $http({
          method: 'GET',
          url: '/myapp/list/usuarios'
      }).then(function successCallback(response) {
          _self.users = response.data;
      });

    };

    _self.botao = function(){

        var data = {login:'teste',nome:'teste',senha:'teste',email:'teste'};

        $http.post('/myapp/list/usuarios', data).then(function(response){
            _self.load();
        });

    };

    _self.load();

}

phonecatApp.controller('PhoneListController', PhoneListController);