import { Modal } from "@suid/material"
import { Component, Setter, For } from "solid-js"
import { styled } from "solid-styled-components"
import { UpcomingClassItem } from "../dummydata/upcomingClass"
import { CourseMaterial } from "../@types/CourseMaterial"
import { BiRegularX } from 'solid-icons/bi'
import { css } from "solid-styled-components";

const UpcomingClassModal: Component<{
  upcomingClass: UpcomingClassItem,
  couseMaterial: CourseMaterial[]
  open: boolean,
  setOpen: Setter<boolean>
}> = (props) => {
  return (
    <ModalLayout open={props.open}>
      <Container>
        <Header>
          <hgroup>
            <div>
              <b>{props.upcomingClass.courseCode}</b>
              &nbsp-&nbsp
              {props.upcomingClass.courseTime}
              &nbsp@&nbsp
              {props.upcomingClass.classroomAddress}
              &nbsp/&nbsp
              <a href={props.upcomingClass.zoomLink} target="_blank"
                class={css`&:visited {color: white}`}>Zoom</a>
            </div>
            <h2>{props.upcomingClass.courseName}</h2>
          </hgroup>
        </Header>
        <Content>
          <For each={props.couseMaterial}>{(material, i) =>
            <MaterialItem>
              <h4><a href={material.url} target="_blank">{material.title}</a></h4>
              <div>{material.description}</div>
            </MaterialItem>
          }
          </For>
        </Content>
        <Cross onClick={() => props.setOpen(false)}/>
      </Container>
    </ModalLayout>
  )
}

const ModalLayout = styled(Modal)`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
`

const Container = styled('div')`
  position: relative;
  width: 50rem;
  height: 35rem;
  border-radius: 1rem;
  background-color: rgba(241,245,244,255);
  overflow: hidden;
`

const Header = styled('div')`
  background-color: #45a08b;
  color: white;
  height: 10rem;
  display: flex;
  flex-direction: column;
  justify-content: end;
  padding: 0.5rem 1rem;
`

const Content = styled('div')`
  padding: 1rem;
  overflow-y: scroll;
  overflow-x: scroll;
  height: 22rem;
`

const MaterialItem = styled('div')`

`

const Cross = styled(BiRegularX)`
  position: absolute;
  top: 1rem;
  right: 1rem;
  color: white;
  cursor: pointer;
`


export default UpcomingClassModal;
