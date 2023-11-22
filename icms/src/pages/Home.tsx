import { Component, createSignal, For } from "solid-js";
import { styled } from "solid-styled-components";
import NormalFlow from "../components/NormalFlowPage";
import UpcomingClassCard from "../components/UpcomingClassCard";
import dummyUpcomingClass from "../dummydata/upcomingClass";
import { dummyCourseMaterial } from "../dummydata/dummyCourseMaterial";
import UpcomingClassModal from "../components/UpcomingClassModal";
import { CourseInfo, dummyCourseInfo } from "../dummydata/dummyCourseInfo";
import CourseCard from "../components/CourseCard";

const Home: Component = () => {

  const options: Intl.DateTimeFormatOptions = { year: "numeric", month: 'long', day: 'numeric' };
  const dateTimeFormat = new Intl.DateTimeFormat('en-US', options);
  const [username, setUsername] = createSignal('User');
  const [loginTime, setLoginTime] = createSignal(dateTimeFormat.format(Date.now()));
  const [modalOpened, setModalOpened] = createSignal(false);
  const [timetable, setTimetable] = createSignal<TimeSlot[]>([
    {
      courseCode: 'COMP3278',
      time: Date.now(),
      duration: 3600,
    }
  ])

  let hello = "hello"
  console.log(hello)

  return (
    <NormalFlow>
      <h3>Welcome back, {username()}</h3>
      <p>Last login at: {loginTime()}</p>
      <Section>
        <h3>Upcoming Class</h3>
        <UpcomingClassCard upcomingClass={dummyUpcomingClass} onClick={() => setModalOpened(true)}/>
        <UpcomingClassModal upcomingClass={dummyUpcomingClass} couseMaterial={dummyCourseMaterial} open={modalOpened()} setOpen={setModalOpened} />
      </Section>
      <Section>
        <h3>All Courses</h3>
        <Carousel>
          <For each={dummyCourseInfo}>
            {(course) => (
              <CourseCard upcomingClass={course} onClick={() => setModalOpened(true)}/>
            )}
          </For>
        </Carousel>
      </Section>
    </NormalFlow>
  )

}

type TimeSlot = {
  courseCode: string,
  time: number,
  duration: number,
}

const Section = styled('div')`
  gap: 4px;
  margin: 1rem 0;
  width: 100%;
`

const Carousel = styled('div')`
  width: 100%;
  position: relative;
  display: flex;
  flex: 0 0 800px;
  overflow-x: hidden;
  gap: 1rem;
`

export default Home;
