import React from "react";
import axios from "axios";
import {Card, Button} from "antd";

import CustomForm from './../components/Form';

class ArticleDetail extends React.Component {
  state = {
    article: {}
  };
  componentDidMount() {
    // каждый раз, когда загружается компонент, из джанго апи достается одна статья и помещается в состояние, и к которой есть доступ через this.state.  
    // this.props.match.params.articleID достает articleID из routers.js из строчки exact path="/articles/:articleID/"
    const articleID = this.props.match.params.articleID;
    axios.get(`http://127.0.0.1:8000/api/${articleID}`).then(res => {
      this.setState({
        article: res.data
      });
    });
  }
  handleDelete = (event) => {
    const articleID = this.props.match.params.articleID;
    axios.delete(`http://127.0.0.1:8000/api/${articleID}`)
    this.props.history.push('/');
    this.forceUpdate();
    // !!!  ПОДУМАТЬ О ТОМ, КАК МОЖНО ЭТО УЛУЧШИТЬ, ПРИ ПОМОЩИ REACT-ROUTER-DOM И REDUX !!! //
  }
  render() {
    return (
      <div>
        <Card title={this.state.article.title}>
          <p> {this.state.article.content} </p>
        </Card>
        <CustomForm 
        requestType='put'
        articleID={this.props.match.params.articleID}
        btnText="Update Post"
        />
        <form onSubmit={this.handleDelete}>
          <Button type="danger" htmlType="submit">Delete</Button>
        </form>
      </div>
    );
  }
}

export default ArticleDetail;
