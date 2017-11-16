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

      $http({
          method: 'GET',
          url: '/myapp/list/categorias'
      }).then(function successCallback(response) {
          _self.categories = response.data;
      });

      $http({
          method: 'GET',
          url: '/myapp/list/jingles'
      }).then(function successCallback(response) {
          _self.jingles = response.data;
      });

    };

    _self.botao = function(){

        var data = {login:'teste',nome:'teste',senha:'teste',email:'teste'};

        $http.post('/myapp/list/usuarios', data).then(function(response){
            _self.load();
        });

    };

    _self.deletarUsuario = function(userId){
        $http.delete('/myapp/list/usuarios/'+userId).then(function(response){
            _self.load();
        });
    };

    _self.deletarJingle = function(jingleId){
        $http.delete('/myapp/list/jingles/'+jingleId).then(function(response){
            _self.load();
        },function(response){
          alert(response.data.message);
        });
    };


    _self.load();

}

phonecatApp.controller('PhoneListController', PhoneListController);