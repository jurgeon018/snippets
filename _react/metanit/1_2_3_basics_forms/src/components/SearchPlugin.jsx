class SearchPlugin extends React.Component{
    constructor(props){
      super(props);
      this.onTextChanged = this.onTextChanged.bind(this);
    }
    onTextChanged(e){
      var text = e.target.value.trim();
      this.props.filter(text);
    }
    render(){
      return <input placeholder="Поиск" onChange={this.onTextChanged}></input>
      
    }
  }

module.exports = SearchPlugin;