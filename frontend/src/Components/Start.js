import React from "react";
import Button from "react-bootstrap/esm/Button";

const Start = ({props}) => {
  const startQuiz = () => props(true);

  return (
    <div>
      <h1>Take the Quiz when u want</h1>
      <Button
        onClick={() => {
          startQuiz()
        }}
        variant="outline-primary"
      >
        Lets Begin
      </Button>
    </div>
  );
};

export default Start;
