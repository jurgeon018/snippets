import React from "react";
import { Form, Input, Button } from "antd";
import axios from 'axios';

const FormItem = Form.Item;

class CustomForm extends React.Component {
  handleFormSubmit = (event, requestType, articleID) => {
    // prevents page from reloading, when the form is submited
    // event.preventDefault() // Когда убираешь эту кнопку, то страница перезагружается, но новая статья не добавляется, а должна добавляться.
    const title = event.target.elements.title.value;
    const content = event.target.elements.content.value;
    console.log(title, content);
    switch(requestType){
      case 'post':
        return axios.post('http://127.0.0.1:8000/api/', {
            title: title,
            content: content
          })
        .then(res => console.log(res))
        .catch(error => console.error(error));
      
      case 'put':
        return axios.put(`http://127.0.0.1:8000/api/${articleID}/`, {
            title: title,
            content: content
          })
        .then(res => console.log(res))
        .catch(error => console.error(error));
        
    }
  }
  
  render() {
    return (
      <div>
        <Form
         onSubmit={ (event) => this.handleFormSubmit(
                                        event, 
                                        this.props.requestType, 
                                        this.props.articleID
          )}
        >
          <FormItem label="Title">
            <Input 
            // we need the name of an input, so we can get in in handleFormSubmit through the event.target.elements , when the form is being submited
             name="title" 
             placeholder="Put a title here" />
          </FormItem>
          <FormItem label="Content">
            <Input 
             name="content" 
             placeholder="Enter some content ..." />
          </FormItem>
          <FormItem>
            {/* To handle the submiting be need to specify htmlType  */}
            <Button 
              type="primary" // styling
              htmlType="submit" // means that type of button is submit
            >
              {this.props.btnText}
            </Button>
          </FormItem>
        </Form>
      </div>
    );
  }
}

export default CustomForm;
