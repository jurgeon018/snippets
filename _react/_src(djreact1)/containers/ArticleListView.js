import React from "react";
import axios from "axios";
import { List, Avatar, Icon } from "antd";

const IconText = ({ type, text }) => (
  <span>
    <Icon
      type={type}
      style={{
        marginRight: 8
      }}
    />
    {text}
  </span>   
);

class ArticleList extends React.Component {
  state = {
    articles: []
  };
  // работает как requests в python. Помещает в состояние статьи, которые достаются из джанго-апи.
  // каждый раз, когда загружается компонент, из джанго апи достаются все статьи и помещаются в состояние, и к которым есть доступ через this.state.  
  componentDidMount() {
    axios
    .get("http://127.0.0.1:8000/api/")
    .then(res => {
      this.setState({
        articles: res.data
      });
      console.log('"res.data":',res.data)
    });
  }

  render() {
    return (
      <div>
          {/* Можно писать так: */}
        {/* <Articles data={this.state.articles} /> <br /> */}
          {/* А можно перенести шаблон для списка статей сюда и не импортировать его, и писать так: */}
        <List
      itemLayout="vertical"
      size="large"
      pagination={{
        onChange: page => {
          console.log(page);
        },
        pageSize: 1
      }}
      // Что делают dataSource и renderItem? загадка.
      // dataSource={props.data} // нужно, если импортировать шаболон для списка статей из другого файла
      dataSource={this.state.articles}
      renderItem={item => (
        <List.Item
          key={item.title}
          actions={[
            <IconText type="star-o" text="156" />,
            <IconText type="like-o" text="156" />,
            <IconText type="message" text="2" />
          ]}
          extra={
            <img
              width={272}
              alt="logo"
              src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
            />
          }
        >
          <List.Item.Meta
            avatar={<Avatar src={item.avatar} />}
            title={<a href={`/articles/${item.id}`}> {item.title} </a>}
            description={item.description}
          />
          {item.content}
        </List.Item>
      )}
    />
      </div>
    );
  }
}

export default ArticleList;
