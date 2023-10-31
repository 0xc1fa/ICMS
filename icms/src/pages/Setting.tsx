import { Component } from "solid-js";
import { styled } from "solid-styled-components";

const Setting: Component = () => {
  return (
    <Page>
      <h1>Settting</h1>
      <p>This is the setting page</p>
    </Page>
  )
}

const Page = styled('div')`
  /* display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 50vh; */
`

export default Setting;
