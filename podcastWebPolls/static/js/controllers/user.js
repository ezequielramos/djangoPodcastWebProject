// Define the `userApp` module
var userApp = angular.module('userApp', []);

// Define the `UserController` controller on the `userApp` module

var UserController = function($scope, $http) {

    var _self = this;

    _self.saveUser = function(){

        $http.post('/list/usuarios', _self.user).then(function(response){
            alert("salvo com sucesso");
        });
    }

    _self.login = function(){
    	console.info('aaa');
    }

};

userApp.controller('UserController', UserController);