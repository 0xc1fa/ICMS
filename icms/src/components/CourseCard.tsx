import { styled } from "solid-styled-components";

import { Component } from "solid-js";
import { CourseInfo } from "../dummydata/dummyCourseInfo";


const CourseCard: Component<{
  upcomingClass: CourseInfo,
  onClick: (e: MouseEvent) => void
}> = (props) => {
  return (
    <Card onClick={props.onClick}>
      <hgroup>
        <CourseCode>{props.upcomingClass.courseCode}</CourseCode>
        <CourseName>{props.upcomingClass.courseName}</CourseName>
      </hgroup>
    </Card>
  )
}


const Card = styled('div')`
  background-color: #45a08b;
  color: white;
  border-radius: 0.5rem;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  padding: 1rem;
  margin: 0.5rem 0;
  width: 16rem !important;
  height: 6rem !important;
  height: 120px;
  cursor: pointer;
  flex: 0 0 250px;

  &:hover {
    background-color: #39917c;
    box-shadow: 0 0 10px rgba(19, 14, 14, 0.2);
  }
`

const CourseCode = styled('div')`
  color: white;
  margin: 0;
  font-size: smaller;
  text-align: right;
  font-weight: bold;
  /* font-size: x-small; */
`

const CourseName = styled('h2')`
  text-align: right;
  margin-bottom: 1rem;
  line-height: 1.5;
  text-decoration: underline;
  /* margin-right: 4rem; */
  font-size: larger;
`

export default CourseCard;
