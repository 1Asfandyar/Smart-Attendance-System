import React, { useState } from "react";
import { LoadingButton } from "@mui/lab/";

const MyButton = ({ text, onClick, color = "primary", fullWidth = true }) => {
  const [fetching, setFetching] = useState(false);

  const clickHandler = async () => {
    setFetching(true);
    await onClick();
    setFetching(false);
  };

  return (
    <>
      <LoadingButton
        variant="contained"
        loading={fetching}
        color={color}
        onClick={clickHandler}
        fullWidth={fullWidth}
      >
        {text}
      </LoadingButton>
    </>
  );
};

export default MyButton;
