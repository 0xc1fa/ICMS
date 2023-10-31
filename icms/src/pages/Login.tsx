import { Component } from "solid-js";
import { styled } from "solid-styled-components";
import Auth from "../components/Auth";

const Login: Component = () => {
  return (
    <Page>
      {/* <h1>ICMS: Login</h1>
      <p>ICMS is a CMS for the 21st century</p> */}
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
