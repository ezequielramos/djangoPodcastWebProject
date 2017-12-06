var userApp = angular.module('userApp', []);

var UserController = function($scope, $http) {

    var _self = this;

    _self.saveUser = function(){

        $http.post('/list/usuarios', _self.user).then(function(response){
            document.location.href = 'login'
        });
    }

    _self.login = function(){
    	$http.post('/list/login', _self.user).then(function(response){
            document.location.href = 'index'
        },function(response){
            alert(response.data.message);
        });
    }

};

userApp.controller('UserController', UserController);