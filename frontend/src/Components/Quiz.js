import React, { useEffect, useState } from 'react'
import Phone from './Phone'
import Button from 'react-bootstrap/Button';
import axios from 'axios';
const Quiz = () => {
  const [phones, setPhones] = useState([])
  const [over, setover] = useState(false)
  const [currentQuestion, setcurrentQuestion] = useState(0)
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
    console.log(apicall)
    await fetchPhones() 
    setover(true)
    

    }
  }

  const fetchPhones = async () =>{
    try{
      await axios.post("phone/Phone/Camera",apicall).then((response)=>{
        const res = response.data
        setPhones(res);
      })
    }catch(err){
      console.error(err);
    }
  }
  
  return (
    <>
    { over ? (<Phone phones={phones}/>) :  (
    <div>
         <div> 
        <span>{currentQuestion+1}</span>/<span>{Questionbank.length}</span>
        <div>
          <h2>{Questionbank[currentQuestion].Question}</h2>
          </div>
          <div>
            {Questionbank[currentQuestion].AnswerText.map((Ans) =>{
              return(
                <Button key={Ans.Option} variant="outline-primary" className='' onClick={()=>{handleAnswer(Ans)}} >{Ans.Option}</Button>
              )
            })}
            </div>
      </div>
    </div>
    )
      }
  </>
  )
}

export default Quiz