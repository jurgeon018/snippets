'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var user = {
    id: 5,
    age: 33,
    firstName: 'Tom',
    lastName: 'Smith',
    getFullName: function getFullName() {
        return this.firstName + ' ' + this.lastName;
    }
};

var userClassName = 'user-info';

var styleObj = {
    color: 'red',
    fontFamily: 'Verdana'
};

var Hello = function (_React$Component) {
    _inherits(Hello, _React$Component);

    function Hello() {
        _classCallCheck(this, Hello);

        return _possibleConstructorReturn(this, (Hello.__proto__ || Object.getPrototypeOf(Hello)).apply(this, arguments));
    }

    _createClass(Hello, [{
        key: 'render',
        value: function render() {
            return React.createElement(
                'div',
                { 'class': userClassName, style: styleObj },
                'Hello react',
                React.createElement(
                    'p',
                    null,
                    'id: ',
                    user.id
                ),
                React.createElement(
                    'p',
                    null,
                    '\u041F\u043E\u043B\u043D\u043E\u0435 \u0438\u043C\u044F: ',
                    user.getFullName()
                ),
                React.createElement(
                    'p',
                    null,
                    '\u0412\u043E\u0437\u0440\u0430\u0441\u0442: ',
                    user.age
                ),
                React.createElement(
                    'p',
                    null,
                    '\u0412\u0440\u0435\u043C\u044F \u0433\u0435\u043D\u0435\u0440\u0430\u0446\u0438\u0438 \u0434\u0430\u043D\u043D\u044B\u0445: ',
                    new Date().toLocaleTimeString()
                )
            );
        }
    }]);

    return Hello;
}(React.Component);

ReactDOM.render(React.createElement(Hello, null), document.getElementById('app'));
