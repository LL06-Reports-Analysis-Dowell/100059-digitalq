import React, { Component } from "react";
import styled, { css } from "styled-components";
import { IoReloadCircleSharp } from "react-icons/io5";
import { TbPower, TbShieldCheck } from "react-icons/tb";
import { FaUserCircle } from "react-icons/fa";

function CupertinoFooter2(props) {
  return (
    <Container {...props}>
      <BtnWrapper1>
        <ButtonOverlay>
          <TbPower size="40px" />
        </ButtonOverlay>
      </BtnWrapper1>
      <BtnWrapper3>
        <ButtonOverlay>
          <TbShieldCheck size="40px" />
        </ButtonOverlay>
      </BtnWrapper3>
      <BtnWrapper4>
        <ButtonOverlay>
          <img src={require("../assets/images/reward.png")} />
        </ButtonOverlay>
      </BtnWrapper4>
      <BtnWrapper2>
        <ButtonOverlay>
          <img src={require("../assets/images/dowellcart.png")} />
        </ButtonOverlay>
      </BtnWrapper2>
      <Rect>
        <img src={require("../assets/images/dowelluser.png")} />
      </Rect>
      <BtnWrapper5>
        <ButtonOverlay>
          <FaUserCircle size="40px" />
        </ButtonOverlay>
      </BtnWrapper5>
    </Container>
  );
}

const Container = styled.div`
  display: flex;
  flex-direction: row;

  justify-content: space-between;
`;

const ButtonOverlay = styled.button`
  display: block;
  background: none;
  height: 100%;
  width: 100%;
  border: none;
`;
const BtnWrapper1 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

const BtnWrapper3 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

const BtnWrapper4 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

const BtnWrapper2 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

const Rect = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  display: flex;
`;

const BtnWrapper5 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

export default CupertinoFooter2;
