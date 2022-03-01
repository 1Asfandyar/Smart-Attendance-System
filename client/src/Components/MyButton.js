import React, { useState } from "react";
import { Button, CircularProgress } from "@mui/material";

const MyButton = ({ text, onClick, size = 40, color = "inherit" }) => {
  const [fetching, setFetching] = useState(false);

  const clickHandler = async () => {
    setFetching(true);
    await onClick();
    setFetching(false);
  };

  return (
    <>
      <Button variant="contained" color={color} onClick={clickHandler}>
        {fetching ? <CircularProgress size={size} /> : text}
      </Button>
    </>
  );
};

export default MyButton;
