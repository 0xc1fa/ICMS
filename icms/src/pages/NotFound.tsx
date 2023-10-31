import { Component } from "solid-js";
import { styled } from "solid-styled-components";

const NotFound: Component = () => (
  <Page>
    <h1>404 Error: Page not found</h1>
    <p>The page you navigate to does not exist</p>
  </Page>
)

const Page = styled('div')`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 50vh;
`

export default NotFound;
