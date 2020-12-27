var React = require('react');

//////////// 2_1, 2_2
function tick(){
    ReactDOM.render(
        <div>
            <h2>Текущее время: {new Date().toLocaleTimeString()}</h2>
        </div>,
        document.getElementById('app2')
    )
};
setInterval(tick, 1000); // Через 1 секунду перезаписывает поле app2
class App2 extends React.Component{
    render(){
        return(
            <div>
                <h2>App2</h2>
                <h2>This component will be rewritten by Ticker after 1 second.</h2>
            </div>
        )
    }
}
module.exports =  App2;
