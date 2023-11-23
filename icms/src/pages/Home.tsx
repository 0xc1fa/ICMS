import { Component, createSignal, For, onMount } from "solid-js";
import { styled } from "solid-styled-components";
import NormalFlow from "../components/NormalFlowPage";
import UpcomingClassCard from "../components/UpcomingClassCard";
import dummyUpcomingClass, { UpcomingClassItem } from "../dummydata/upcomingClass";
import { dummyCourseMaterial } from "../dummydata/dummyCourseMaterial";
import UpcomingClassModal from "../components/UpcomingClassModal";
import { CourseInfo, dummyCourseInfo } from "../dummydata/dummyCourseInfo";
import CourseCard from "../components/CourseCard";
import CourseModal from "../components/CourseModal";
import axios from "axios";
import { authStore } from "../store/authStore";
import { CourseMaterial } from "../@types/CourseMaterial";
import { YYYYMMDD, hhmm } from "../helpers/formatDate"
import { WeekView } from "../components/Timetable";


const Home: Component = () => {
  const [currentTime, setCurrentTime] = createSignal(new Date(Date.now()));
  const [upcomingClass, setUpcomingClass] = createSignal<UpcomingClassItem | null>(null)
  const [upcomingClassMaterial, setUpcomingClassMaterial] = createSignal<CourseMaterial[] | null>(null)
  const [modalCourse, setModalCourse] = createSignal(dummyCourseInfo[0])
  const [loginTime, setLoginTime] = createSignal(`${YYYYMMDD(currentTime())} ${hhmm(currentTime())}`);
  const [upcomingClassModalOpened, setUpcomingClassModalOpened] = createSignal(false);
  const [courseModalOpened, setCourseModalOpened] = createSignal(false);
  const [allCourseInfo, setAllCourseInfo] = createSignal<CourseInfo[]>([]);


  onMount(async () => {
    const upcomingClassResult = (await axios.get(`http://localhost:8000/upcoming-class/get/${authStore.studentId}`)).data.rows
    const upcomingClassMapping = upcomingClassResult.map((row: any) => ({
      courseCode: row.course_id,
      courseName: row.course_name,
      courseTime: `${YYYYMMDD(new Date(row.class_time))} ${hhmm(new Date(row.class_time))}`,
      classroomAddress: row.classroom_address,
      teacherMessage: row.teacher_message,
      zoomLink: row.zoom_link,
      classId: row.class_id,
    }))
    setUpcomingClass(upcomingClassMapping.length > 0 ? upcomingClassMapping[0] : null);

    if (upcomingClass() !== null) {
      const upcomingClassMaterialResult = (await axios.get(`http://localhost:8000/material/get/${upcomingClass()!.courseCode}`)).data.rows
      setUpcomingClassMaterial(upcomingClassMaterialResult.map((row: any) => ({
        id: row.material_id,
        title: row.title,
        description: row.description,
        url: row.url,
      })))
    }

    const allCourseInfo = (await axios.get(`http://localhost:8000/course/get/${authStore.studentId}`)).data.rows
    let allCourseInfoWithMaterial: CourseInfo[] = []
    for (const course of allCourseInfo) {
      const courseMaterial = (await axios.get(`http://localhost:8000/material/get/${course.course_id}`)).data.rows
      allCourseInfoWithMaterial.push({
        courseCode: course.course_id,
        courseName: course.course_name,
        courseMaterial: courseMaterial
      })
    }
    setAllCourseInfo(allCourseInfoWithMaterial)
  })


  return (
    <NormalFlow>
      <h3>Welcome back, {authStore.name}</h3>
      <p>Last login at: {loginTime()}</p>
      <Section>
        <h3>All Courses</h3>
        <Carousel>
          <For each={allCourseInfo()}>
            {(course) => (
              <CourseCard upcomingClass={course} onClick={() => {
                setCourseModalOpened(true);
                setModalCourse(course);
                (course);
              }}/>
            )}
          </For>
        </Carousel>
        <CourseModal course={modalCourse()} open={courseModalOpened()} setOpen={setCourseModalOpened} />
      </Section>
      <Section>
        <h3>Upcoming Class</h3>
        {
          upcomingClass() === null ?
          <WeekView setModalCourse={setModalCourse} setCourseModalOpened={setCourseModalOpened}/> :
          <>
            <UpcomingClassCard upcomingClass={upcomingClass()!} onClick={() => setUpcomingClassModalOpened(true)} />
            <UpcomingClassModal upcomingClass={upcomingClass()!} couseMaterial={upcomingClassMaterial()!} open={upcomingClassModalOpened()} setOpen={setUpcomingClassModalOpened} />
          </>
        }
      </Section>
    </NormalFlow>
  )
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
