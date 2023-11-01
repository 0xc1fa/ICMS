import { Component } from "solid-js";
import { styled } from "solid-styled-components";
import Auth from "../components/Auth";

const Login: Component = () => {
  return (
    <Page>
      <Auth/>
    </Page>
  )
}

const Page = styled('div')`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
`

export default Login;
