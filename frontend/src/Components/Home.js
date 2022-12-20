import React, { useEffect, useState } from 'react'
import Quiz from './Quiz';
import Button from 'react-bootstrap/Button';
import Start from './Start';

const Home = () => {
  // const [message, setmessage] = useState('')
  // useEffect(() => {
  //   fetch('/phone/Phone')
  //   .then(response => response.json())
  //   .then(data => 
  //     {
  //     console.log(data)
  //     setmessage(data.Phone_name)
  //     }
  //    )
    
    
  // }, [])
  const [start, setStart] = useState(false);
  

  return (
    <div> 
     {start ?(<Quiz/>):( <Start props={setStart} /> )
    }
    </div>
  )
  } 

export default Home;