import { NavLink, Outlet } from "@solidjs/router";
import { Component, JSX } from "solid-js";
import { styled } from "solid-styled-components";
import { Avatar } from "@suid/material"


const SidebarLayout: Component<{ children?: JSX.Element | JSX.Element[] }> = (props) => {
  return (
    <Page>
      <Sidebar class="unselectable">
        <ItemsList>
          <SectionTitle>Page Navigation</SectionTitle>
          <NavButton href="/home">Home</NavButton>
          <NavButton href="/history">History</NavButton>
          <NavButton href="/setting">Setting</NavButton>
        </ItemsList>
        <ItemsList>
          <SectionTitle>Feature Media</SectionTitle>
          <Droppable>
          </Droppable>
        </ItemsList>
        <Avatar style={{ "margin-top": "auto", "margin-left": "auto" }}/>
      </Sidebar>
      {props.children || <Outlet/>}
    </Page>
  );
};


const Page = styled('div')`
  background-color: #ecf0f0;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
`

const Sidebar = styled('aside')`
  display: flex;
  flex-direction: column;
  width: 12.5rem;
  height: 100vh;
  background-color: #f3f4f4;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  padding: 0 0.5rem;
  box-sizing: border-box;
  padding: 0.75rem;
  padding-top: 2.5rem;

  & a {
    display: block;
    padding: 10px;
    text-decoration: none;
    color: black;
  }
`

const ItemsList = styled('nav')`
  padding-bottom: 3rem;
`

const Droppable = styled('div')`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin: 0.5rem 1rem;
  flex-grow: 1;
`

const NavButton = styled(NavLink)`
  color: #444444 !important;
  font-weight: 600;
  text-decoration: none;
  transition: padding 0.2s ease-in-out, color 0.2s ease-in-out;
  padding-top: 5px !important;
  padding-bottom: 5px !important;

  &:hover {
    padding-left: 20px;
  }

  &.active {
    padding-left: 20px;
    color: rgba(69,160,140,255) !important;
  }
`;

const SectionTitle = styled('h2')`
  font-size: 0.75rem;
  font-weight: 500;
  color: #444444;
  margin: 0;
  padding-bottom: 0.25rem;
  margin: 0 0.5rem;
  border-bottom: 1px solid #e0e0e0;
  cursor: default;
`

export default SidebarLayout;
