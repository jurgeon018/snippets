import React from "react";
import axios from "axios";
import {Card} from "antd";


class ArticleDetail extends React.Component {
  state = {
    article: {}
  };
  // работает как requests в python. Помещает в состояние статьи, которые достаются из джанго-апи.
  // каждый раз, когда загружается компонент, из джанго апи достается одна статья и помещается в состояние, и к которой есть доступ через this.state.  
  componentDidMount() {
    // this.props.match.params.articleID достает articleID из routers.js из строчки exact path="/articles/:articleID/"
    const articleID = this.props.match.params.articleID;
    axios
    .get(`http://127.0.0.1:8000/api/${articleID}`)
    .then(res => {
      this.setState({
        article: res.data
      });
    });
  }
  render() {
    return (
      <div>
        <Card title={this.state.article.title}>
          <p> {this.state.article.content} </p>
        </Card>
      </div>
    );
  }
}

export default ArticleDetail;
