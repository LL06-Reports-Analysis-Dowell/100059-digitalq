import React from "react";
import styled from "styled-components";

function CupertinoFooter21(props) {
  return (
    <Container {...props}>
      <BtnWrapper1>
        <ButtonOverlay>
          <img src={require("../assets/images/dowella.png")} alt="Dowell" />
        </ButtonOverlay>
      </BtnWrapper1>
      <BtnWrapper3>
        <ButtonOverlay>
          <img src={require("../assets/images/dowellb.png")} alt="Dowell" />
        </ButtonOverlay>
      </BtnWrapper3>
      <BtnWrapper4>
        <ButtonOverlay>
          <img src={require("../assets/images/dowellc.png")} alt="Dowell" />
        </ButtonOverlay>
      </BtnWrapper4>
      <BtnWrapper2>
        <ButtonOverlay>
          <img src={require("../assets/images/dowelld.png")} alt="Dowell" />
        </ButtonOverlay>
      </BtnWrapper2>
      <BtnWrapper5>
        <ButtonOverlay>
          <img src={require("../assets/images/dowellf.png")} alt="Dowell" />
        </ButtonOverlay>
      </BtnWrapper5>
      <BtnWrapper6>
        <ButtonOverlay>
          <img src={require("../assets/images/dowellg.png")} alt="Dowell" />
        </ButtonOverlay>
      </BtnWrapper6>
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

const Btn1Caption = styled.span`
  font-family: Roboto;
  background-color: transparent;
  padding-top: 4px;
  font-size: 12px;
`;

const BtnWrapper3 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

const Btn3Caption = styled.span`
  font-family: Roboto;
  background-color: transparent;
  padding-top: 4px;
  font-size: 12px;
  color: #9e9e9e;
`;

const BtnWrapper4 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

const Btn4Caption = styled.span`
  font-family: Roboto;
  background-color: transparent;
  padding-top: 4px;
  font-size: 12px;
  color: #9e9e9e;
`;

const BtnWrapper2 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

const Btn2Caption = styled.span`
  font-family: Roboto;
  background-color: transparent;
  padding-top: 4px;
  font-size: 12px;
  color: #9e9e9e;
`;

const BtnWrapper5 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

const Btn5Caption = styled.span`
  font-family: Roboto;
  background-color: transparent;
  padding-top: 4px;
  font-size: 12px;
  color: #9e9e9e;
`;

const BtnWrapper6 = styled.div`
  flex: 1 1 0%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: none;
  display: flex;
`;

const Btn7 = styled.span`
  font-family: Roboto;
  background-color: transparent;
  padding-top: 4px;
  font-size: 12px;
  color: #9e9e9e;
`;

export default CupertinoFooter21;
