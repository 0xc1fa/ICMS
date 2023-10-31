import { NavLink, Outlet } from "@solidjs/router";
import { Component, JSX } from "solid-js";
import { styled } from "solid-styled-components";

const StyledAside = styled('aside')`
  width: 200px;
  height: 100vh;
  background-color: #f0f0f0;

  & a {
    display: block;
    padding: 10px;
    text-decoration: none;
    color: black;
  }
`

const Page = styled('div')`
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
`

const Sidebar: Component<{ children?: JSX.Element | JSX.Element[] }> = (props) => {
  return (
    <Page>
      <StyledAside >
        <NavLink href="/home">Home</NavLink>
        <NavLink href="/timetable">Timetable</NavLink>
        <NavLink href="/setting">Setting</NavLink>
      </StyledAside>
      {props.children || <Outlet/>}
    </Page>
  );
};

export default Sidebar;
