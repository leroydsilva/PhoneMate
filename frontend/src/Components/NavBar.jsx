import React, { useState } from 'react'
import {GiHamburgerMenu} from 'react-icons/gi'
import {MdClose} from 'react-icons/md'
import {ImSun} from 'react-icons/im'
import {BsFillMoonFill} from 'react-icons/bs'

const NavBar = ({changeTheme,currentTheme}) => {
  const [navState, setnavState] = useState(false)
  const html = document.querySelector("html")
   html.addEventListener("click",() =>setnavState(false))
  return (
    // <div>
    //     <Navbar bg="dark" variant="dark">
    //     <Container>
    //       <Navbar.Brand href="#home">PhoneMate</Navbar.Brand>
    //       <Nav className="me-auto">
    //         {/* <Nav.Link href="/">Home</Nav.Link>
    //         <Nav.Link href="#features">Features</Nav.Link>
    //         <Nav.Link href="#pricing">Pricing</Nav.Link> */}
    //       </Nav>
    //     </Container>
    //   </Navbar>
    // </div>
    <nav>
      <div className="container py-3 mx-3">
        <div className="brand" onClick={() => {window.location.reload(true)}}>
          <span>PhoneMate</span>
          <span className="dot">.</span>
        </div>
        <div className="links-container" onClick={(e) => e.stopPropagation()}>
          <div className="toggle">
            {/* {navState ? (
              <MdClose onClick={() => setnavState(false)} />
            ) : (
              <GiHamburgerMenu
                onClick={(e) => {
                  e.stopPropagation();
                  setnavState(true);
                }}
              />
            )} */}
            <div onClick={changeTheme}>
              {currentTheme === "dark" ? (
                <ImSun className="sun" />
              ) : (
                <BsFillMoonFill className="moon" />
              )}
            </div>
          </div>
          <div className={`links ${navState ? "responsive-toggle" : ""}`}>
            <ul>
              {/* <li>
                <a onClick={() => {window.location.reload(true)}}> Home</a>
              </li> */}
              <li onClick={changeTheme} className="color-mode">
                {currentTheme === "dark" ? (
                 <>
                  <ImSun className="sun" />
                 </>
                ) : (
                  <BsFillMoonFill className="moon" />
                )}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default NavBar