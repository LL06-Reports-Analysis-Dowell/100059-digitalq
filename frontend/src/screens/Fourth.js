import React from "react";
import styled from "styled-components";
import { AiFillPlusCircle } from "react-icons/ai";
import { Carousel } from "@trendyol-js/react-carousel";

function Fourth(props) {
  const handleOnChange = (value) => {
    console.log(value);
    this.setState({ phone: value }, () => {
      console.log(this.state.phone);
    });
  };
  return (
    <Container>
      <RectStack>
        <Rect2>
          <TextHead>Hi, Christ Select From Menu</TextHead>
          <hr
            style={{
              marginLeft: "0",
              width: "95%",
              marginTop: "5px",
              borderColor: "green",
            }}
          />
          <Image3 src={require("../assets/images/logo.png")}></Image3>
          <Brand>brand of cafe, branch</Brand>
        </Rect2>
      </RectStack>
    </Container>
  );
}
const Highlight = styled.div`
  height: '200px',
  margin: '6px',
  padding: '5px',
  border: '3px',
  borderColor: 'green',
  `;

const Container = styled.div`
  // display: flex;
  // border-width: 0px;
  // border-color: rgba(65, 117, 5, 1);
  // border-radius: 5px;
  // flex-direction: column;
  border-style: solid;
  position: absolute;
  left: 30%;
`;
const TextHead = styled.div`
  padding-left: 10px;
  padding-top: 20px;
  font-size: 20px;
  font-style: italic;
`;

const Image3 = styled.img`
  top: 0px;
  left: 300px;
  width: 50px;
  height: 65px;
  position: absolute;
  object-fit: contain;
`;
const Rect2 = styled.div`
  top: -25px;
  left: 13px;
  width: 357px;
  height: 740px;
  position: absolute;
  background-color: rgba(212, 253, 194, 0.91);
  border-width: 1px;
  border-color: rgba(0, 0, 0, 1);
  flex-direction: column;
  display: flex;
  border-style: solid;
  border-radius: 5%;
`;

const FoodList = styled.div`
  top: 70px;
  left: 0px;
  position: absolute;
`;
const Brand = styled.span`
  font-family: Roboto;
  top: 70px;
  left: 0px;
  position: absolute;
  font-style: normal;
  font-weight: 500;
  color: #121212;
  height: 32px;
  width: 357px;
  text-align: center;
  font-size: 20px;
`;

const RectStack = styled.div`
  width: 381px;
  height: 738px;
  margin-top: 50px;
  position: relative;
  border-radius: 10px;
`;

export default Fourth;
