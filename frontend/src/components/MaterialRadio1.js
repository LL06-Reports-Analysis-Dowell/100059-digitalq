import React, { Component } from "react";
import styled, { css } from "styled-components";

function MaterialRadio1(props) {
  return (
    <Container {...props}>
      {/* <MaterialCommunityIconsIcon
        name={props.selected ? "radiobox-marked" : "radiobox-blank"}
        style={{
          color: "#3F51B5",
          fontSize: 23,
          lineHeight: "24px"
        }}
      ></MaterialCommunityIconsIcon> */}
      <input
        className="form-check-input position-relative"
        type="radio"
        name="exampleRadios"
        id="exampleRadios2"
        value="b"></input>
    </Container>
  );
}

const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 20px;
  background-color: transparent;
  flex-direction: column;
`;

export default MaterialRadio1;
