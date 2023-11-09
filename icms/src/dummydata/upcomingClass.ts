const dummyUpcomingClass = {
  courseCode: "COMP3278",
  courseName: "Introduction to database management systems",
  courseTime: "10:00 - 11:50",
  classroomAddress: "MW L2",
  teacherMessage: "Work harder!",
  zoomLink: "https://zoom.us/j/1234567890?pwd=QWERTYUIOPASDFGHJKLZXCVBNM",
}

export type UpcomingClassItem = {
  courseCode: string,
  courseName: string,
  courseTime: string,
  classroomAddress: string,
  teacherMessage: string,
  zoomLink: string,
}


export default dummyUpcomingClass;
