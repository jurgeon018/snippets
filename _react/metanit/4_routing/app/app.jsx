var React = require('react');
var ReactDOM = require('react-dom');
// import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
var ReactRouterDOM = require('react-router-dom');

const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Switch = ReactRouterDOM.Switch;
const Link = ReactRouterDOM.Link;
const NavLink = ReactRouterDOM.NavLink;
const Redirect = ReactRouterDOM.Redirect;


var Phone = require('./components/Phone.jsx');
var Tablet = require('./components/Tablet.jsx');
var NotFound = require('./components/NotFound.jsx');
var About = require('./components/About.jsx');
var Main = require('./components/Main.jsx');
var Home = require('./components/Home.jsx');
var ProductsList = require('./components/ProductsList.jsx');






// // 4_1
ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={Main}></Route>
            <Route path='/about' component={About}></Route> // /about /about/ about/23432f
            <Route exact path='/about' component={About}></Route> // /about или /about/
            <Route strict path='/about' component={About}></Route> // только /about
            <Route path='/contact' children = { () => <h2>Contacts</h2> } ></Route>
            <Route component={NotFound}></Route>
        </Switch>
    </Router>,
    document.getElementById('app14')
)







// // 4_2 НЕ РАБОТАЕТ
// class Products extends React.Component{
//     render(){
//         return (
//         <div>
//             <h2>4_2</h2>
//             <h2>Товары</h2>
//             <Switch>
//                 <Route path="/products/phones" component={Phone} />  // НЕ РАБОТАЕТ ПЕРЕХОД НА ВТОРУЮ ССЫЛКУ
//                 <Route path="/products/tablets" component={Tablet} /> // НЕ РАБОТАЕТ ПЕРЕХОД НА ВТОРУЮ ССЫЛКУ
//             </Switch>
//         </div>
//         )
//     }
// }
// ReactDOM.render(
//     <Router>
//         <Switch>
//             <Route exact path="/" component={Home} />
//             <Route path="/about" component={About} /> 
//             <Route path="/products" component={Products} /> // НЕ РАБОТАЕТ
//             <Route component={NotFound} />
//         </Switch>
//     </Router>,
//     document.getElementById("app15")
// )







// 4_3_1 
class Nav extends React.Component{
    render(){
        return <nav>
                <Link to="/">Главная</Link>  
                <Link to="/about">О сайте</Link>  
                <Link to="/products">Товары</Link>
              </nav>;
    }
}
class Products3 extends React.Component{
    render(){
        return <div>
                    <h2>Товары</h2>
                </div>;
    }
}
ReactDOM.render(
    <Router>
        <div>
            <h2>4_3_1</h2>
            <Nav />
            <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/about" component={About} />
                <Route path="/products" component={Products3} />
                <Route component={NotFound} />
            </Switch>
        </div>
    </Router>,
    document.getElementById("app16")
)




// 4_3_2
class Nav2 extends React.Component{
    render(){
        return <nav>
                <NavLink exact to="/" activeStyle={{color:"green", fontWeight:"bold"}}>Главная</NavLink>
                {/* <NavLink exact to="/" activeClassName="active">Главная</NavLink>   */}
                <NavLink to="/about" activeClassName="active">О сайте</NavLink>  
                <NavLink to="/products" activeClassName="active">Товары</NavLink>
              </nav>;
    }
}

ReactDOM.render(
    <Router>
        <div>
            <h2>4_3_2</h2>
            <Nav2 />
            <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/about" component={About} />
                <Route path="/products" component={Products3} />
                <Route component={NotFound} />
            </Switch>
        </div>
    </Router>,
    document.getElementById("app17")
)












// // 4_4_1 ПЕРРЕХОД ПО ССЫЛКАМ - НЕ РАБОТАЕТ
// class About2 extends React.Component{
//     render(){
//         const id = this.props.match.params.id;
//         const name = this.props.match.params.name;
//         return <h2>id: {id} Name: {name}</h2>
//     }
// }

// class Product extends React.Component{
//     render(){
//         const prodId = this.props.match.params.id;
//         return <h2>Product # {prodId}</h2>
//     }
// }
// class Products extends React.Component{
//     render(){
//         return (
//             <div>
//                 <Switch>
//                     <Route exact path="/products" component={ProductsList}></Route>
//                     <Route path="/products/:id" component={Product}></Route>
//                 </Switch>
//             </div>
//         )
//     }
// }
// ReactDOM.render(
//     <Router>
//         <div>
//             <h2>4_4_1</h2>
//             <Switch>
//                 <Route exact path="/" component={Home}></Route>
//                 <Route path="/products" component={Products}></Route>
//                 <Route path="/about/:id/:name" component={About2}></Route>
//                 <Route component={NotFound}></Route>

//                 // Необязательные параметры
//                 // <Route path="about/:id?" component={About2} />
//                 // <Route path="about/:id?/:name?" component={About} />
//                 // Ограничения параметров через регулярки
//                 // <Route path="/products/:id(\d+)" component={Product} />
//                 // <Route path="/products/:id(\d{3}-\d{3}-\d{4})" component={Product} />
//             </Switch>
//         </div>
//     </Router>,
//     document.getElementById('app18')
// )
















// // 4_4_2 - НЕ РАБОТАЕТ
// class About3 extends React.Component{
//     render(){
//         const id = this.props.match.params.id;
//         const name = this.props.match.params.name;
//         return <h2>id: {id} Name: {name}</h2>
//     }
// }


// class Product2 extends React.Component{
//     render(){
//         const prodId = this.props.match.params.id;
//         const cat = this.props.match.params.category;
//         return <div>
//             <h2>Товар</h2>
//             <p>Категория {cat}</p>
//             <p>Идентификатор {prodId}</p>
//         </div>;
//     }
// }
// class Products2 extends React.Component{
//     render(){
//         return <div>
//             <Switch> 
//                 // сегментация параметров. В качестве разделителя можно использовать не только /
//                 <Route exact path="/products" component={ProductsList} />
//                 <Route path="/products/:category-:id" component={Product2} />
//             </Switch>
//         </div>;
//     }
// }
// ReactDOM.render(
//     <Router>
//         <div>
//             <Switch>
//                 <Route exact path="/" component={Home}></Route>
//                 <Route path="/products" component={Products2}></Route>
//                 <Route path="/about/:id/:name" component={About}></Route>
//                 <Route component={NotFound}></Route>
//             </Switch>
//         </div>
//     </Router>,
//     document.getElementById('app19')
// )


















// // 4_5
const phones =[
                {id: 1, name: "iPhone 7"}, 
                {id: 2, name: "Google Pixel"}, 
                {id: 3, name: "HTC U Ultra"} 
            ];

class ProductsList2 extends React.Component{
render(){
    return <div>
            <h2>Список товаров</h2>
            <ul>
            {
                phones.map(function(item){
                    return <li key={item.id}>
                                <NavLink to={`/products/${item.id}`}>{item.name}</NavLink>
                            </li>
                })
            }
        </ul>
    </div>;
}
}
class Product extends React.Component{
    render(){
        const prodId = this.props.match.params.id;
        let phone;
        for(var i=0; i<phones.length; i++){
            if(phones[i].id==prodId){
                phone = phones[i];
                break;
            }
        }
        if(phone===undefined)
            return <h2>Товар не найден</h2>;
        else
            return <h2>Товар {phone.name}</h2>;
    }
}
class Products2 extends React.Component{
    render(){
        return <div>
                    <Switch>
                        <Route exact path="/products" component={ProductsList2} />
                        <Route path="/products/:id" component={Product} />
                    </Switch>
                </div>;
    }
}
ReactDOM.render(
    <Router>
        <div>
            <nav>
                <Link to="/">Main</Link> | 
                <Link to="/about">About</Link> | 
                <Link to="/products">Products</Link>
             </nav>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/about" component={About} />
                <Route path="/products" component={Products2} />
                <Route component={NotFound} />
            </Switch>
        </div>
    </Router>,
    document.getElementById("app20")
)




// 4_6
class Home2 extends React.Component{
    render(){
        return <div>
                    <h2>Главная</h2>
                    <p>Match:   {JSON.stringify(this.props.match)}</p>
                    <p>Location {JSON.stringify(this.props.location)}</p>
                    <p>Id:      {this.props.match.params.id}</p>
                    <p>Name:    {new URLSearchParams(this.props.location.search).get("name")}</p>
                    <p>Age:     {new URLSearchParams(this.props.location.search).get("age")}</p>
                </div>;
    }
}
ReactDOM.render(
    <Router>
        <div>
            <nav>
                <Link to="/1/?name=Andrew&age=21">Andrew</Link> | 
                <Link to="/2/?name=Bob&age=23">Bob</Link> | 
                <Link to="/3/?name=Tim&age=33">Tim</Link>
            </nav>
            <Switch>
                <Route path="/:id?" component={Home2} />
            </Switch>
        </div>
    </Router>,
    document.getElementById("app21")
)






// // 4_7_1
class New1 extends React.Component{
    render(){
        return <h2>New</h2>;
    }
}

ReactDOM.render(
    <Router>
        <div>
            <nav>
                <Link to="/">Home</Link> | 
                <Link to="/old">Old</Link> |
                <Link to="/new">New</Link>
            </nav>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/new" component={New1} />
                <Redirect from="/old" to="/new" />
            </Switch>
        </div>
    </Router>,
    document.getElementById("app22")
)




// 4_7_2
class New2 extends React.Component{
    render(){
        return <h2>New {this.props.match.params.id}</h2>;
    }
}
class Old extends React.Component{
    render(){
        return <Redirect to={`/new/${this.props.match.params.id}`} />;
    }
}
ReactDOM.render(
    <Router>
        <div>
            <nav>
                <Link to="/">Home</Link> | 
                <Link to="/old/123">Old</Link> |
                <Link to="/new/456">New</Link>
            </nav>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/new/:id" component={New2} />
                <Route path="/old/:id" component={Old} />   
            </Switch>
        </div>
    </Router>,
    document.getElementById("app23")
)



// 4_7_3
let logged = false;
class Home3 extends React.Component{
    render(){
        if(logged==true)
            return <h2>Welcome</h2>;
        return <Redirect to="/login" />;
    }
}
class Login extends React.Component{
    render(){
        logged = true;
        return <h2>Login</h2>;
    }
}

ReactDOM.render(
    <Router>
        <div>
            <nav>
                <Link to="/">Home</Link> | 
                <Link to="/login">Login</Link>
            </nav>
            <Switch>
                <Route exact path="/" component={Home3} />
                <Route path="/login" component={Login} />               
            </Switch>
        </div>
    </Router>,
    document.getElementById("app24")
)