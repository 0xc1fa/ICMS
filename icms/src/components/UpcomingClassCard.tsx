import { styled } from "solid-styled-components";
import { UpcomingClassItem } from "../dummydata/upcomingClass";
import { Component } from "solid-js";


const UpcomingClassCard: Component<{
  upcomingClass: UpcomingClassItem,
  onClick: (e: MouseEvent) => void
}> = (props) => {
  return (
    <Card onClick={props.onClick}>
      <hgroup>
        <b>{props.upcomingClass.courseCode}</b>
        <h2>{props.upcomingClass.courseName}</h2>
      </hgroup>
      <TwoSide>
        <span>{props.upcomingClass.courseTime} @ {props.upcomingClass.classroomAddress}</span>
        <span>{props.upcomingClass.teacherMessage}</span>
      </TwoSide>
    </Card>
  )
}


const Card = styled('div')`
  background-color: #45a08b;
  color: white;
  border-radius: 0.5rem;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  padding: 1rem;
  max-width: 900px;
  margin: 0.5rem 0;
  cursor: pointer;

  &:hover {
    background-color: #39917c;
    box-shadow: 0 0 10px rgba(0,0,0,0.2);
  }

  & * {
    color: white;
    margin: 0;
  }

  & h2 {
    margin-bottom: 1rem;
    line-height: 1.5;
    text-decoration: underline;
    margin-right: 4rem;
  }
`

const TwoSide = styled('div')`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
`

export default UpcomingClassCard;
