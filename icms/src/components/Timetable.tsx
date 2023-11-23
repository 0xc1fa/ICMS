// components/DayColumn.jsx
import { Component, For, createEffect, onMount } from 'solid-js';
import { createSignal } from 'solid-js';
import { styled } from "solid-styled-components";
import axios from "axios";
import { authStore } from "../store/authStore";
import { hhmm } from "../helpers/formatDate";
import { CourseInfo } from "../dummydata/dummyCourseInfo";
import { CourseMaterial } from "../@types/CourseMaterial";

const hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19];

const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

type ClassTimeSlot = {
  course_id: string,
  class_time: string,
  classroom_address: string,
  teacher_message: string
  duration_hour: number,
  weekday: number,
  course_name: string,
  course_material: CourseMaterial[],
}


const TimeColumn: Component<{
}> = () => {

  return (
    <Time>
      <DayHeader>&nbsp;</DayHeader>
      <For each={hours}>
        {hour => <Hour>{hour}:30</Hour>}
      </For>
    </Time>
  );
}




export const WeekView: Component<{
  setModalCourse: (course: CourseInfo) => void,
  setCourseModalOpened: (opened: boolean) => void,
}> = (props) => {
  const [classes, setClasses] = createSignal<ClassTimeSlot[]>([])
  const [classArray, setClassArray] = createSignal<(ClassTimeSlot | null)[][]>([])

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
      course_name: row.course_name,
      course_material: [],
    })))

    for (const classSlot of classesResponse.data.rows) {
      const res = await axios.get(`http://localhost:8000/material/get/${classSlot.course_id}`)
      setClasses(classes().map((row) => {
        if (row.course_id === classSlot.course_id) {
          return {
            ...row,
            course_material: res.data.rows.map((row: any) => ({
              id: row.material_id,
              title: row.title,
              description: row.description,
              url: row.url,
            }))
          }
        }
        return row
      }))
    }
    console.log(classes())


    for (const day in daysOfWeek) {
      const dayArray: (ClassTimeSlot | null)[] = []
      for (const hour of hours) {
        let haveClass = false
        for (const classSlot of classes()) {
          if (isSameDay(classSlot, parseInt(day)) && overlapHour(classSlot, `${hour.toString().padStart(2, '0')}:30`)) {
            dayArray.push(classSlot)
            haveClass = true
          }
        }
        if (!haveClass) {
          dayArray.push(null)
        }
      }
      setClassArray([...classArray(), dayArray])
    }
    console.log(classArray())
  })


  const isSameDay = (classSlot: ClassTimeSlot, day: number): boolean => (
    classSlot.weekday === day
  )

  const overlapHour = (classSlot: ClassTimeSlot, hour: string): boolean => {
    for (let i = 0; i < classSlot.duration_hour; i++) {
      let classNow = new Date(classSlot.class_time)
      classNow.setHours(classNow.getHours() + i)
      if (hhmm(classNow) === hour) {
        return true
      }
    }
    return false
  }

  return (
    <Week class="unselectable">
      <TimeColumn />
      <For each={classArray()}>
      {(day, index) =>
        <Day>
          <DayHeader>{daysOfWeek[index()]}</DayHeader>
          <For each={day}>
          {timeSlot => {
              if (timeSlot !== null) {
                return (
                  <HightlightHour onClick={() => {
                    props.setModalCourse({
                      courseCode: timeSlot.course_id,
                      courseName: timeSlot.course_name,
                      courseMaterial: timeSlot.course_material,
                    })
                    props.setCourseModalOpened(true)
                  }}>
                    <b>{timeSlot.course_id}</b>
                    <div>{timeSlot.classroom_address}</div>
                  </HightlightHour>
                )
              } else {
                return <Hour>&nbsp;</Hour>
              }
            }
          }
          </For>
        </Day>
      }
      </For>
    </Week>
  );
}

const Week = styled('div')`
  display: grid;
  grid-template-columns: auto repeat(7, 1fr);
  gap: 1px;
  text-align: center;
  cursor: default;
  background-color: #d9ede8;
  border: 1px solid #b1c6e1;
  border-radius: 4px;
`
const Time = styled('div')`
  background-color: #45a08b;
  color: white;
`

const Day = styled('div')`
  /* border: 1px solid #e1e4e8; */
`

const DayHeader = styled('div')`
  padding: 4px;
  /* border-bottom: 1px solid #e1e4e8; */
  font-weight: bold;
  background-color: #45a08b;
  color: white;
`

const Hour = styled('div')`
  border-top: 1px solid #e1e4e8;
  padding: 8px;
  height: 50px;
`

const HightlightHour = styled('div')`
  border-top: 1px solid #e1e8e6;
  padding: 8px;
  height: 50px;
  background-color: #45a08b;
  color: white;
  border-radius: 8px;

  &:hover {
    background-color: #58b09b;
    color: white;
    cursor: pointer;
  }
`
