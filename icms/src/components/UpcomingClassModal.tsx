import { Modal } from "@suid/material"
import { Component, Setter } from "solid-js"
import { styled } from "solid-styled-components"
import { UpcomingClassItem } from "../dummydata/upcomingClass"
import { BiRegularX } from 'solid-icons/bi'

const UpcomingClassModal: Component<{
  upcomingClass: UpcomingClassItem,
  open: boolean,
  setOpen: Setter<boolean>
}> = (props) => {
  return (
    <ModalLayout open={props.open}>
      <Container>
        <Header>
          <hgroup>
            <b>{props.upcomingClass.courseCode}</b>
            <h2>{props.upcomingClass.courseName}</h2>
          </hgroup>
        </Header>
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

const Cross = styled(BiRegularX)`
  position: absolute;
  top: 1rem;
  right: 1rem;
  color: white;
  cursor: pointer;
`


export default UpcomingClassModal;
