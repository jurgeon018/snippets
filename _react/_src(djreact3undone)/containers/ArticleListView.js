import React from "react";
import axios from "axios";

// import { List, Avatar, Icon } from "antd"; // нужно, если не импортировать шаблон для статей, а вставлять его в файл напрямую
import Articles from './../components/Article'
import CustomForm from './../components/Form'

class ArticleList extends React.Component {
  state = {
    articles: []
  };
  // работает как requests в python. Помещает в состояние статьи, которые достаются из джанго-апи.
  // каждый раз, когда загружается компонент, из джанго апи достаются все статьи и помещаются в состояние, и к которым есть доступ через this.state.  
  componentDidMount() {
    axios.get("http://127.0.0.1:8000/api/").then(res => {
      this.setState({
        articles: res.data
      });
      console.log('"res.data":',res.data)
    });
  }

  render() {
    return (
      <div>
          {/* А можно перенести тэг <List></List> из шаблона для списка статей сюда и не импортировать его, и заменить в нем props.data на this.state.articles */}
          {/* А можно писать так: */}
        <Articles data={this.state.articles} /> 
        <br />
        <h2>Create an article</h2>
        {/* CustomForm component is what will be used as a form on CreateView and UpdateView. We need to handle when that form is submitted. We need to specify when we are going to create something(POST), and when we are going to update something(PUT) */}
        <CustomForm 
          requestType="post"
          articleID={null}
          btnText="Add Post"
        />
      </div>
    );
  }
}

export default ArticleList;
