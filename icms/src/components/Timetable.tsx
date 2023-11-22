// components/DayColumn.jsx
import { Component, For, createEffect, onMount } from 'solid-js';
import { createSignal } from 'solid-js';
import { styled } from "solid-styled-components";
import axios from "axios";
import { authStore } from "../store/authStore";
import { hhmm } from "../helpers/formatDate";

const hours = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19];

const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

type ClassTimeSlot = {
  course_id: string,
  class_time: string,
  classroom_address: string,
  teacher_message: string
  duration_hour: number,
  weekday: number,
}


const TimeColumn: Component<{
}> = () => {

  return (
    <Day>
      <DayHeader>&nbsp;</DayHeader>
      <For each={hours}>
        {hour => <Hour>{hour}:30</Hour>}
      </For>
    </Day>
  );
}





export const WeekView: Component = () => {
  // const [selectedDay, setSelectedDay] = createSignal(null);
  const [classes, setClasses] = createSignal<ClassTimeSlot[]>([])

  onMount(async () => {
    const classesResponse = await axios.get('http://localhost:8000/week-class/', {
      params: {
        student_id: authStore.studentId,
      }
    })
    setClasses(classesResponse.data.rows.map((row: any) => ({
      course_id: row.course_id,
      class_time: new Date(row.class_time),
      classroom_address: row.classroom_address,
      teacher_message: row.teacher_message,
      weekday: new Date(row.class_time).getDay(),
      duration_hour: row.duration_hour,
    })))
  })

  return (
    <Week class="unselectable">
      <TimeColumn />
      {daysOfWeek.map((day, index) => (
        <DayColumn day={index} classes={classes()} />
      ))}
    </Week>
  );
}


const DayColumn: Component<{
  day: number
  classes: ClassTimeSlot[]
}> = (props) => {

  const isSameDay = (classSlot: ClassTimeSlot): boolean => (
    classSlot.weekday === props.day
  )

  const overlapHour = (classSlot: ClassTimeSlot, hour: string): boolean => {
    return true;
    console.log(classSlot.duration_hour)
    for (let i = 0; i < classSlot.duration_hour; i++) {
      let classNow = new Date(classSlot.class_time)
      console.log(classNow, hour)
      classNow.setHours(classNow.getHours() + i)
      console.log(classNow, hour)
      if (hhmm(classNow) === hour) {
        return true
      }
    }
    return false
  }

  return (
    <Day>
      <DayHeader>{daysOfWeek[props.day]}</DayHeader>
      <For each={hours}>
        {hour => {
          console.log(props.classes)
          for (const classSlot of props.classes) {
            // overlapHour(classSlot, `${hour}:30`)
            // console.log()
            if (overlapHour(classSlot, `${hour}:30`)) {
              return <Hour>{classSlot.course_id}</Hour>
            }
          }
          return <Hour>&nbsp;</Hour>
        }}
      </For>
    </Day>
  );
}

const Week = styled('div')`
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 1px;
  text-align: center;
  cursor: default;
`

const Day = styled('div')`
  border: 1px solid #e1e4e8;
`

const DayHeader = styled('div')`
  background-color: #f0f0f0;
  padding: 4px;
  border-bottom: 1px solid #e1e4e8;
`

const Hour = styled('div')`
  border-top: 1px solid #e1e4e8;
  padding: 8px;
  height: 40px;
`
