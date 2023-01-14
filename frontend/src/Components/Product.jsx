import React, { useState } from 'react'
import { BsChevronDown } from "react-icons/bs";
import { BiSearch } from "react-icons/bi";
import { useEffect } from 'react';
const Product = ({phones}) => {
  const [Search, setSearch] = useState("")
  const [result, setresult] = useState([])

  const filteredData = phones.filter((el) => { //filterdata is function used for search
    //if no input the return the original
    if (Search === '') {
        return el
    }
    //return the item which contains the user input
    else  {
        return(el.Phone_name.toLowerCase().includes(Search))
    }
})

  // useEffect(() => {
  //   const filtered = phones.filter(p => p.Phone_name.toLowerCase().includes(Search))
  //   setresult(filtered)
  // }, [Search])
  

  return (
    <div className="products-container mx-3 py-3">
      <div className="container">
        <div className="title-container">
          <h2>Showing {phones.length} Results</h2>
          {/* <button>New Comparison</button> */}
        </div>
          <div className="input-container">
              <div className="icon">
                <BiSearch />
              </div>
            <input  type="text" placeholder="I want to buy..." value={Search} onChange={(e)=>{setSearch(e.target.value.toLowerCase())}} />
          </div>
        <div className="products">
          {
          filteredData.length > 0 ? (
            filteredData?.map(({ Phone_name, Phone_price, Phone_img }, index) => {
             return( 
              <div className="product" key={index}>  
              <div className="image">
                <img src={Phone_img} alt="Product" />
                </div>
                <h4>{Phone_name}</h4>
                <h4>₹ {Phone_price}</h4>
                <hr />
                  {/* <div className="processor">
                  <img src={processorimage} alt="processor" />
                  <h4>Processor</h4>
                  <p>{processor}</p>
                </div> */}
                {/* <div className="os">
                  <img src={osimage} alt="os" />
                  <h4>Operating System</h4>
                  <p>{os}</p>
                </div> */}
                {/* <BsChevronDown /> */}
              </div>
             )
            }
            )) :(
              <h2>No Result</h2>
            )
          }
        </div>
      </div>
    </div>
  );
}

export default Product