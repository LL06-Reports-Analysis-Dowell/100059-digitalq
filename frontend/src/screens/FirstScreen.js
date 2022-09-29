import React from "react";
import styled from "styled-components";
import { AiFillPlusCircle } from "react-icons/ai";
import { Link } from "react-router-dom";

function FirstScreen(props) {
  return (
    <Container>
      <RectStack>
        <>
          <Image2></Image2>

          <Link to="/SecondScreen">
            <PlusIcon>
              <AiFillPlusCircle size="40px" color="green" />
            </PlusIcon>
          </Link>
        </>
      </RectStack>
    </Container>
  );
}

const Container = styled.div`
  display: flex;

  border-style: solid;
  position: absolute;
  padding: 50px 0;
  left: 30%;
  width: fit-content;
  height: fit-content;
`;

const Image2 = styled.div`
  top: -50px;
  left: 10px;
  width: 350px;
  height: 650px;
  position: absolute;
  flex-direction: column;
  display: flex;
  background-image: url(${require("../assets/images/do1.png")});
  background-size: cover;
`;

const PlusIcon = styled.div`
  width: 66px;
  height: 100%;
  position: absolute;
  top: 620px;
  left: 300px;
  object-fit: contain;
`;

const RectStack = styled.div`
  width: 381px;
  height: 660px;
  margin-top: 50px;
  position: relative;
  border-radius: 10px;
`;

export default FirstScreen;
