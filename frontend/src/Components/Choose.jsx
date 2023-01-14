import React from 'react'
import Button from "react-bootstrap/esm/Button";
const Choose = ({props}) => {
  const startQuiz = () => props(true);
  return (
    <div className="choose-us-container mx-3 py-3">
      <div className="container">
            <div className="title-container">
                <h2>Why Choose PhoneMate?</h2>
                <p>
                    Welcome to PhoneMate,
                    the easy way to find your perfect phone.
                    Just answer a few questions about your needs and preferences, 
                    and we'll provide a personalized recommendation for the ideal phone for you. 
                    No more endless scrolling or guesswork - PhoneMate makes it simple to find your perfect phone match. Try it now!
                </p>

                
            </div>
            <Button className='button'
              onClick={() => {
                startQuiz()
              }}
            >
              Lets Begin
           </Button>
        </div>
    </div>
  )
}

export default Choose