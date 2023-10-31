import { Component } from "solid-js";
import { styled } from "solid-styled-components";

const Home: Component = () => {
  return (
    <Page>
      <h1>Home Page</h1>
      <p>This is the home page</p>
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

export default Home;
