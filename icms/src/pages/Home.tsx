import { Component, createSignal } from "solid-js";
import { styled } from "solid-styled-components";
import NormalFlow from "../components/NormalFlowPage";
import UpcomingClassCard from "../components/UpcomingClassCard";
import dummyUpcomingClass from "../dummydata/upcomingClass";
import UpcomingClassModal from "../components/UpcomingClassModal";


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


  return (
    <NormalFlow>
      <h3>Welcome back, {username()}</h3>
      <p>Last login at: {loginTime()}</p>
      <UpcomingClassCard upcomingClass={dummyUpcomingClass} onClick={() => setModalOpened(true)}/>
      <UpcomingClassModal upcomingClass={dummyUpcomingClass} open={modalOpened()} setOpen={setModalOpened} />
    </NormalFlow>
  )

}

type TimeSlot = {
  courseCode: string,
  time: number,
  duration: number,
}

export default Home;
