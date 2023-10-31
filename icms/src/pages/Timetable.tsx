import { Component } from "solid-js";
import { styled } from "solid-styled-components";

const Timetable: Component = () => {
  return (
    <Page>
      <h1>Timetable</h1>
      <p>This is the timetable page</p>
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

export default Timetable;
