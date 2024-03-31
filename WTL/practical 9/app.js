
var myApp = angular.module("myApp", []);

myApp.service("ContactService", function () {
    var uid = 1;
    var contacts = [
        {
            id: 0,
            name: 'Prathamesh',
            email: 'prathamesh@gmail.com',
            password: '123456', // **Placeholder, replace with secure password hashing**
            phone: '123456789',
            age: '21'
        }
    ];


    // Save Service for saving new contact and saving existing edited contact.
    this.save = function (contact) {
        if (contact.id == null) {
            contact.id = uid++;
            contacts.push(contact);
        } else {
            for (var i in contacts) {
                if (contacts[i].id == contact.id) {
                    contacts[i] = contact;
                }
            }
        }
    };

    // Search for a contact
    this.get = function (id) {
        for (var i in contacts) {
            if (contacts[i].id == id) {
                return contacts[i];
            }
        }
    };

    // Delete a contact
    this.delete = function (id) {
        for (var i in contacts) {
            if (contacts[i].id == id) {
                contacts.splice(i, 1);
            }
        }
    };

    // Show all contacts
    this.list = function () {
        return contacts;
    };
});

myApp.controller("MainController", function ($scope, ContactService) {
    $scope.isLogin = true;
    $scope.contacts = ContactService.list();
    $scope.loginData = {};
    $scope.ifSearchUser = false;
    $scope.title = "List of Users";

    $scope.toggleForm = function () {
        $scope.isLogin = !$scope.isLogin;
    };

    $scope.login = function () {
        const foundUser = $scope.contacts.find(
            user => user.email === $scope.loginData.email && user.password === $scope.loginData.password // Use simple comparison for now
        );

        if (foundUser) {
            localStorage.setItem('currentUser', JSON.stringify(foundUser));
            $scope.isLogin = false;
            alert("Login successful!");
        } else {
            alert("Invalid email or password.");
        }
    };

    $scope.logout = function () {
        localStorage.removeItem('currentUser');
        $scope.isLogin = true;
        alert("Logout successful!");
    }

    $scope.reset = function () {
        $scope.newcontact = {};
    };

    $scope.saveContact = function () {
        if (!$scope.newcontact || !$scope.newcontact.name || !$scope.newcontact.email || !$scope.newcontact.password) {
            alert("Please fill in all required fields.");
            return;
        }
        ContactService.save($scope.newcontact);
        $scope.newcontact = {};
    };

    $scope.delete = function (id) {
        ContactService.delete(id);
        if ($scope.newcontact != undefined && $scope.newcontact.id == id) {
            $scope.newcontact = {};
        }
    };

    $scope.edit = function (id) {
        $scope.newcontact = angular.copy(ContactService.get(id));
    };

    $scope.searchUser = function () {
        $scope.ifSearchUser = !$scope.ifSearchUser;
        $scope.title = $scope.ifSearchUser ? "Back" : "List of Users";
    };

    var contacts = ContactService.list(); // Define contacts variable

    $scope.loginData = {};

    $scope.login = function () {
        const foundUser = contacts.find(
            user => user.email === $scope.loginData.email && user.password === $scope.loginData.password // Use simple comparison for now
        );

        if (foundUser) {
            localStorage.setItem('currentUser', JSON.stringify(foundUser));
            $scope.isLogin = false;
            alert("Login successful!");
        } else {
            alert("Invalid email or password.");
        }
    };

    $scope.logout = function () {
        localStorage.removeItem('currentUser');
        $scope.isLogin = true;
        alert("Logout successful!");
    }

});
