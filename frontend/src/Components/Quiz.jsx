import React, { useEffect, useState } from 'react'
import Product from './Product';
import axios from 'axios';
import scrollreveal from "scrollreveal"
import { LinearProgress } from '@material-ui/core';

const Quiz = () => {
  const [phones, setPhones] = useState([])
  const [over, setover] = useState(false)
  const [currentQuestion, setcurrentQuestion] = useState(0)
  const [Loading, setLoading] = useState(false)
  const [apicall, setapicall] = useState({
    "Camera" :false,
    "Storage" : false,
    "Usage":true,
    "Game":false,
    "Display":true,
    "Protection":true
  })


  const [Questionbank, setQuestionbank] = useState(
    [
      {
      Question: "Is a good Camera a priority for you?",
      AnswerText:
      [
        {Option: "Yes", type: "Camera"},
        {Option: "No", type: "Camera"}
      ],
      Answer: false
      },
      {
      Question: "Do you usually store a lot of pictures and videos on your phone ?",
      AnswerText:
      [
        {Option: "Yes", type: "Storage"},
        {Option: "No", type: "Storage"}
      ],
      Answer: false
      },
      {
        Question: "Do you spend more than 5 hours on your phone daily?",
        AnswerText:
        [
          {Option: "Yes", type: "Usage"},
          {Option: "No", type: "Usage"}
        ],
        Answer: false
      },
      {
        Question: "Do you play games often?",
        AnswerText:
        [
          {Option: "Yes", type: "Game"},
          {Option: "No", type: "Game"}
        ],
        Answer: false
      },
      {
        Question: "Do you binge watch on your phone a lot?",
        AnswerText:
        [
          {Option: "Yes", type: "Display"},
          {Option: "No", type: "Display"}
        ],
        Answer: false
      },
      {
        Question: "Do you drop phones more often than not?",
        AnswerText:
        [
          {Option: "Yes", type: "Protection"},
          {Option: "No", type: "Protection"}
        ],
        Answer: false
      }
    ]  
  )  

const handleAnswer = async(A) => {
  
  if(A.Option==="Yes")
  {
    setQuestionbank(Questionbank,Questionbank[currentQuestion].Answer=true)
  }
  const nextQuestion = currentQuestion +1
  if(nextQuestion<Questionbank.length){
    setcurrentQuestion(nextQuestion) 
  }
  else {
    Questionbank.map((question) => (
      setapicall(apicall,
          apicall[question.AnswerText[0].type]=question.Answer
      )
    )) 
    setLoading(true)
    console.log(apicall)
    await fetchPhones() 
    setLoading(false)
    setover(true)
    

    }
  }

  // const sleep = ms => new Promise(
  //   resolve => setTimeout(resolve, ms)
  // );

  const fetchPhones = async () =>{
    try{
      // await sleep(5000)
      await axios.post("phone/Phone/",apicall).then((response)=>{
        const res = response.data
        setPhones(res);
      })
    }catch(err){
      console.error(err);
    }
  }
  
  useEffect(() => {
    const registerAnimations = () => {
      const sr = scrollreveal({
        origin: "bottom",
        distance: "80px",
        duration: 1000,
        reset: false,
      });
      sr.reveal(
        `
        .title-container,
        .container 
    `,
        {
          interval: 500,
        }
      );
    };
    registerAnimations();
  }, []);


  return (
    <>
    { Loading ? <LinearProgress/> :
        
        over ? (<Product phones={phones}/>) :  (
    // <div className='home'>
    //      <div className='container mx-3 py-3'> 
    //     <div className='title-container'>
    //       {/* <span>{currentQuestion+1}</span><span>/</span><span>{Questionbank.length}</span> */}
    //       <h4>{Questionbank[currentQuestion].Question}</h4>
    //       </div>
    //       <div className="categories">
    //         {Questionbank[currentQuestion].AnswerText.map((Ans) =>{
    //           return(
    //             <div className="category" onClick={()=>{handleAnswer(Ans)}} key={Ans.Option}>
    //                 <h4 className=''>{Ans.Option}</h4>
    //             </div>
    //           )
    //         })}
    //         </div>
    //   </div>
    // </div>

    <div className="services-container mx-3 py-3">
    <div className="container">
      <div className="service one">
        <p>{currentQuestion+1} / {Questionbank.length}</p>
        <h4>{Questionbank[currentQuestion].Question}</h4>
      </div>
      {Questionbank[currentQuestion].AnswerText.map((Ans) =>{
              return(
      <div className="service two" onClick={()=>{handleAnswer(Ans)}} key={Ans.Option}>
        <div className="content">
          <h4>{Ans.Option}</h4>
        </div>
        <div className="image">
        </div>
      </div>
          )
                  })}
      </div>
  </div>


    )
      }
  </>
  )
}

export default Quiz