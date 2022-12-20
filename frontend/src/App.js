
import './App.css';
import Home from './Components/Home';
import NavBar from './Components/NavBar';
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
  return (
    <div className="App">
      <NavBar/>
      <BrowserRouter> 
        <Routes>
        <Route exact path={"/"} element={<Home/>}/> 
        </Routes>
        {/* <Alert/> */}
      </BrowserRouter>
    </div>
  );
}

export default App;
