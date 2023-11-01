import { Component, createSignal } from "solid-js";
import { styled } from "solid-styled-components";
import NormalFlow from "../components/NormalFlowPage";


const Home: Component = () => {

  const [username, setUsername] = createSignal('User');
  const [loginTime, setLoginTime] = createSignal(Date.now());
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
      <p>Last login at {loginTime()}</p>
    </NormalFlow>
  )

}

type TimeSlot = {
  courseCode: string,
  time: number,
  duration: number,
}

export default Home;
