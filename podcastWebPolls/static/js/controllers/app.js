// Define the `phonecatApp` module
var phonecatApp = angular.module('phonecatApp', []);

// Define the `PhoneListController` controller on the `phonecatApp` module

var PhoneListController = function($scope, $http) {

    var _self = this;

    _self.load = function(){

      $http({
          method: 'GET',
          url: '/list/usuarios'
      }).then(function successCallback(response) {
          _self.users = response.data;
      });

      $http({
          method: 'GET',
          url: '/list/categorias'
      }).then(function successCallback(response) {
          _self.categories = response.data;
      });

      _self.curtir = function(jingle){

          temp = jingle.favoritado;

          jingle.favoritado = !jingle.favoritado;

          if(jingle.favoritado){
              $http.post('/list/favorito', {usuario_id:_self.login,jingle_id:jingle.id}).then(function(response){
                _self.load();
              });
          }else{
              $http.delete('/list/favorito/' + temp, {}).then(function(response){
                _self.load();
              });
          }
      };

      $http({
          method: 'GET',
          url: '/list/jingles'
      }).then(function successCallback(response) {
          _self.jingles = response.data;
          _self.jingles.forEach(function(eachJingle){
              eachJingle.favoritado = false;
              $http({
                  method: 'GET',
                  url: '/list/favorito/' + eachJingle.id
              }).then(function successCallback(response) {
                  eachJingle.favoritado = response.data.id;
              });
          });
      });

      $http({
          method: 'GET',
          url: '/list/login'
      }).then(function successCallback(response) {
          _self.login = response.data.id;
      });

    };

    _self.botao = function(){

        var data = {login:'teste',nome:'teste',senha:'teste',email:'teste'};

        $http.post('/list/usuarios', data).then(function(response){
            _self.load();
        });

    };

    _self.logout = function(){
        $http.post('/list/logout', {}).then(function(response){
            _self.load();
        });
    };

    _self.teste = function(a){

      if(_self.playing){
        document.getElementById('jingle-'+_self.playing).pause();
      }

      if(a==_self.playing){
        _self.playing = null
        return;
      }

      _self.playing = a;
      document.getElementById('jingle-'+_self.playing).play();
    }

    _self.deletarUsuario = function(userId){
        $http.delete('/list/usuarios/'+userId).then(function(response){
            _self.load();
        });
    };

    _self.deletarJingle = function(jingleId){
        $http.delete('/list/jingles/'+jingleId).then(function(response){
            _self.load();
        },function(response){
          alert(response.data.message);
        });
    };

    _self.playing = null;

    _self.load();

};

phonecatApp.controller('PhoneListController', PhoneListController);