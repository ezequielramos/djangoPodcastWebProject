var jingleApp = angular.module('jingleApp', ['bootstrap.fileField']);

var JingleController = function($scope, $http) {

    var _self = this;

    _self.load = function(){
		$http({
			method: 'GET',
			url: '/list/categorias'
		}).then(function successCallback(response) {
			_self.categorias = response.data;
		});
    };

    _self.saveJingle = function(){

        _self.jingle.docfile = _self.file;

        var fd = new FormData();

        fd.append("docfile", _self.file);

       	properties = Object.getOwnPropertyNames(_self.jingle);

       	properties.forEach(function(eachProperty){
       		fd.append(eachProperty, _self.jingle[eachProperty]);
       	});

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/list/jingles");
        xhr.send(fd);

        xhr.onreadystatechange = function () {
			if(xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
				document.location.href = 'index';
			}
		};

    };

    _self.load();

};

jingleApp.controller('JingleController', JingleController);