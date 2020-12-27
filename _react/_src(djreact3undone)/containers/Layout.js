import React from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Link } from 'react-router-dom';

const { Header, Content, Footer } = Layout;

class CustomLayout extends React.Component {
  render() {
    return (
      <Layout className="layout">
        <Header>
          <div className="logo" />
          <Menu
            theme="dark" mode="horizontal"
            defaultSelectedKeys={['2']} 
            style={{ lineHeight: '64px' }}
          > 


            {
              this.props.isAuthenticated 
              ?
              <Menu.Item key="2">
                Login
              </Menu.Item>
               :
              <Menu.Item key="2">
                <Link to="/login">Login</Link>
              </Menu.Item>
            }
            <Menu.Item key="1">
              <Link to="/">Posts</Link>
            </Menu.Item>
            
          </Menu>
        </Header>
        <Content style={{ padding: '0 50px' }}>
          <Breadcrumb style={{ margin: '16px 0' }}>
            <Breadcrumb.Item>

              {/*вручную*/}
              <Link to="/">Home</Link>
              {/*вручную*/}

            </Breadcrumb.Item>
            <Breadcrumb.Item>

              {/*вручную*/}
              <Link to="/">List</Link>
              {/*вручную*/}

            </Breadcrumb.Item>
          </Breadcrumb>
          <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>

            {/*вручную
              {this.props.children} будет отображать все что будет передано в CustomLayout из App, но не в виде агрумента, а в виде тэга, который оборачивается в CustomLayot. 
            */}
            {this.props.children} 
            {/* вручную */}
            {/*
              this.props.children в данном случае отобращает статьи, вмещает в себя BaseRouter.Это то же самое, что импортировать
              import BaseRouter from './../routers'; 
              и заменить {this.props.children} на <BaseRouter/> 
            */}

          </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          Ant Design ©2016 Created by Ant UED
                </Footer>
      </Layout>
    );
  }
}

export default CustomLayout;