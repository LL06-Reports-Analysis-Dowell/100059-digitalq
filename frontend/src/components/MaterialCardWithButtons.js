import React, { Component } from "react";
import styled, { css } from "styled-components";
import { IoReloadCircleSharp } from "react-icons/io5";

function MaterialCardWithButtons(props) {
  return (
    <Container {...props}>
      <CardItemImagePlace
        src={require("../assets/images/cardImage.png")}></CardItemImagePlace>
      <ButtonGroup>
        <LeftBtn>
          <ButtonOverlay>
            <IoReloadCircleSharp />
          </ButtonOverlay>
        </LeftBtn>
        <CenterBtn>
          <ButtonOverlay>
            <IoReloadCircleSharp />
          </ButtonOverlay>
        </CenterBtn>
        <RightBtn>
          <ButtonOverlay>
            <IoReloadCircleSharp />
          </ButtonOverlay>
        </RightBtn>
      </ButtonGroup>
      <IoReloadCircleSharp />
    </Container>
  );
}

const Container = styled.div`
  display: flex;
  border-width: 1px;
  border-radius: 2px;
  border-color: #ccc;
  flex-wrap: nowrap;
  background-color: #fff;
  overflow: hidden;
  flex-direction: column;
  border-style: solid;
  position: relative;
  box-shadow: -2px 2px 1.5px 0.1px #000;
`;

const ButtonOverlay = styled.button`
  display: block;
  background: none;
  height: 100%;
  width: 100%;
  border: none;
`;
const CardItemImagePlace = styled.img`
  background-color: #ccc;
  min-height: 180px;
  left: 0px;
  width: 165px;
  top: 0px;
  height: 100%;
`;

const ButtonGroup = styled.div`
  padding: 8px;
  flex-direction: row;
  justify-content: space-around;
  display: flex;
`;

const LeftBtn = styled.div`
  padding: 8px;
  flex-direction: column;
  display: flex;
  border: none;
`;

const CenterBtn = styled.div`
  padding: 8px;
  flex-direction: column;
  display: flex;
  border: none;
`;

const RightBtn = styled.div`
  padding: 8px;
  flex-direction: column;
  display: flex;
  border: none;
`;

export default MaterialCardWithButtons;
