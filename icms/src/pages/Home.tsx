import { Component, createSignal, For } from "solid-js";
import { styled } from "solid-styled-components";
import NormalFlow from "../components/NormalFlowPage";
import UpcomingClassCard from "../components/UpcomingClassCard";
import dummyUpcomingClass from "../dummydata/upcomingClass";
import { dummyCourseMaterial } from "../dummydata/dummyCourseMaterial";
import UpcomingClassModal from "../components/UpcomingClassModal";
import { CourseInfo, dummyCourseInfo } from "../dummydata/dummyCourseInfo";
import CourseCard from "../components/CourseCard";
import CourseModal from "../components/CourseModal";

const Home: Component = () => {

  const options: Intl.DateTimeFormatOptions = { year: "numeric", month: 'long', day: 'numeric' };

  const [upcomingClass, setUpcomingClass] = createSignal(dummyUpcomingClass)
  const [modalCourse, setModalCourse] = createSignal(dummyCourseInfo[0])
  const dateTimeFormat = new Intl.DateTimeFormat('en-US', options);
  const [username, setUsername] = createSignal('User');
  const [loginTime, setLoginTime] = createSignal(dateTimeFormat.format(Date.now()));
  const [upcomingClassModalOpened, setUpcomingClassModalOpened] = createSignal(false);
  const [courseModalOpened, setCourseModalOpened] = createSignal(false);
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
        <UpcomingClassCard upcomingClass={upcomingClass()} onClick={() => setUpcomingClassModalOpened(true)}/>
        <UpcomingClassModal upcomingClass={upcomingClass()} couseMaterial={dummyCourseMaterial} open={upcomingClassModalOpened()} setOpen={setUpcomingClassModalOpened} />
      </Section>
      <Section>
        <h3>All Courses</h3>
        <Carousel>
          <For each={dummyCourseInfo}>
            {(course) => (
              <CourseCard upcomingClass={course} onClick={() => {
                setCourseModalOpened(true);
                setModalCourse(course);
              }}/>
            )}
          </For>
        </Carousel>
        <CourseModal course={modalCourse()} open={courseModalOpened()} setOpen={setCourseModalOpened} />
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
