var Reflux = require("reflux");
var Actions = require("./actions.jsx");
 
class PhonesStore extends Reflux.Store {
    constructor()
    {
        super();
        this.state = {phones: ["iPhone 7", "Samsung Galaxy S8"]};
         
        this.listenTo(Actions.addItem, this.onAddItem);
        this.listenTo(Actions.removeItem, this.onRemoveItem);
    }
     
    onAddItem(phone){
         
        this.state.phones.push(phone);
    }
    onRemoveItem(phone){
         
        var data = this.state.phones;
        var index = data.indexOf(phone);
        if (index > -1) {
            data.splice(index, 1);
            this.setState({phones: data});
        }
    }
}
 
module.exports = PhonesStore;