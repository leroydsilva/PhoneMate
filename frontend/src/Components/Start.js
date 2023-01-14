import React from "react";
import Button from "react-bootstrap/esm/Button";
import { makeStyles } from '@material-ui/core';
import Typography from '@material-ui/core/Typography';
import Choose from "./Choose";



const Start = ({props}) => {
  return (
    <div className=''>
      <Choose props={props} />
      
    </div>
  );
};

export default Start;
